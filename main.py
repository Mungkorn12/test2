from PIL import Image, ImageDraw, ImageFont
import numpy as np

# ASCII characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def generate_image():
    # Create an image with white background
    width, height = 200, 200
    image = Image.new('RGB', (width, height), color='white')

    # Draw a pattern and some text on the image
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    # Draw some shapes
    draw.ellipse([20, 20, 180, 180], outline="black")
    draw.line((20, 100, 180, 100), fill="black", width=2)
    draw.line((100, 20, 100, 180), fill="black", width=2)

    # Add text
    text = "ASCII ART"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (width - text_width) / 2
    text_y = height - text_height - 10
    draw.text((text_x, text_y), text, font=font, fill='black')

    # Save the image
    image_path = "Image.jpg" # Path to save the image 
    image.save(image_path)
    return image_path

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65  # Adjust ratio for better aspect
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = np.array(image)
    ascii_str = ""
    for pixel in pixels:
        for value in pixel:
            ascii_str += ASCII_CHARS[value // 25]
        ascii_str += "\n"
    return ascii_str

def main(image_path, output_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = resize_image(image, output_width)
    image = grayify(image)

    ascii_art = pixels_to_ascii(image)
    print(ascii_art)

    # Save to a text file
    with open("ascii_art.txt", "w") as f:
        f.write(ascii_art)

# Generate the image
image_path = generate_image()

# Run the ASCII art generator
main(image_path)


