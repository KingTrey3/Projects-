"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi
from math import sqrt

__author__ = "730482751" 


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Returns distance between points."""
        distance: float = sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Used for ticks."""
        self.location = self.location.add(self.direction)
        if self.is_infected() is True:
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
                
    # def color(self) -> str:
    # """Return the color representation of a cell."""
    # return "black"

    def contract_disease(self) -> None:
        """Assign the Infected constant to sickness attribute."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Returns True when the cell's sickness attribute is equal to Vulnerable and False."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Returns true when the cell's sickness is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False                    

    def color(self) -> str:
        """Returns gray if cell is vulnerable or green if infected."""
        if self.is_infected():
            return constants.GREEN
        if self.is_vulnerable():
            return constants.GRAY 
        if self.is_immune():
            return constants.BLUE

    def contact_with(self, other: Cell) -> None:
        """Infects cells that come into contact."""
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()   
        if other.is_infected() and self.is_vulnerable():
            self.contract_disease()

    def immunize(self) -> None:
        """Assigns the constat Immune to the Sickness attribute."""
        self.sickness = constants.IMMUNE         
                 
    def is_immune(self) -> bool:
        """Returns True when the cell's object is equal to immune."""
        if self.sickness == constants.IMMUNE:
            return True


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        if infected >= cells or infected <= 0:
            raise ValueError("Cell objects must begin infected.")
        if immune + infected > cells or immune < 0:
            raise ValueError("Improper number of immune or infected cells.")    
        self.population = []
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if _ < infected:
                cell.contract_disease()
            elif _ < infected + immune:
                cell.immunize()
            self.population.append(cell)     
        
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed 
        direction_y: float = sin(random_angle) * speed 
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0          

    def check_contacts(self) -> None:
        """Tests if cells come into contact."""
        i: int = 0
        while i < len(self.population):
            j: int = i + 1
            while j < len(self.population):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])
                j += 1    
            i += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        i: int = 0
        complete: bool = True
        while i < len(self.population):
            if self.population[i].is_infected():
                complete = False
            
            i += 1

        return complete