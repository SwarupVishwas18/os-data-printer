# Create the System Data Displayer

from colorama import Fore
import normal, func

while True:
    normal.printBrand("System Data Displayer")
    ch = normal.myMenu(["Show Battery Status","Show Disk Status","Show Other Data","About Me","Exit"])

    if ch == 1:
        func.displayBattery()
    elif ch == 2:
        func.displayDisk()
    elif ch == 3:
        func.displayOther()
    elif ch == 4:
        normal.aboutMe()
    elif ch == 5:
        normal.quitMe()