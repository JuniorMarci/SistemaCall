def generate_captcha():

    from PIL import Image, ImageDraw, ImageFont
    import random

    # Create a blank image
    image_width = 500
    image_height = 200
    image_background_color = (255, 255, 255)  # white
    image = Image.new('RGB', (image_width, image_height), image_background_color)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Set the font and font size
    font = ImageFont.truetype('BRADHITC.TTF', 50)

    # Generate a random string of 6 letters and numbers
    random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))

    # Specify the text and its position
    text = random_string
    text_color = (0, 0, 0)  # black
    text_position = (100, 100)

    # Draw the text
    draw.text(text_position, text, fill=text_color, font=font, rotate=90)

    image = image.rotate(random.randrange(-70,71), expand=True)

    # Save the image to a file
    #image.save("output.png")
    image.save("./Portable Python-3.10.5 x64/p1/p1/static/output.png")

    #image = text

    return image,text