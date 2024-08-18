import argparse
import save_pdf_to_images as P2I
import images_to_text as I2T

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Convert PDF to images and extract text.")
    parser.add_argument("pdf_path", type=str, help="Path to the PDF file to be processed.")
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Use the provided PDF path
    pdf_path = args.pdf_path

    P2I.create_destination_folder('Converted Images')

    P2I.pdf_to_images(pdf_path, 'Converted Images')

    I2T.image_to_text('Converted Images', 'Extracted Texts')


if __name__ == "__main__":
    main()
