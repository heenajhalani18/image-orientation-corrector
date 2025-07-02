IMAGE ORIENTATION CORRECTOR:-
This project automatically detects and corrects tilted or upside-down images and PDF files using OCR and image processing. It is ideal for scanned documents like KYC forms, identity proofs, and similar document-based inputs.

What It Does-
1. Detects the orientation of images using Tesseract OCR.
2. Corrects any rotation (e.g., 90°, 180°) to make the image upright.
3. Works with both image files (JPG, PNG) and PDF documents (1–2 pages).
4. Saves corrected versions to an output folder automatically.

Folder Structure-
orientation_corrector/
├── input/              # Place your tilted PDFs or images here
├── output/             # Corrected files will be saved here
├── orientation_corrector.py
└── README.md

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
-Place any tilted PDF or image in the input folder.
-The script processes them and saves the corrected version in the output folder.

Example-
Input:
  input/kyc_form.pdf
  input/photo_upside_down.jpg
Output:
  output/kyc_form_corrected.pdf
  output/photo_upside_down_corrected.jpg

