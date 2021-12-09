# importing os and shutil module  
import os, shutil, time
from pathlib import Path
from datetime import datetime
from extensions import extension_paths



def add_cdate_to_path(child, path: Path):
    """
    Helper function that adds current month and year to destination path.
    """
    date = datetime.strptime(time.ctime(os.path.getctime(child)), "%a %b %d %H:%M:%S %Y")
    dated_path = path / f'{date.strftime("%b")} {date.year}'
    dated_path.mkdir(parents=True, exist_ok=True)
    return dated_path



def organize_by_type(source, destination):
    """
    Main function that moves the files from the source directory to a desired destination directory based on file type
    For loop only check for files and not directories and if the file extension is supported
    Open extensions.py to view all supported file extensions and its parent directories

    pathlib doc: https://docs.python.org/3/library/pathlib.html
    """
    source_path = Path(source)
    destination_path = Path(destination)
    destination_root = Path(destination)
    for child in source_path.iterdir():
        if child.is_file() and child.suffix.lower() in extension_paths:
            destination_path = destination_root / extension_paths[child.suffix.lower()]
            destination_path = add_cdate_to_path(child, path=destination_path)
            shutil.move(src=child, dst=destination_path)
            print(f'{child.name} has successfully been moved to {destination_path}')



def organize_by_keyword(source, destination, keywords):
    """
    Main function that moves the files from the source directory to a desired destination directory based on keywords entered
    For loop only check for files and not directories then checks if the keywords exists in the file name
    """
    source_path = Path(source)
    destination_path = Path(destination)
    destination_root = Path(destination)
    for child in source_path.iterdir():
        if child.is_file():
            for keyword in keywords:
                if keyword.upper() in child.name.upper():
                    destination_path = destination_root / keyword
                    destination_path.mkdir(parents=True, exist_ok=True)
                    shutil.copy(src=child, dst=destination_path)
                    print(f'{child.name} has successfully been copied to {destination_path}')
