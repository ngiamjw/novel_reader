import os

# Specify the path of the new folder
def folder_maker(name):
    folder_path = f"./{name}"

    # Create the new folder
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

def file_maker(number, folder_path):
    file_name = f"chapter-{number}.txt"
    file_path = os.path.join(folder_path, file_name)
    return file_path