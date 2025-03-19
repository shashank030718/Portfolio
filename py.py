from PIL import Image, ImageOps

# Load the uploaded image
image_path = "/mnt/data/shashank pick.jpg"
image = Image.open(image_path)

# Add a black background to the image
# Since it's not clear if "black background" means full replacement or border,
# I'll try adding a black background by creating a solid black canvas and pasting the image onto it.
black_background = Image.new("RGB", image.size, (0, 0, 0))
black_background.paste(image, (0, 0))

# Save the modified image
output_path = "/mnt/data/shashank_black_background.jpg"
black_background.save(output_path)
output_path
