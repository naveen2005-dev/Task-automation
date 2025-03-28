import os

import shutil

Define file extensions and their corresponding folders

FILE_CATEGORIES = {

"Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],

"Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],

"Audio": [".mp3", ".wav", ".aac"],

"Videos": [".mp4", ".avi", ".mkv", ".mov"],

"Archives": [".zip", ".rar", ".tar", ".gz"],

"Others": []

}

def organize_files(directory):

if not os.path.exists(directory):

    print("Directory does not exist!")

    return



for file in os.listdir(directory):

    file_path = os.path.join(directory, file)

    if os.path.isfile(file_path):

        file_ext = os.path.splitext(file)[1].lower()

        moved = False

        

        for category, extensions in FILE_CATEGORIES.items():

            if file_ext in extensions:

                category_path = os.path.join(directory, category)

                if not os.path.exists(category_path):

                    os.makedirs(category_path)

                shutil.move(file_path, os.path.join(category_path, file))

                moved = True

                break

        

        if not moved:  # If the file extension doesn't match any category

            other_path = os.path.join(directory, "Others")

            if not os.path.exists(other_path):

                os.makedirs(other_path)

            shutil.move(file_path, os.path.join(other_path, file))

if name == "main":

folder_path = input("Enter the directory to organize: ")

organize_files(folder_path)

print("Files organized successfully!")  give me acorrect output
