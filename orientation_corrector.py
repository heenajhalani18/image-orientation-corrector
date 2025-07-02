import os
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from fpdf import FPDF

# ========== CONFIGURATION ==========
INPUT_DIR = "input"
OUTPUT_DIR = "output"
TESSERACT_PATH = "/opt/homebrew/bin/tesseract"  # May vary based on install
POPPLER_PATH = "/opt/homebrew/bin"              # May vary on macOS
# ====================================

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def correct_image_orientation(image):
    try:
        osd = pytesseract.image_to_osd(image)
        rotation = int([line for line in osd.split('\n') if 'Rotate' in line][0].split(":")[1].strip())
        if rotation != 0:
            corrected = image.rotate(-rotation, expand=True)
            return corrected
        else:
            return image
    except Exception as e:
        print(f"Error detecting orientation: {e}")
        return image

def process_image_file(file_path, output_path):
    img = Image.open(file_path)
    corrected = correct_image_orientation(img)
    # Convert RGBA to RGB if needed
    if corrected.mode == 'RGBA':
        corrected = corrected.convert('RGB')

    corrected.save(output_path)

    print(f"Processed image saved to {output_path}")

def process_pdf_file(pdf_path, output_path):
    pages = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
    corrected_images = []
    
    for i, page in enumerate(pages):
        print(f"Processing page {i+1}")
        corrected_img = correct_image_orientation(page)
        corrected_images.append(corrected_img)

    # Save corrected images as a single PDF
    pdf = FPDF()
    for img in corrected_images:
        img_path = os.path.join(OUTPUT_DIR, "temp.jpg")
        img.save(img_path)
        pdf.add_page()
        pdf.image(img_path, x=0, y=0, w=210, h=297)  # A4 size

    pdf.output(output_path, "F")
    print(f"Corrected PDF saved to {output_path}")
    os.remove(img_path)

def main():
    for file_name in os.listdir(INPUT_DIR):
        file_path = os.path.join(INPUT_DIR, file_name)
        output_file = os.path.splitext(file_name)[0] + "_corrected.pdf"
        output_path = os.path.join(OUTPUT_DIR, output_file)

        if file_name.lower().endswith(".pdf"):
            process_pdf_file(file_path, output_path)
        elif file_name.lower().endswith((".png", ".jpg", ".jpeg")):
            output_image = os.path.splitext(file_name)[0] + "_corrected.jpg"
            process_image_file(file_path, os.path.join(OUTPUT_DIR, output_image))
        else:
            print(f"Unsupported file format: {file_name}")

if __name__ == "__main__":
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    main()
