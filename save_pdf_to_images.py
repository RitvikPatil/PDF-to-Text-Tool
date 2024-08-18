from pathlib import Path
from pdf2image import convert_from_path

#------------- CREATE A FOLDER TO SAVE IMAGES -------------
def create_destination_folder(name):
    folder_name = Path(name)

    # Check if the folder already exists
    if not folder_name.exists():
        folder_name.mkdir(parents=True, exist_ok=True)
        print(f"Folder '{folder_name}' created.")
    else:
        print(f"Folder '{folder_name}' already exists.")


#------------- CONVERT PDF TO IMAGES -------------
#------------- AND SAVE THEM -------------

def pdf_to_images(pdf_path, image_folder_path):
    # Define the specific path where you want to save the images
    save_directory = Path(image_folder_path)

    # Ensure the directory exists
    save_directory.mkdir(parents=True, exist_ok=True)

    images = convert_from_path(pdf_path, 200, poppler_path=r'C:\Program Files\poppler-24.07.0\Library\bin')
    for i in range(len(images)):
        file_path = save_directory / ('page' + str(i) + '.jpg')
        if file_path.exists() == False:
            images[i].save(file_path, 'JPEG') 