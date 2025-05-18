from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
figlet_list = figlet.getFonts()


if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet_list))

elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font":
    figlet.setFont(font=sys.argv[2])

else:
    sys.exit("Invalid usage")

txt = input("Input: ")
print(figlet.renderText(txt))
