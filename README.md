Image Resizer – Developer Version (CLI Tool)

A powerful batch image processing tool built using Python and Pillow, designed for developers who need automation for resizing, scaling, and converting images in bulk.

This project supports CLI commands, format conversion, percentage-based resizing, skips already processed files, and logs all actions for easy tracking.

🚀 Features

🔧 Resize images by width & height

📏 Resize by percentage (--scale)

🔄 Convert between formats (JPG, PNG, WEBP, JPEG)

⏭️ Skip already processed images

📝 Logging system (log.txt)

📂 Batch processing support

📁 Auto-creates output folder

🖥️ Works perfectly on Windows, Mac, and Linux

📦 Tech Stack

Python

Pillow (PIL)

argparse

OS module

📁 Project Structure
image_resizer/
│
├── input_images/        # Add images here
├── output_images/       # Processed images saved here
├── image_resizer.py     # CLI script
└── README.md

🔧 Installation
1️⃣ Install Python dependencies
pip install pillow

2️⃣ Add your source images

Place all images inside:

input_images/

🛠 How to Use (CLI Commands)

Run the script using PowerShell, Command Prompt, or Terminal:

1️⃣ Resize Using Width & Height
python image_resizer.py --width 800 --height 600


Resizes all images to 800×600 px.

2️⃣ Resize Using Percentage (Scale)
python image_resizer.py --scale 50


Makes image 50% smaller.

3️⃣ Convert Format Only
python image_resizer.py --format png


Converts all images to PNG format.

4️⃣ Resize + Convert Format
python image_resizer.py --width 500 --height 500 --format webp

📄 Logging

The script automatically generates a file:

log.txt


It records:

Processed: photo1.jpg -> photo1.webp
Skipped (already processed): image2.jpg
Error processing: corrupted.png

✔️ Output

All resized/converted images will be saved inside:

output_images/
🎯 Why This Project Is Useful

Automates repetitive image tasks

Converts large batches of images with one command

Helps web developers compress & optimize images

Ideal for photographers, designers, and software developers
