import os
from PIL import Image

# Define paths
input_folder = 'input_images'
output_folder = 'output_images'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Desired size
new_width = 800
new_height = 600

# Loop through all files in input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Open and resize the image
        with Image.open(input_path) as img:
            resized_img = img.resize((new_width, new_height))
            resized_img.save(output_path)
            print(f"Resized and saved: {output_path}")

print("All images resized successfully!")