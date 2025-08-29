import os
import sys
import argparse
from PIL import Image
from PyPDF2 import PdfMerger

def get_image_files(folder):
    supported_formats = ('.jpg', '.jpeg', '.png')
    return [os.path.join(folder, f) for f in os.listdir(folder)
            if f.lower().endswith(supported_formats)]

def convert_image_to_pdf(image_path, quality):
    img = Image.open(image_path)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    # Resize based on quality
    width, height = img.size
    scale = quality / 100.0
    new_size = (int(width * scale), int(height * scale))
    img = img.resize(new_size)

    temp_path = f"{image_path}.temp.pdf"
    img.save(temp_path, "PDF", resolution=100.0)
    return temp_path

def combine_pdfs(pdf_files, output_file):
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write(output_file)
    merger.close()

def main():
    parser = argparse.ArgumentParser(description="Convert images to a single PDF.")
    parser.add_argument("-f", "--folder", type=str, required=True, help="Folder containing images")
    parser.add_argument("-q", "--quality", type=int, default=100,
                        help="Output quality (1-100), default is 100")
    parser.add_argument("-o", "--output", default="output.pdf", help="Output PDF filename")
    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print("Error: Provided folder does not exist.")
        sys.exit(1)

    image_files = get_image_files(args.folder)
    if not image_files:
        print("No image files found in the folder.")
        sys.exit(1)

    print(f"Converting {len(image_files)} images at {args.quality}% quality...")
    temp_pdfs = []
    for img_file in sorted(image_files):
        temp_pdf = convert_image_to_pdf(img_file, args.quality)
        temp_pdfs.append(temp_pdf)

    print("Merging into a single PDF...")
    combine_pdfs(temp_pdfs, args.output)

    print(f"Saved to {args.output}. Cleaning up temporary files...")
    for temp_pdf in temp_pdfs:
        os.remove(temp_pdf)

    print("Done.")

if __name__ == "__main__":
    main()
