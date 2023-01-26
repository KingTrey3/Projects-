"""Choose Your Own Adventure."""

__author__ = "730482571"

points: int = 0
player: str = ""
player_hp: int = 100
GREEN_BOX: str = "\U0001F7E9"


def greet() -> None:
    """Opening of the game."""
    print("You there! Come over here quickly!")
    name_input: str = input("what is your name? ")
    global player
    if len(name_input) > 0:
        player = name_input
    print("The kingdom of Compsciland in the land of Chapelill has been attacked by evil enemies. They have stolen the sacred adventure points from our castle. I tried to go after them but alas, I have not been chosen by the sacred weapons. As a result I was defeated in combat by the most evil one.")
    print(f"However, I sense something deep with you, {player}.")
    

def end_of_journey(decision: str) -> None:
    """Path 1 was chosen."""
    print("I can not judge you.")
    print("You have stumbled upon a kingdom in ruins.")
    print("You must not have been the hero I was searching for...")
    print(f"Goodbye {player}, safe travels.")
    print("...")
    print("[The Kingdom was overun with monsters and destroyed.]")
    print(f"[Adventure Points {points}]")
    quit()


def weapon_selection(selected_path: str) -> int:
    """Sacred weapon selection."""
    print("While escaping the castle, I managed to take five of the sacred weapons with me.")
    print("The sacred weapons are tools crafted by legendary toolsmiths and have been imbued with powerful magic.")
    print("[The sacred tools begin to glow]")
    print("There is a Sword, Spear, Bow, Katana, and Battle Axe.")
    print("Which of these weapons resonates with you the most?")
    print("1 - Sword")
    print("2 - Spear")
    print("3 - Bow")
    print("4 - Katana")
    print("5 - Battle axe")
    sacred_weapon: str = input("Choose a weapon. ")
    if sacred_weapon == "1":
        print(f"[{player} picked up the Sword.]")
        print("[The sword begins to emit a mysterious energy.]")
        print("You have picked the Sword. This sword was forged here in Chapelill by a group of the greatest toolsmiths centuries ago.")
        print("This weapon retains the enegery and magic of its previous weilders. To be chosen by this weapon is a great honor.")
    if sacred_weapon == "2":
        print(f"[{player} picked up the Spear.]")
        print("[The spear begins to emit a mysterious energy.]")
        print("You have picked the Spear. The spear was forged in the land of the giants. The sorcerers from the land of the giants condensed the spear to be wielded by a human")
        print("This spear was gifted to us by the royal giant family after it was condensed.")
    if sacred_weapon == "3":
        print(f"[{player} picked up the Bow.]")
        print("[The Bow begins to emit a mysterious energy.]")
        print("You have picked the Bow. This ancient weapon was crafted by the elves in the hidden forest.")
        print("The magic in the bow allows it to never run out of arrows.")
    if sacred_weapon == "4":
        print(f"[{player} picked up the Katana.]")
        print("You have picked the Katana. The katana was forged in the lands in the far east where the sun rises.")
        print("The legendary blacksmiths from the east have found a way to create an indestructable weapon.")
        print("With this your cuts will be quick and precise.")
    if sacred_weapon == "5":
        print(f"[{player} picked up the Battle Axe.]")
        print("[The ground shakes.]")
        print("This axe was forged in the land of the vikings in the north.")
        print("A legendary hero who was rummored to have the ability to create tremors and earthquakes once wielded this axe.")    
    return int(sacred_weapon)


def game_over(player_hp: int) -> None:
    """Game Over."""
    if player_hp == 0:
        print(f"{player}'s HP has reached 0")
        print("...")
        print("[As your conscious begins to fade you hear a voice...]")
        print("Another hero has fallen to evil.")
        print("It appears that you were not the chosen one the kingdom was looking for.")
        print(f"[Adventure Points: {points}]")
        print("GAME OVER")
        quit()
    return None


def final_scene(points: int, path_choice: str) -> int:
    """Final scene of game."""
    if points == 30:
        print("[After the defeat of Akuma with all of the Adventure Points that were stolen you were able to restore the kingdom to its formor glory due to their magical properties.]")
        print("[The survivng memmbers of the royal family threw a celebration for you and had a ceremony in your honor.]")
        print(f"[The {path_choice} was not easy.]")
        print("[Your name will go down in history as the name of a hero.]")
        print("[You have saved the kingdom and created a future for generations to come.]")
        print(f"[Adventure Points]: {points}")
        print(f"{GREEN_BOX}THANK YOU FOR PLAYING {GREEN_BOX}")
        print("THE END")
        quit()
    if points < 30:
        return points    
    return 1


def katana_system(weapon_name: int) -> int:
    """Katana chosen as weapon."""
    tenkiri = 10
    # Heavenly Slash 
    iai = 20
    # Quick draw
    ryunokamu = 30
    # Dragon Chomp
    print("1 - Tenkiri (10 damage)")
    print("2 - Iai (20 damage)")
    print("3 - Ryunokamu (30 damage)")
    attack: str = input("Input your attack! ")
    if attack == "1":
        print(f"{player} used Tenkiri!")
        return tenkiri
    if attack == "2":
        print(f"{player} used Iai!")
        return iai
    if attack == "3":
        print(f"{player} used Ryunokamu!")
        return ryunokamu
    return 1


def sword_system(weapon_name: int) -> int:
    """Sword chosen as weapon."""
    two_hand_slash = 10
    stab = 20
    cross_slash = 30
    print("1 - Two Handed Slash (10 damage)")
    print("2 - Stab (20 damage)")
    print("3 - Cross Slash (30 damage)")
    attack: str = input("Input your attack! ")
    if attack == "1":
        print(f"{player} used Two Handed Slash!")
        return two_hand_slash
    if attack == "2":
        print(f"{player} used Stab!")
        return stab
    if attack == "3":
        print(f"{player} used Cross Slash!")
        return cross_slash
    return 1 


def spear_system(weapon_name: int) -> int:
    """Spear chosen as weapon."""
    super_strike = 10
    quick_thrust = 20
    javelin_throw = 30
    print("1 - Super Strike (10 damage)")
    print("2 - Quick Thrust (20 damage)")
    print("3 - Javelin Throw (30 damage)")
    attack: str = input("Input your attack! ")
    if attack == "1":
        print(f"{player} used Super Strike!")
        return super_strike
    if attack == "2":
        print(f"{player} used Quick Thrust!")
        return quick_thrust
    if attack == "3":
        print(f"{player} used Javelin Throw!")
        return javelin_throw
    return 1


def bow_system(weapon_name: int) -> int:
    """Bow chosen as weapon."""
    charged_shot = 10
    multi_arrow_shot = 20
    quick_shot = 30
    print("1 - Charged Shot (10 damage)")
    print("2 - Multi Arrow Shot (20 damage)")
    print("3 - Quick Shot (30 damage)")
    attack: str = input("Input your attack! ")
    if attack == "1":
        print(f"{player} used Charged Shot!")
        return charged_shot
    if attack == "2":
        print(f"{player} used Multi Arrow Shot!")
        return multi_arrow_shot
    if attack == "3":
        print(f"{player} used Quick Shot!")
        return quick_shot
    return 1


def battle_axe_system(weapon_name: int) -> int:
    """Battle Axe chosen as weapon."""
    viking_throw = 10
    overhead_slash = 20
    lumberjack_strike = 30
    print("1 - Viking Throw (10 damage)")
    print("2 - Overhead Slash (20 damage)")
    print("3 - Lumberjack Strike (30 damage)")
    attack: str = input("Input your attack! ")
    if attack == "1":
        print(f"{player} used Viking Throw!")
        return viking_throw
    if attack == "2":
        print(f"{player} used Overhead Slash!")
        return overhead_slash
    if attack == "3":
        print(f"{player} used Lumberjack Strike!")
        return lumberjack_strike
    return 1


def enemy_system_one(enemy_name: str) -> int:
    """Radom Number Generated enemy combat."""
    import random
    dark_slash = 5
    purple_twin_strike = 10
    air_cutter = 25
    enemy_attack = random.choice([dark_slash, purple_twin_strike, air_cutter])
    if enemy_attack == dark_slash:
        print(f"{enemy_name} used Dark Slash!")
        return dark_slash
    if enemy_attack == purple_twin_strike:
        print(f"{enemy_name} used Purple Twin Strike!")
        return purple_twin_strike
    if enemy_attack == air_cutter:
        print(f"{enemy_name} used Air Cutter!")
        return air_cutter
    return 1


def enemy_system_two(enemy_name: str) -> int:
    """Second system for enemy."""
    import random
    tetsu_punch = 10
    strong_counter = 15
    great_suplex = 30
    enemy_attack = random.choice([tetsu_punch, strong_counter, great_suplex])
    if enemy_attack == tetsu_punch:
        print(f"{enemy_name} used Tetsu Punch!")
        return tetsu_punch
    if enemy_attack == strong_counter:
        print(f"{enemy_name} used Strong Counter!")
        return strong_counter
    if enemy_attack == great_suplex:
        print(f"[{enemy_name}]: No one survives this one.")
        print(f"{enemy_name} used Great Suplex!")
        return great_suplex
    return 1


def enemy_system_boss(enemy_name: str) -> int:
    """Boss fight."""
    import random
    jigokukiri = 20
    cursed_flurry = 30
    ending_blow = 50
    enemy_attack = random.choice([jigokukiri, cursed_flurry, ending_blow])
    if enemy_attack == jigokukiri:
        print(f"[{enemy_name}'s Cursed Blade Yoru glows...]")
        print(f"{enemy_name} used Jigokukiri!")
        return jigokukiri
    if enemy_attack == cursed_flurry:
        print(f"{enemy_name} used Cursed Flurry!")
        return cursed_flurry
    if enemy_attack == ending_blow:
        print(f"[{enemy_name}]: You won't escape! Ending Blow!!!")
        print(f"{enemy_name} used ENDING BLOW!")
        return ending_blow
    return 1


def battle_system_katana(player_hp: int, enemy_hp: int, enemy_name: str) -> int:
    """Turn based combat system."""
    while player_hp > 0 and enemy_hp > 0:
        enemy_hp -= katana_system(4)
        if enemy_hp < 0:
            enemy_hp = 0
        print(f"{enemy_name} has {enemy_hp} HP remaning.")
        player_hp -= enemy_system_one(f"{enemy_name}")
        if player_hp < 0:
            player_hp = 0
        print(f"{player} has {player_hp} HP remaining.")
        if player_hp == 0:
            game_over(player_hp)
        if enemy_hp == 0:
            print("You won")
            return 1    
    return 1


def battle_system_katana_two(player_hp: int, enemy_hp: int, enemy_name: str) -> int:
    """Turn based combat system."""
    while player_hp > 0 and enemy_hp > 0:
        enemy_hp -= katana_system(4)
        if enemy_hp < 0:
            enemy_hp = 0
        print(f"{enemy_name} has {enemy_hp} HP remaning.")
        player_hp -= enemy_system_two(f"{enemy_name}")
        if player_hp < 0:
            player_hp = 0
        print(f"{player} has {player_hp} HP remaining.")
        if player_hp == 0:
            game_over(player_hp)
        if enemy_hp == 0:
            print("You won")
            return 1
    return 1


def battle_system_katana_boss(player_hp: int, enemy_hp: int, enemy_name: str) -> int:
    """Turn based combat system."""
    sacred_water: int = 25
    player_hp += sacred_water
    print(f"[The Sacred Water has given you {sacred_water} more HP!]")
    while player_hp > 0 and enemy_hp > 0:
        enemy_hp -= katana_system(4)
        if enemy_hp < 0:
            enemy_hp = 0
        print(f"{enemy_name} has {enemy_hp} HP remaning.")
        player_hp -= enemy_system_boss(f"{enemy_name}")
        if player_hp < 0:
            player_hp = 0
        print(f"{player} has {player_hp} HP remaining.")
        if player_hp == 0:
            game_over(player_hp)
        if enemy_hp == 0:
            print("You won")
            return 1    
    return 1


def battle_system_sword(player_hp: int, enemy_hp: int, enemy_name: str) -> int:
    """Turn based combat system."""
    while player_hp > 0 and enemy_hp > 0:
        enemy_hp -= sword_system(1)
        if enemy_hp < 0:
            enemy_hp = 0
        print(f"{enemy_name} has {enemy_hp} HP remaning.")
        player_hp -= enemy_system_one(f"{enemy_name}")
        if player_hp < 0:
            player_hp = 0
        print(f"{player} has {player_hp} HP remaining.")
        if player_hp == 0:
            game_over(player_hp)
        if enemy_hp == 0:
            print("You won")
            return 1    
    return 1


def battle_system_sword_two(player_hp: int, enemy_hp: int, enemy_name: str) -> int:
    """Turn based combat system."""
    while player_hp > 0 and enemy_hp > 0:
        enemy_hp -= sword_system(1)
        if enemy_hp < 0:
            enemy_hp = 0
        print(f"{enemy_name} has {enemy_hp} HP remaning.")
        player_hp -= enemy_system_two(f"{enemy_name}")
        if player_hp < 0:
            player_hp = 0
        print(f"{player} has {player_hp} HP remaining.")
        if player_hp == 0:
            game_over(player_hp)
        if enemy_hp == 0:
            print("You won")
            return 1    
    return 1


def battle_system_sword_boss(player_hp: int, enemy_hp: int, enemy_name: str) -> int:
    """Turn based combat system."""
    sacred_water: int = 25
    player_hp += sacred_water
    print(f"[The Sacred Water has given you {sacred_water} more HP!]")
    while player_hp > 0 and enemy_hp > 0:
        enemy_hp -= sword_system(1)
        if enemy_hp < 0:
            enemy_hp = 0
        print(f"{enemy_name} has {enemy_hp} HP remaning.")
        player_hp -= enemy_system_boss(f"{enemy_name}")
        if player_hp < 0:
            player_hp = 0
        print(f"{player} has {player_hp} HP remaining.")
        if player_hp == 0:
            game_over(player_hp)
        if enemy_hp == 0:
            print("You won")
            return 1    
    return 1


def battle_system_spear(player_hp: int, enemy_hp: int, enemy_name: str) -> int:
    """Turn based combat system."""
    while player_hp > 0 and enemy_hp > 0:
        enemy_hp -= spear_system(2)
        if enemy_hp < 0:
            enemy_hp = 0
        print(f"{enemy_name} has {enemy_hp} HP remaning.")
        player_hp -= enemy_system_one(f"{enemy_name}")
        if player_hp < 0:
            player_hp = 0
        print(f"{player} has {player_hp} HP remaining.")
        if player_hp == 0:
            game_over(player_hp)
        if enemy_hp == 0:
            print("You won")
            return 1
    return 1


def battle_system_spear_two(player_hp: int, enemy_hp: int, enemy_name: str) -> int:
    """Turn based combat system."""
    while player_hp > 0 and enemy_hp > 0:
        enemy_hp -= spear_system(2)
        if enemy_hp < 0:
            enemy_hp = 0
        print(f"{enemy_name} has {enemy_hp} HP remaning.")
        player_hp -= enemy_system_two(f"{enemy_name}")
        if player_hp < 0:
            player_hp = 0
        print(f"{player} has {player_hp} HP remaining.")
        if player_hp == 0:
            game_over(player_hp)
        if enemy_hp == 0:
            print("You won")
            return 1
    return 1


def battle_system_spear_boss(player_hp: int, enemy_hp: int, enemy_name: str) -> int:
    """Turn based combat system."""
    sacred_water: int = 25
    player_hp += sacred_water
    print(f"[The Sacred Water has given you {sacred_water} more HP!]")
    while player_hp > 0 and enemy_hp > 0:
        enemy_hp -= spear_system(2)
        if enemy_hp < 0:
            enemy_hp = 0
        print(f"{enemy_name} has {enemy_hp} HP remaning.")
        player_hp -= enemy_system_boss(f"{enemy_name}")
        if player_hp < 0:
            player_hp = 0
        print(f"{player} has {player_hp} HP remaining.")
        if player_hp == 0:
            game_over(player_hp)
        if enemy_hp == 0:
            print("You won")
            return 1
    return 1


def battle_system_bow(player_hp: int, enemy_hp: int, enemy_name: str) -> int:
    """Turn based combat system."""
    while player_hp > 0 and enemy_hp > 0:
        enemy_hp -= bow_system(3)
        if enemy_hp < 0:
            enemy_hp = 0
        print(f"{enemy_name} has {enemy_hp} HP remaning.")
        player_hp -= enemy_system_one(f"{enemy_name}")
        if player_hp < 0:
            player_hp = 0
        print(f"{player} has {player_hp} HP remaining.")
        if player_hp == 0:
            game_over(player_hp)
        if enemy_hp == 0:
            print("You won")
            return 1    
    return 1


def battle_system_bow_two(player_hp: int, enemy_hp: int, enemy_name: str) -> int:
    """Turn based combat system."""
    while player_hp > 0 and enemy_hp > 0:
        enemy_hp -= bow_system(3)
        if enemy_hp < 0:
            enemy_hp = 0
        print(f"{enemy_name} has {enemy_hp} HP remaning.")
        player_hp -= enemy_system_two(f"{enemy_name}")
        if player_hp < 0:
            player_hp = 0
        print(f"{player} has {player_hp} HP remaining.")
        if player_hp == 0:
            game_over(player_hp)
        if enemy_hp == 0:
            print("You won")
            return 1    
    return 1


def battle_system_bow_boss(player_hp: int, enemy_hp: int, enemy_name: str) -> int:
    """Turn based combat system."""
    sacred_water: int = 25
    player_hp += sacred_water
    print(f"[The Sacred Water has given you {sacred_water} more HP!]")
    while player_hp > 0 and enemy_hp > 0:
        enemy_hp -= bow_system(3)
        if enemy_hp < 0:
            enemy_hp = 0
        print(f"{enemy_name} has {enemy_hp} HP remaning.")
        player_hp -= enemy_system_boss(f"{enemy_name}")
        if player_hp < 0:
            player_hp = 0
        print(f"{player} has {player_hp} HP remaining.")
        if player_hp == 0:
            game_over(player_hp)
        if enemy_hp == 0:
            print("You won")
            return 1    
    return 1


def battle_system_battle_axe(player_hp: int, enemy_hp: int, enemy_name: str) -> int:
    """Turn based combat system."""
    while player_hp > 0 and enemy_hp > 0:
        enemy_hp -= battle_axe_system(5)
        if enemy_hp < 0:
            enemy_hp = 0
        print(f"{enemy_name} has {enemy_hp} HP remaning.")
        player_hp -= enemy_system_one(f"{enemy_name}")
        if player_hp < 0:
            player_hp = 0
        print(f"{player} has {player_hp} HP remaining.")
        if player_hp == 0:
            game_over(player_hp)
        if enemy_hp == 0:
            print("You won")
            return 1    
    return 1


def battle_system_battle_axe_two(player_hp: int, enemy_hp: int, enemy_name: str) -> int:
    """Turn based combat system."""
    while player_hp > 0 and enemy_hp > 0:
        enemy_hp -= battle_axe_system(5)
        if enemy_hp < 0:
            enemy_hp = 0
        print(f"{enemy_name} has {enemy_hp} HP remaning.")
        player_hp -= enemy_system_two(f"{enemy_name}")
        if player_hp < 0:
            player_hp = 0
        print(f"{player} has {player_hp} HP remaining.")
        if player_hp == 0:
            game_over(player_hp)
        if enemy_hp == 0:
            print("You won")
            return 1 
    return 1


def battle_system_battle_axe_boss(player_hp: int, enemy_hp: int, enemy_name: str) -> int:
    """Turn based combat system."""
    sacred_water: int = 25
    player_hp += sacred_water
    print(f"[The Sacred Water has given you {sacred_water} more HP!]")
    while player_hp > 0 and enemy_hp > 0:
        enemy_hp -= battle_axe_system(5)
        if enemy_hp < 0:
            enemy_hp = 0
        print(f"{enemy_name} has {enemy_hp} HP remaning.")
        player_hp -= enemy_system_boss(f"{enemy_name}")
        if player_hp < 0:
            player_hp = 0
        print(f"{player} has {player_hp} HP remaining.")
        if player_hp == 0:
            game_over(player_hp)
        if enemy_hp == 0:
            print("You won")
            return 1    
    return 1


def main() -> None:
    """Game teakes place here."""
    global points
    global player 
    game_loop: bool = True
    greet()
    while game_loop:
        print("I sense multiple posibilities within you. They lay before thee, thy paths of fate.")
        print("You have three choices. You can turn around and return to your homeland, take the path of the senshi, take the path of the knight, or quit the game.")
        print(f"{player} has 4 options! Input 1 - 4 based on which choice you decide.")
        print("Warning. You can not choose another path later.")
        print("1 - Homeland Path")
        print("2 - Senshi Path")
        print("3 - Knight Path")
        print("4 - Quit")
        path_choice: str = input()
        if path_choice == "1":
            path_choice = "Homeland Path"
        if path_choice == "2":
            path_choice = "Senshi Path"
        if path_choice == "3":
            path_choice = "Knight Path"
        if path_choice == "4":
            path_choice = "Quit Path"
            game_loop = False
            print(f"[Adventure Points]: {points}")
        print(f"{player} has chosen the {path_choice}.")
        if path_choice == "Homeland Path":
            end_of_journey(path_choice)
        if path_choice == "Senshi Path":
            print("So you've chosen the Senshi Path. I sense you have a warrior's spirit. The journey will not be easy.")
            weapon_of_choice = weapon_selection("Senshi path")
            print("There are three major enemies you must face.")
            print("Two of the eneimes work directly under the overlord of terror.")
            print("The overlord of terror is currently in the castle.")
            print("Make your way through the kingdom taking down the two subordinates first. After you have taken them down, challenge the overlord of terror.")
            print("Remeber, when you are fighting your openents, just because their HP is 0 does not mean they won't go for one final attack.")
            print(f"Safe travels {player}.")
            print("[After departing from the old man you make your way through the kingdom with you new sacred weapon]")
            print("[After some time you come across a large man wearing a cloak.]")
            print("[Large man]: You must be one of the chumps they sent to take back the kingdom.")
            print("             Sadly, you'll end up like the rest of the people they sent.")
            print("             My name is Jack. I am renowned for my sword skills!!")
            print("[Jack]: Prepare to be sliced!]")
            print(f"[Battle 1: {player} VS. Jack the Dual Wielding Slasher]")
            if weapon_of_choice == 4:
                battle_system_katana(player_hp, 100, "Jack")
            if weapon_of_choice == 1:
                battle_system_sword(player_hp, 100, "Jack")
            if weapon_of_choice == 2:
                battle_system_spear(player_hp, 100, "Jack")
            if weapon_of_choice == 3:
                battle_system_bow(player_hp, 100, "Jack")
            if weapon_of_choice == 5:
                battle_system_battle_axe(player_hp, 100, "Jack")
            print("[Jack]: This can't be!! ")
            print("[Jack perishes and all that is left behind are the stolen Adventure Points]")
            points += 5
            print(f"{player} has gained 5 Adventure Points.")
            print(f"[Adventure Points]: {points}")
            print("After Jack's defeat you travel deaper towards the heart of the kingdom, defeating monsters and beasts along the way.")
            print("As you make your way towards the castle you find yourself in the ruins of a nearby town.")
            print("There are no signs of life anywhere.")
            print("In the center of the town there are no ruins, only an oddly shaped area that has been flattened.")
            print("In this area you can see a shadowy figue")
            print("[Shadowy figure]: I figured you would find your way here.")    
            print("                  In anticipation of your arrival, I went ahead and disposed of everyone in this town and cleared a space for our fight.")
            print(f"                  All of the monsters have reported back to me talking about you, {player}.")
            print("                  However, If you were strong enough to defeat Jack, then you really are no joke.")
            print("                  I am the legendary master of martial arts from the lands of darkness.")
            print("                  I once had a name but now I am only known as Title.")
            print(f"[Title]: It's over {player}!!")
            print(f"[Battle 2: {player} VS. Title the champion of martial arts")
            if weapon_of_choice == 4:
                battle_system_katana_two(player_hp, 100, "Title")
            if weapon_of_choice == 1:
                battle_system_sword_two(player_hp, 100, "Title")
            if weapon_of_choice == 2:
                battle_system_spear_two(player_hp, 100, "Title")
            if weapon_of_choice == 3:
                battle_system_bow_two(player_hp, 100, "Title")
            if weapon_of_choice == 5:
                battle_system_battle_axe_two(player_hp, 100, "Title")
            print("[Title]: I've faced many in my centuries of living in the lands of darkness...")
            print("         I have... never faced an oppenent like you.")
            print(f"         Here {player}, take this.")
            print("[Obtained Sacred Water]")
            print("[Title]: I found it in the castle but I have no idea what it does.")                    
            print("[Title perishes and all that is left behind are the stolen Adventure points.]")
            points += 10
            print(f"{player} has gained 10 Adventure Points.")
            print(f"[Adventure Points]: {points}")
            print("Title's defeat caused there to be a shift in the kingdom.")
            print("Some monsters and beasts began to withdraw from the kingdom and back to the lands of darkness.")
            print("Soon after, you began to feel closer to your sacred weapon.")
            print("You found your way to the castle defeating several strong monsters and beasts along the way.")
            print("Forcing your way into the castle you defeat any strong enmey that crosses your path and enter the throne room.")
            print("The man sitting in the throne is the one responsible for all of this carnage.")
            print("[You feel the malice eminating from him.]")
            print(f"[Man on the throne]: No matter how many I sent, they all fell before you, {player}.")
            print("                      You even defeated Jack and Title, my strongest commanders.")
            print(f"                      We could join forces. You and me, {player} and Akuma. We could rule this land together")
            print("[Akuma]: But I already know that isn't an option for you.")
            print("         I heard about your Sacred Weapon. Where I'm from nothing like that exists.")
            print("         However, I was able to find one of them, and my my they are stunning")
            print("[Akuma begins to stand, unsheathing a sword.]")
            print("[Akuma] At first this blade rejected me. However, after imbuing my own magic into this blade I made it my own.")
            print("        I guess the term 'Sacred Weapon' no longer fits this sword")
            print("        It's more fitting to call this sword cursed now. So I have named it Cursed Blade Yoru.")
            print("        You're about to find out how I was able to take over this kingdom!")
            print(f"[Final Battle: {player} VS. AKUMA the Overlord of Terror]")
            if weapon_of_choice == 4:
                battle_system_katana_boss(player_hp, 100, "AKUMA")
            if weapon_of_choice == 1:
                battle_system_sword_boss(player_hp, 100, "AKUMA")
            if weapon_of_choice == 2:
                battle_system_spear_boss(player_hp, 100, "AKUMA")
            if weapon_of_choice == 3:
                battle_system_bow_boss(player_hp, 100, "AKUMA")
            if weapon_of_choice == 5:
                battle_system_battle_axe_boss(player_hp, 100, "AKUMA")
            print("[Akuma]: NOOOOOOO!!")
            print("         This can't be happening.")
            print("         Don't think this is over...")                    
            print("[Akuma perishes and all that is left behind are the stolen Adventure Points.]")
            points += 15
            print(f"{player} has gained 15 Adventure Points.")
            final_scene(points, path_choice) 
        if path_choice == "Knight Path":
            print("So you've chosen the Knight Path. I sense you have a knight's spirit. The journey will not be easy.")
            weapon_of_choice = weapon_selection("Knight path")
            print("There are three major enemies you must face.")
            print("Two of the eneimes work directly under the overlord of terror.")
            print("The overlord of terror is currently in the castle.")
            print("Make your way through the kingdom taking down the two subordinates first. After you have taken them down, challenge the overlord of terror.")
            print("Remeber, when you are fighting your openents, just because their HP is 0 does not mean they won't go for one final attack.")
            print(f"Safe travels {player}.")
            print("[After departing from the old man you make your way through the kingdom with you new sacred weapon]")
            print("As you make your way towards the castle you find yourself in the ruins of a nearby town.")
            print("There are no signs of life anywhere.")
            print("In the center of the town there are no ruins, only an oddly shaped area that has been flattened.")
            print("In this area you can see a shadowy figue")
            print("[Shadowy figure]: I figured you would find your way here.")    
            print("                  In anticipation of your arrival, I went ahead and disposed of everyone in this town and cleared a space for our fight.")
            print(f"                  All of the monsters have reported back to me talking about you, {player}.")
            print("                  However, If you were strong enough to defeat those monsters, then you really are no joke.")
            print("                  I am the legendary master of martial arts from the lands of darkness.")
            print("                  I once had a name but now I am only known as Title.")
            print(f"[Title]: It's over {player}!!")
            print(f"[Battle 1: {player} VS. Title the champion of martial arts")
            if weapon_of_choice == 4:
                battle_system_katana_two(player_hp, 100, "Title")
            if weapon_of_choice == 1:
                battle_system_sword_two(player_hp, 100, "Title")
            if weapon_of_choice == 2:
                battle_system_spear_two(player_hp, 100, "Title")
            if weapon_of_choice == 3:
                battle_system_bow_two(player_hp, 100, "Title")
            if weapon_of_choice == 5:
                battle_system_battle_axe_two(player_hp, 100, "Title")
            print("[Title]: I've faced many in my centuries of living in the lands of darkness...")
            print("         I have... never faced an oppenent like you.")
            print("[Title perishes and all that is left behind are the stolen Adventure points.]")
            points += 5
            print(f"{player} has gained 5 Adventure Points.")
            print(f"[Adventure Points]: {points}")
            print("[After some time you come across a large man wearing a cloak.]")
            print("[Large man]: You must be one of the chumps they sent to take back the kingdom.")
            print("             Sadly, you'll end up like the rest of the people they sent.")
            print("             My name is Jack. I am renowned for my sword skills!!")
            print("[Jack]: Prepare to be sliced!]")
            print(f"[Battle 2: {player} VS. Jack the Dual Wielding Slasher]")
            if weapon_of_choice == 4:
                battle_system_katana(player_hp, 100, "Jack")
            if weapon_of_choice == 1:
                battle_system_sword(player_hp, 100, "Jack")
            if weapon_of_choice == 2:
                battle_system_spear(player_hp, 100, "Jack")
            if weapon_of_choice == 3:
                battle_system_bow(player_hp, 100, "Jack")
            if weapon_of_choice == 5:
                battle_system_battle_axe(player_hp, 100, "Jack")
            print("[Jack]: This can't be!! ")
            print("[Jack perishes and all that is left behind are the stolen Adventure Points]")
            points += 10
            print(f"{player} has gained 10 Adventure Points.")
            print(f"[Adventure Points]: {points}")
            print("[!!]")
            print("[There is also something else along with the adventure points!]")
            print("[Obtained Sacred Water]")
            print("[The effects are unknown for now.]")
            print("Jack's defeat caused there to be a shift in the kingdom.")
            print("Some monsters and beasts began to withdraw from the kingdom and back to the lands of darkness.")
            print("Soon after, you began to feel closer to your sacred weapon.")
            print("You found your way to the castle defeating several strong monsters and beasts along the way.")
            print("Forcing your way into the castle you defeat any strong enmey that crosses your path and enter the throne room.")
            print("The man sitting in the throne is the one responsible for all of this carnage.")
            print("[You feel the malice eminating from him.]")
            print(f"[Man on the throne]: No matter how many I sent, they all fell before you, {player}.")
            print("                      You even defeated Title and Jack, my strongest commanders.")
            print(f"                      We could join forces. You and me, {player} and Akuma. We could rule this land together")
            print("[Akuma]: But I already know that isn't an option for you.")
            print("         I heard about your Sacred Weapon. Where I'm from nothing like that exists.")
            print("         However, I was able to find one of them, and my my they are stunning")
            print("[Akuma begins to stand, unsheathing a sword.]")
            print("[Akuma] At first this blade rejected me. However, after imbuing my own magic into this blade I made it my own.")
            print("        I guess the term 'Sacred Weapon' no longer fits this sword")
            print("        It's more fitting to call this sword cursed now. So I have named it Cursed Blade Yoru.")
            print("        You're about to find out how I was able to take over this kingdom!")
            print(f"[Final Battle: {player} VS. AKUMA the Overlord of Terror]")
            if weapon_of_choice == 4:
                battle_system_katana_boss(player_hp, 100, "AKUMA")
            if weapon_of_choice == 1:
                battle_system_sword_boss(player_hp, 100, "AKUMA")
            if weapon_of_choice == 2:
                battle_system_spear_boss(player_hp, 100, "AKUMA")
            if weapon_of_choice == 3:
                battle_system_bow_boss(player_hp, 100, "AKUMA")
            if weapon_of_choice == 5:
                battle_system_battle_axe_boss(player_hp, 100, "AKUMA")
            print("[Akuma]: NOOOOOOO!!")
            print("         This can't be happening.")
            print("         Don't think this is over...")                    
            print("[Akuma perishes and all that is left behind are the stolen Adventure Points.]")
            points += 15
            print(f"{player} has gained 15 Adventure Points.")
            final_scene(points, path_choice)


if __name__ == "__main__":
    main()
