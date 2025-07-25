# Image-Resizer-Tool
# Image Resizer Tool

A simple Python tool to resize and convert images in batch using the Pillow library.

##  Objective
- Resize and convert all images in a folder.
- Automate repetitive image editing tasks.

---

##  Tools & Libraries Used
- Python
- Pillow (PIL)
- OS Module (for file handling)

---

##  Folder Structure

image-resizer-tool/ │ ├── input_images/       # Folder containing original images ├── output_images/      # Folder where resized images are saved └── image_resizer.py    # Python script

---

##  How to Run the Project

### 1. Install Required Library

Make sure Pillow is installed:

```bash
pip install pillow


---

2. Add Images

Place the images you want to resize in the input_images/ folder.



---

3. Run the Script

python image_resizer.py

Resized images will be saved in the output_images/ folder.



---

# How It Works

1. Reads all image files from input_images/ folder.


2. Resizes each image to a defined size (default: 800x600).


3. Saves the resized image in output_images/.




---

# Key Concepts Used

File Handling: Reading from and writing to folders using the os module.

Image Processing: Using PIL.Image to resize and save images.



---

# Customization

You can change image size in image_resizer.py:

new_width = 800
new_height = 600


---

# Outcome

Automate repetitive image resizing tasks easily.

Learn file handling and image processing in Python.
