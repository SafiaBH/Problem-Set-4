import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    font = random.choice(fonts)

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    if sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    font = sys.argv[2]

else:
    sys.exit("Invalid usage")

text = input("Input: ")

figlet.setFont(font=font)

print("Output:")
print(figlet.renderText(text))
