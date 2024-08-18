import save_pdf_to_images as P2I
from pathlib import Path
from PIL import Image
import pytesseract

def image_to_text(image_directory_path, text_directory_path):
    # Replace with your path
    directory = image_directory_path
    P2I.create_destination_folder(text_directory_path)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    files = Path(directory).glob('*.jpg')
    counter = 0
    for file in files:
        extracted_text = pytesseract.image_to_string(Image.open(file))
        print(str(file) + " extraction done.")
        
        with Path(text_directory_path + rf"\extracted_text{counter}.txt").open('w') as file:
            file.write(extracted_text)
        print(str(file) + " extraction saved.")
        counter += 1
        
        