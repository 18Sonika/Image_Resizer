import os
import argparse
from PIL import Image

input_folder = "input_images"
output_folder = "output_images"
log_file = "log.txt"

SUPPORTED = (".png", ".jpg", ".jpeg", ".webp")

# ---------------------------------------------------------
# LOGGING FUNCTION
# ---------------------------------------------------------
def write_log(message):
    with open(log_file, "a", encoding="utf-8", errors="ignore") as f:
        f.write(message + "\n")
    print(message)


# ---------------------------------------------------------
# MAIN IMAGE PROCESSING FUNCTION
# ---------------------------------------------------------
def process_images(width=None, height=None, scale=None, output_format=None):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if not filename.lower().endswith(SUPPORTED):
            write_log(f"Skipped non-image file: {filename}")
            continue

        input_path = os.path.join(input_folder, filename)

        # Create output file name
        base_name = os.path.splitext(filename)[0]

        ext = output_format.lower() if output_format else os.path.splitext(filename)[1][1:]
        output_name = f"{base_name}.{ext}"
        output_path = os.path.join(output_folder, output_name)

        # Skip if already processed
        if os.path.exists(output_path):
            write_log(f"Skipped (already processed): {output_name}")
            continue

        try:
            img = Image.open(input_path)

            # Scaling (percentage)
            if scale:
                new_w = int(img.width * (scale / 100))
                new_h = int(img.height * (scale / 100))
                img = img.resize((new_w, new_h))

            # Width + Height resize
            elif width and height:
                img = img.resize((width, height))

            # Output format conversion
            save_format = output_format.upper() if output_format else img.format

            # Save image
            img.save(output_path, save_format)
            write_log(f"Processed: {filename} -> {output_name}")

        except Exception as e:
            write_log(f"Error processing {filename}: {e}")


# ---------------------------------------------------------
# COMMAND-LINE INTERFACE
# ---------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch image resizer & converter tool")

    parser.add_argument("--width", type=int, help="Target width")
    parser.add_argument("--height", type=int, help="Target height")
    parser.add_argument("--scale", type=int, help="Resize by percentage (e.g., 50 for 50%)")
    parser.add_argument("--format", type=str, help="Output image format (jpg, png, webp)")

    args = parser.parse_args()

    process_images(
        width=args.width,
        height=args.height,
        scale=args.scale,
        output_format=args.format
    )

    write_log("\n[OK] All images processed successfully!")
