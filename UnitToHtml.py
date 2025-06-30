import json
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Err!! Please enter a unit.json file to configure the datasheet")
        quit(1)

    with open(sys.argv[1], "r") as file:
        specifications = json.loads(file.read())
        file.close()
    
    with open("./Template/template.html", "r") as file:
        template = file.read()
        file.close()
    
    template = template.replace("<SQUADNAME>", specifications["SQUADNAME"]);
    template = template.replace("<MOVE>", specifications["MOVE"]);
    template = template.replace("<TOUGHNESS>", specifications["TOUGHNESS"]);
    template = template.replace("<SAVE>", specifications["SAVE"]);
    template = template.replace("<WOUNDS>", specifications["WOUNDS"]);
    template = template.replace("<LEADERSHIP>", specifications["LEADERSHIP"]);
    template = template.replace("<OBJECTIVECONTROL>", specifications["OBJECTIVECONTROL"]);

    # Ranged Weapons
    weapon_buffer = ""
    for weapon in specifications["RANGEDWEAPONS"]:
        with open("./Template/weapon.html", "r") as file:
            weapon_template = file.read()
            weapon_template = weapon_template.replace("<WEAPONNAME>", weapon["WEAPONNAME"])
            weapon_template = weapon_template.replace("<RANGE>", weapon["RANGE"])
            weapon_template = weapon_template.replace("<ATTACKS>", weapon["ATTACKS"])
            weapon_template = weapon_template.replace("<SKILL>", weapon["SKILL"])
            weapon_template = weapon_template.replace("<STRENGTH>", weapon["STRENGTH"])
            weapon_template = weapon_template.replace("<ARMORPIERCING>", weapon["ARMORPIERCING"])
            weapon_template = weapon_template.replace("<DAMAGE>", weapon["DAMAGE"])
            weapon_buffer += weapon_template
            file.close()
    template = template.replace("<RANGEDWEAPONS>", weapon_buffer)
    
    # Melee Weapons
    weapon_buffer = ""
    for weapon in specifications["MELEEWEAPONS"]:
        with open("./Template/weapon.html", "r") as file:
            weapon_template = file.read()
            weapon_template = weapon_template.replace("<WEAPONNAME>", weapon["WEAPONNAME"])
            weapon_template = weapon_template.replace("<RANGE>", weapon["RANGE"])
            weapon_template = weapon_template.replace("<ATTACKS>", weapon["ATTACKS"])
            weapon_template = weapon_template.replace("<SKILL>", weapon["SKILL"])
            weapon_template = weapon_template.replace("<STRENGTH>", weapon["STRENGTH"])
            weapon_template = weapon_template.replace("<ARMORPIERCING>", weapon["ARMORPIERCING"])
            weapon_template = weapon_template.replace("<DAMAGE>", weapon["DAMAGE"])
            weapon_buffer += weapon_template
            file.close()

    template = template.replace("<MELEEWEAPONS>", weapon_buffer)



    template = template.replace("<FACTION>", specifications["FACTION"]);

    # Abilities
    ability_buffer = ""
    for ability in specifications["ABILITIES"]:
        with open("./Template/ability.html", "r") as file:
            ability_template = file.read()
            ability_template = ability_template.replace("<ABILITYNAME>", ability["ABILITYNAME"])
            ability_template = ability_template.replace("<ABILITYTEXT>", ability["ABILITYTEXT"])
            ability_buffer += ability_template
            file.close()
    
    template = template.replace("<ABILITIES>", ability_buffer)

    # War Gear
    wargear_buffer = ""
    for option in specifications["WARGEAR"]["WARGEAROPTION"]:
        with open("./Template/wargear.html", "r") as file:
            wargear_template = file.read()
            wargear_template = wargear_template.replace("<WARGEAROPTION>", option)
            file.close()
        
        wargear_buffer += wargear_template
    
    template = template.replace("<WARGEAR>", wargear_buffer)

    # Unit Composition
    unitcomp_buffer = ""
    for option in specifications["UNITCOMPOSITION"]["COMPOSITION"]:
        with open("./Template/unitcomposition.html", "r") as file:
            unitcomp_template = file.read()
            unitcomp_template = unitcomp_template.replace("<UNITCOMPOSITION>", option)
            file.close()
        
        unitcomp_buffer += wargear_template
    
    template = template.replace("<UNITCOMPOSITION>", unitcomp_buffer)


    template = template.replace("<EQUIPMENT>", specifications["EQUIPMENT"]);


    # Keywords
    keyword_buffer = ""
    for option in specifications["KEYWORDS"]:
        keyword_buffer += option + ", "
    keyword_buffer = keyword_buffer[:-2]

    template = template.replace("<KEYWORDS>", keyword_buffer);

    template = template.replace("<FACTIONKEYWORD>", specifications["FACTIONKEYWORD"]);

    filename = sys.argv[1].split(".")[0]
    with open(filename + ".html", "w+") as file:
        file.write(template)
        file.close()