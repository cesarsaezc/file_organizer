import os
import shutil

class OrganizerFolder:
    """
    References the folders where the files filtered by extension will be organized.
    """
    def __init__(self,name:str,base_path:str,files:list):
        self.name = name
        self.base_path = base_path
        self.files = files
        self.is_created = False
        self.files_moved = 0

    def create_folder(self):
        """
        Creates folder if it doesn't already exist.
        """
        try:
            os.mkdir(os.path.join(self.base_path,self.name))
        except FileExistsError:
            self.is_created = True
            return
        except Exception as e:
            print(f"Error creating folder, error name: {type(e).__name__}")
            return
        else:
            self.is_created = True
    
    def move_files(self):
        """
        Move files into the created Organizer folder.
        """
        if len(self.files) < 1:
            return
        
        for file in self.files:
            path_file = os.path.join(self.base_path,file)
            new_path_file = os.path.join(self.base_path,self.name,file)
            if os.path.exists(new_path_file):
                print(f"File {file} already exists in {self.name}.")
                continue
            try:
                shutil.move(path_file,new_path_file)
            except Exception as e:
                print(e)
                continue
            else:
                print(f"{file} moved to {self.name} folder.")
                self.files_moved += 1


    def get_base_path(self):
        return self.base_path
    
    def get_files(self):
        return self.files

    def get_is_created(self):
        return self.is_created
    
    def get_files_moved(self):
        return self.files_moved