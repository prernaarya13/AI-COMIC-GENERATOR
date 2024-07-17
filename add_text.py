from PIL import Image, ImageDraw, ImageFont
import os

def add_text_to_panel(text, panel_image):
    # Check if panel_image is a path or an image object
    if isinstance(panel_image, str):
        if not os.path.exists(panel_image):
            # Create a placeholder image if the file doesn't exist
            panel_image = Image.new('RGB', (1024, 1024), color='lightgray')
            draw = ImageDraw.Draw(panel_image)
            draw.text((512, 512), "Panel Image Missing", fill='black', anchor='mm')
        else:
            panel_image = Image.open(panel_image)
    elif not isinstance(panel_image, Image.Image):
        raise TypeError("panel_image should be a string path or an image object")

    text_image = generate_text_image(text)

    result_image = Image.new('RGB', (panel_image.width, panel_image.height + text_image.height))

    result_image.paste(panel_image, (0, 0))
    result_image.paste(text_image, (0, panel_image.height))

    return result_image

def generate_text_image(text):
    # Define image dimensions
    width = 1024
    height = 128

    # Create a white background image
    image = Image.new('RGB', (width, height), color='white')

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Choose a font (Pillow's default font)
    font = ImageFont.truetype(font="manga-temple.ttf", size=30)

    # Calculate text size
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Calculate the position to center the text horizontally and vertically
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Define text color (black in this example)
    text_color = (0, 0, 0)

    # Add text to the image
    draw.text((x, y), text, fill=text_color, font=font)

    return image

# Example usage
text = """
Vincent: I think we need a new product.
Adrien: Let's brainstorm some ideas.
"""
panel_image_path = "D:\\comic generator\\panel1.png"
result_image = add_text_to_panel(text, panel_image_path)

# Save the image with PIL
result_image.save('D:\\comic generator\\panel1-text.png')
