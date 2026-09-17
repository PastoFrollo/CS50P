import sys
import PIL


if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit()
if len(sys.argv) > 3:
    print("Too much command-line arguments")
    sys.exit()
for arg in sys.argv[1:]:
    if not arg.lower().endswith((".png", ".jpeg", ".jpg")):
        print(f"Invalid file type: {arg}")
        sys.exit()


try:
    shirt = PIL.Image.open("shirt.png")
    with PIL.Image.open(sys.argv[1]) as input:
        fitted_img = PIL.ImageOps.fit(input, (600, 600))
        fitted_img.paste(shirt, (0,0), shirt)
        fitted_img.save(sys.argv[2])

except FileNotFoundError:
    print(f"File not found: {sys.argv[1]}")
    sys.exit()