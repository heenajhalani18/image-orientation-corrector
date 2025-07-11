IMAGE ORIENTATION CORRECTOR:-
This project automatically detects and corrects tilted or upside-down images and PDF files using OCR and image processing. It is ideal for scanned documents like KYC forms, identity proofs, and similar document-based inputs.

What It Does-
1. Detects the orientation of images using Tesseract OCR.
2. Corrects any rotation (e.g., 90°, 180°) to make the image upright.
3. Works with both image files (JPG, PNG) and PDF documents (1–2 pages).
4. Saves corrected versions to an output folder automatically.

Folder Structure-
orientation_corrector/
  1. input/              # Place your tilted PDFs or images here
  2. output/             # Corrected files will be saved here
  3. orientation_corrector.py
  4. README.md

Tools & Libraries Used-
1. Python 3.x
2. pdf2image – To convert PDF pages into images.
3. Pillow (PIL) – For image processing and rotation.
4. pytesseract – To detect image orientation using OCR.
5. fpdf – To create new PDFs from corrected images.
6. os – For handling files and folders.

How to Run-
1. Install dependencies
  pip install pillow pytesseract pdf2image fpdf
2. Ensure Tesseract and Poppler are installed
   macOS:
    brew install tesseract  
    brew install poppler

Run the code

Usage-
1. Place any tilted PDF or image in the input folder.
2. The script processes them and saves the corrected version in the output folder.

Example-
1. Input:
     1. input/kyc_form.pdf
     2. input/photo_upside_down.jpg
2. Output:
     1. output/kyc_form_corrected.pdf
     2. output/photo_upside_down_corrected.jpg

