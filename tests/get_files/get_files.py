import os
from typing import List

def get_files_name_by_path(files_path: str) -> List[str]:

    filesname = []

    for directory, sub_directories, files in os.walk(files_path):
        
        #file_downloaded_name = os.path.basename(files)
        #filesname = files

        #return filesname

        return files

filenames = get_files_name_by_path(
    files_path='tests'
)

print(filenames)