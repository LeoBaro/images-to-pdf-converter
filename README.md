# Images to PDF Converter

A Python command-line tool that converts multiple images into a single PDF document. Perfect for creating PDFs from scanned documents, photos, or any collection of images.

## Features

- **Batch Processing**: Convert multiple images at once
- **Quality Control**: Adjustable output quality (1-100%)
- **Multiple Formats**: Supports JPG, JPEG, and PNG files
- **Automatic Sorting**: Images are processed in alphabetical order
- **Memory Efficient**: Processes images one by one to handle large collections
- **Clean Output**: Automatically removes temporary files

## Requirements

- Python 3.6+
- PIL (Pillow)
- PyPDF2

## Installation

1. **Clone or download** this repository
2. **Install dependencies**:
   ```bash
   pip install Pillow PyPDF2
   ```
   
   Or if you prefer using the virtual environment:
   ```bash
   # Activate virtual environment
   source env/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

Convert all images in a folder to a single PDF:

```bash
python main.py -f /path/to/images/folder
```

### Advanced Usage

```bash
python main.py -f /path/to/images/folder -q 80 -o my_document.pdf
```

### Command Line Arguments

- `-f, --folder`: **Required**. Path to the folder containing images
- `-q, --quality`: **Optional**. Output quality (1-100), default is 100
- `-o, --output`: **Optional**. Output PDF filename, default is "output.pdf"

### Examples

1. **Convert scanned documents**:
   ```bash
   python main.py -f ./data/mappe -o scanned_documents.pdf
   ```

2. **Create a low-quality preview** (faster processing, smaller file):
   ```bash
   python main.py -f ./data/mappe_2 -q 50 -o preview.pdf
   ```

3. **High-quality archive**:
   ```bash
   python main.py -f ./data/mappe -q 100 -o archive.pdf
   ```

## How It Works

1. **Scan Directory**: The tool scans the specified folder for supported image files
2. **Convert Images**: Each image is converted to a temporary PDF with the specified quality
3. **Merge PDFs**: All temporary PDFs are merged into a single output file
4. **Cleanup**: Temporary files are automatically removed

## Supported Image Formats

- `.jpg` / `.jpeg`
- `.png`

## File Naming Convention

Images are processed in **alphabetical order** based on their filenames. For best results, use numbered filenames like:
- `001.jpg`, `002.jpg`, `003.jpg`
- `page1.png`, `page2.png`, `page3.png`
- `scan_001.jpeg`, `scan_002.jpeg`

## Output Quality

- **100%**: Original image resolution (largest file size)
- **50%**: Half resolution (balanced quality/size)
- **25%**: Quarter resolution (smallest file size, fastest processing)

## Tips for Best Results

1. **Use consistent image formats** within a folder
2. **Number your files sequentially** for proper page ordering
3. **Consider quality vs. file size** - 80-90% quality often provides good balance
4. **Ensure images are oriented correctly** before conversion

## Troubleshooting

**"No image files found"**: Make sure your folder contains `.jpg`, `.jpeg`, or `.png` files

**"Provided folder does not exist"**: Check the folder path is correct and accessible

**Large file sizes**: Reduce quality setting (e.g., `-q 70`)

**Memory issues**: Process smaller batches of images or reduce quality

## Example Workflow

1. **Scan documents** or collect images in a folder
2. **Rename files** sequentially (001.jpg, 002.jpg, etc.)
3. **Run conversion**:
   ```bash
   python main.py -f ./scanned_docs -o final_document.pdf
   ```
4. **Check output** PDF for correct page order and quality

## License

This tool is provided as-is for personal and educational use.
