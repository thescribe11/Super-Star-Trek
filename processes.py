def photons(torpedoes: int, sector: list, klingons: int, ent_pos: list, galaxy: list):
    try:
        fire_number = int(input("\n[*ARMORY*] How many torpedoes would you like to fire?\n>"))
    except:
        print("[*ARMORY*] Sir, can you please speak more clearly? I cannot understand what you are saying.")
    if fire_number > 3:
        print("[*ARMORY*] I'm sorry sir, but firing that many would melt the tubes!")
        fire_anyway = input("Would you like to fire anyway?\n>")
        if fire_anyway == "Y" or fire_anyway == "y" or fire_anyway == "yes" or fire_anyway == "Yes":
            launch_torps(fire_number, sector, torpedoes, klingons, ent_pos, galaxy)

