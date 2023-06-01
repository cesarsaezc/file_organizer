from OrganizerFolder import OrganizerFolder
import os

if not __name__ == "__main__":
    exit()

extensions = {
    "Documents": ['.txt', '.doc', '.docx', '.docm', '.odt', '.pdf', '.rtf',
                  '.csv', '.xls', '.xlsx', '.xlsm', '.ods', '.pps', '.ppt',
                  '.ppsx', '.pptx', '.ppsm', '.pptm', '.potx', '.odp'],
    "Compressed": ['.zip', '.rar', '.rar5', '.7z', '.ace', '.r00, r01, etc',
                   '.gz', '.tar', '.bz2', '.iso'],
    "Music": ['.mp3', '.wma', '.wav', '.flac', '.midi', '.ogg', '.m3u', '.aac'],
    "Images": ['.jpeg', '.jpg', '.png', '.bmp', '.ico', '.svg', '.webp', '.gif',
               '.psd', '.heic', '.nef', '.crw', '.ai', '.id'],
    "Videos": ['.avi', '.divx', '.mov', '.mp4', '.mpg', '.mkv', '.wmv', '.wpl'],
    "Programs": ['.exe','.msi','.sh']
}
path_file = os.path.dirname(os.path.abspath(__file__))

def find_files(path:str,extensions:list) -> list:
    """
    Scrolls through the path folder and extract all the files
    matched by extension.
    """
    files = []
    for file in os.listdir(path):
        path_file = os.path.join(path,file)
        if not os.path.isfile(path_file):
            continue
        for ext in extensions:
            if not file.endswith(ext):
                continue
            files.append(file)
    return files

def get_path() -> str:
    """
    Ask to user for a path where organize files.
    """
    print("\nTo exit press CTRL+C")
    path = input("Enter the absolute path to the folder you want to organize: ")
    while not os.path.exists(path):
        print("\nError, path doesn't exists.")
        print("To exit press CTRL+C")
        path = input("Enter the absolute path to the folder you want to organize: ")
    return path

while True:
    path = get_path()

    # Search for files by extension and save them in OrganizerFolder instance
    organizer_folders = []
    print("Collecting files...")
    for type in extensions:
        files = find_files(path,extensions[type])
        if len(files) < 1:
            continue
        organizer_folder = OrganizerFolder(type,path,files)
        organizer_folders.append(organizer_folder)

    if not len(organizer_folders):
        print("No files found to organize.")
        continue

    # Iterate the OrganizerFolder instances and move encountered files
    for org in organizer_folders:
        org.create_folder()
        if not org.get_is_created():
            continue
        print("Moving files...")
        org.move_files()
        print(f"Moved {org.get_files_moved()} files of {len(org.get_files())}.")

    organizer_folders.clear()