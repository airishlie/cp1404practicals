"""
Hexadecimal Colour
"""
COLOUR_TO_HEXADECIMAL = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}


# Display instructions
print("Enter a colour name to get its hexadecimal code (e.g., AliceBlue).")
print("Enter a blank input to stop.")

max_length = max(len(colour) for colour in COLOUR_TO_HEXADECIMAL)
for colour, hex_code in COLOUR_TO_HEXADECIMAL.items() :
    print (f"{colour:<{max_length}} is {COLOUR_TO_HEXADECIMAL[colour]}")

colour_name = input("Enter color name: ")
while colour_name:
    try:
        print(f"The hex code for {colour_name} is {COLOUR_TO_HEXADECIMAL[colour_name]}")
    except KeyError:
        print("Invalid color name")
    colour_name = input("Enter color name: ")