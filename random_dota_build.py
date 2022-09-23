import random as rd
import sys

num_args = len(sys.argv)
mode = "1"
attribute = "all"

item_list = ["Orb of Corrosion", "Wraith Band", "Bracer", "Magic Wand", "Soul Ring", "Falcon Blade", "Null Talisman",  "Hand Of Midas",  "Helm Of The Overlord", "Mask Of Madness", "Moon Shard",  "Pipe Of Insight",  "Spirit Vessel", "Wraith Pact", "Holy Locket",  "Veil Of Discord", "Hurricane Pyke", "Glimmer Cape", "Solar Crest", "Gleipnir", "Aghanim's Scepter", "Wind Waker", "Revenant's Brooch", "Refresher Orb", "Scythe of Vyse", "Dagon", "Blade Mail", "Aeon Disk", "Eternal Shroud", "Lotus Orb", "Bloodstone", "Linken's Sphere", "Shyva's Guard", "Assault Cuirass", "Heart Of Terrasque", "Manta Style", "Black King Bar", "Crimson Guard", "Meteor Hammer", "Bloodthorn", "Divine Rapier", "Daedalus", "Silver Edge", "Abyssal Blade", "Radiance", "Butterfly", "Ethereal Blade", "Desolator", "Nullifier", "Monkey King Bar", "Battle Fury", "Armlet Of Mordiggian", "Echo Sabre", "Heaven's Haldberg", "Sange and Yasha", "Satanic", "Aghanim's Shard", "Mjollnir", "Overwhelming Blink", "Diffusal Blade", "Kaya and Sange", "Yasha and Kaya", "Eye of Skadi", "Arcane Blink", "Swift Blink"]

boots_list = ["Power Treads", "Phase Boots", "Boots Of Travel", "Arcane Boots", "Guardian Greaves", "Boots of Bearing", "Tranquil Boots"]

str_heroes_list = ["Abaddon", "Alchemist", "Axe", "Beastmaster", "Brewmaster", "Bristleback", "Centaur Warrunner", "Chaos Knight", "Clockwerk Dawnbreaker", "Doom", "Dragon Knight", "Earth Spirit", "Earthshaker", "Elder Titan", "Huskar", "Io", "Kunkka", "Legion Commander", "Lifestealer", "Lycan", "Magnus", "Marci", "Mars", "Night Stalker", "Omniknight", "Phoenix", "Primal Beast", "Pudge", "Sand King", "Slardar", "Snapfire", "Spirit Breaker", "Sven", "Tidehunter", "Timbersaw", "Tiny", "Treant Protector", "Tusk", "Underlord", "Undying", "Wraith King"]

agi_heroes_list = ['Anti-Mage', 'Arc Warden', 'Bloodseeker', 'Bounty Hunter', 'Broodmother', 'Clinkz', 'Drow Ranger', 'Ember Spirit', 'Faceless Void', 'Gyrocopter', 'Hoodwink', 'Juggernaut', 'Lone Druid', 'Luna', 'Medusa', 'Meepo', 'Mirana', 'Monkey King', 'Morphling', 'Naga Siren', 'Nyx Assassin', 'Pangolier', 'Phantom Assassin', 'Phantom Lancer', 'Razor', 'Riki', 'Shadow Fiend', 'Slark', 'Sniper', 'Spectre', 'Templar Assassin', 'Terrorblade', 'Troll Warlord', 'Ursa', 'Vengeful Spirit', 'Venomancer', 'Viper', 'Weaver']

int_heroes_list = ['Ancient Apparition', 'Bane', 'Batrider', 'Chen', 'Crystal Maiden', 'Dark Seer', 'Dark Willow', 'Dazzle', 'Death Prophet', 'Disruptor', 'Enchantress', 'Enigma', 'Grimstroke', 'Invoker', 'Jakiro', 'Keeper of the Light', 'Leshrac', 'Lich', 'Lina', 'Lion', 'Nature&#39;s Prophet', 'Necrophos', 'Ogre Magi', 'Oracle', 'Outworld Destroyer', 'Puck', 'Pugna', 'Queen of Pain', 'Rubick', 'Shadow Demon', 'Shadow Shaman', 'Silencer', 'Skywrath Mage', 'Storm Spirit', 'Techies', 'Tinker', 'Visage', 'Void Spirit', 'Warlock', 'Windranger', 'Winter Wyvern', 'Witch Doctor', 'Zeus']

all_heroes_list = [str_heroes_list, agi_heroes_list, int_heroes_list]

def print_usage():
    print("""    Usage: <name_of_script> <mode> <attribute>
    Mode 1: Generates a random build for a random hero.
    Mode 2: Generates a random build.
    Mode 3: Returns a random hero.

    If the attribute argument is present (str/agi/int) it will only choose a hero with the respective main attribute.

    If mode is not specified it is defaulted to 1.
    If attribute is not specified it chooses from all attribute heroes.
    """)

def return_hero(attr):
    if attr == "all":
        return rd.choice(rd.choice(all_heroes_list))
    elif attr == "str":
        return rd.choice(str_heroes_list)
    elif attr == "agi":
        return rd.choice(agi_heroes_list)
    elif attr == "int":
        return rd.choice(int_heroes_list)


if num_args == 1:
    pass
elif num_args == 2:
    if "str" in sys.argv:
        attribute = "str"
    elif "agi" in sys.argv:
        attribute = "agi"
    elif "int" in sys.argv:
        attribute = "int"
    else:
        if "1" in sys.argv or "2" in sys.argv or "3" in sys.argv:
            mode = sys.argv[1]
        else:
            print("Incorrect usage.")
            print_usage()
elif num_args == 3:
    if "str" in sys.argv:
        attribute = "str"
    elif "agi" in sys.argv:
        attribute = "agi"
    elif "int" in sys.argv:
        attribute = "int"
    else:
        print("Incorrect usage.")
        print_usage()
    if "1" in sys.argv:
        mode = "1"
    elif "2" in sys.argv:
        mode = "2"
    elif "3" in sys.argv:
        mode = "3"
    else:
        print("Incorrect usage.")
        print_usage()
else:
    print("Incorrect usage.")
    print_usage()

if mode == "1":
    print("Hero: " + return_hero(attribute))
    final_build = rd.choices(item_list, k=5)
    final_build.append(rd.choice(boots_list))
    print("Build: " + str(final_build))
elif mode == "2":
    final_build = rd.choices(item_list, k=5)
    final_build.append(rd.choice(boots_list))
    print("Build: " + str(final_build))
elif mode == "3":
    print("Hero: " + return_hero(attribute))
