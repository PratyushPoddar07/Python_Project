from PIL import Image, ImageDraw, ImageFont

# create function to convert text to handwritten img
def text_to_handwriting(text, out_img):
    # create bgd img with dimension(800x400)
    img = Image.new('RGB', (1920, 1080), color="white")
    draw = ImageDraw.Draw(img)

    # Use a raw string to avoid escape character issues
    font_path = r"C:\Users\shuva\Desktop\Python_Project\textToHandwritten\Homemade_Apple\text.ttf"
    
    try:
        # get the font
        font = ImageFont.truetype(font_path, 35)
    except IOError:
        print("Font file not found or is not a valid TTF font.")
        return

    # draw text on img
    draw.text((50, 100), text, font=font, fill=(0, 0, 0))  # text color -> black

    # save the img
    img.save(out_img)
    print(f"Image saved as {out_img}")

text = input("Enter the text: ")
text_to_handwriting(text, "T2H.png")
