import os, shutil, time
from pathlib import Path
from filecmp import cmp
from datetime import datetime
from extensions import extension_paths


def add_cdate_to_path(child, path: Path):
    """
    Helper function that adds current month and year to destination path.
    """
    date = datetime.strptime(time.ctime(os.path.getctime(child)), "%a %b %d %H:%M:%S %Y")
    dated_path = path.joinpath(f'{date.strftime("%b")} {date.year}')
    return dated_path


def remove_duplicates(source):
    """
    Helper function that remove duplicates in a directory
    """
    source_path = Path(source)
    files = os.listdir(source_path)
    history = ""
    delete_count = 0

    duplicates = []

    for file in files:
        
        is_duplicate = False
        
        for class_ in duplicates:
            is_duplicate = cmp(
                source_path / file,
                source_path / class_[0],
                shallow = False
            )
            if is_duplicate:
                class_.append(file)
                break
        
        if not is_duplicate:
            duplicates.append([file])

    for class_ in duplicates:
        for file in class_[:-1]:
            os.remove(source_path / file)
            delete_count += 1
            history += f'Duplicate of {file} found\n'
    
    return history, delete_count


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
    history = ""
    moved_files_count = 0
    deleted_files_count = 0

    for child in source_path.iterdir():
        if child.is_file() and child.suffix.lower() in extension_paths:
            destination_path = destination_root.joinpath(extension_paths[child.suffix.lower()])
            destination_path = add_cdate_to_path(child, path=destination_path)
            if os.path.exists(destination_path.joinpath(child.name)):
                os.remove(child)
                deleted_files_count += 1
                history += f'Duplicate of {child.name} found in {destination_path}\n'
            else:
                destination_path.mkdir(parents=True, exist_ok=True)
                shutil.move(src=str(child), dst=str(destination_path))
                moved_files_count += 1
                history += f'{child.name} has successfully been moved to {destination_path}\n'

    return history, moved_files_count, deleted_files_count


def organize_by_keyword(source, destination, keywords):
    """
    Main function that moves the files from the source directory to a desired destination directory based on keywords entered
    For loop only check for files and not directories then checks if the keywords exists in the file name
    """
    source_path = Path(source)
    destination_path = Path(destination)
    destination_root = Path(destination)
    organized_files = set()
    history = ""
    moved_files_count = 0
    deleted_files_count = 0

    for child in source_path.iterdir():
        if child.is_file():
            for keyword in keywords:
                if keyword.upper() in child.name.upper():
                    destination_path = destination_root.joinpath(keyword)
                    destination_path.mkdir(parents=True, exist_ok=True)
                    shutil.copy(src=str(child), dst=str(destination_path))
                    moved_files_count += 1
                    history += f'{child.name} has successfully been moved to {destination_path}\n'
                    organized_files.add(child)
    
    for file in organized_files:
        if os.path.exists(file):
            os.remove(file)
            deleted_files_count += 1

    return history, moved_files_count, deleted_files_count
