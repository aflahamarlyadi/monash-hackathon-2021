# importing os and shutil module  
import os, shutil, time
from datetime import datetime



def units_input():
    units = []

    num_units = int(input(f"Number of units taking this semester: "))
    
    if num_units > 0:
        print("Enter your units")
        for i in range(num_units):
            unit = input()
            units.append(unit)

    else:
        print("Invalid input")

    return units



def create_directory(path):
    try:
        os.makedirs(path, exist_ok = True)
        print(f"Directory {path} created successfully")
    except OSError as error:
        print(f"Directory {path} cannot be created")



def check_directory(path): 
    if not os.path.exists(path):
        create_directory(path)



def creation_date(file):
    date = datetime.strptime(time.ctime(os.path.getctime(file)), "%a %b %d %H:%M:%S %Y")
    month = str(date.strftime("%b"))
    year = str(date.year)
    return f"{month}-{year}"



def general_user_mode(source, destination):
    """
    Moves the files from the source directory to a desired destination directory

    If student_mode is enabled, if the file type is a pdf or docx files then move the file to the specified unit folder
        else the file will remain in the 'Downloads' directory

    Else
        if the file type is a pdf or docx then move the file to the 'Documents' directory

        if the file type is a jpg or png then move the file to the 'Pictures' directory

        if the file type is a mp3 then move the file to the 'Music' directory

        if the file type is a mp4 then move the file to the 'Videos' directory
    """

    files = os.listdir(source)

    for file in files:
        file_path = os.path.join(source, file)

        if file_path.endswith('.pdf') or file_path.endswith('.docx'):
            cr_date = creation_date(file_path)
            check_directory(os.path.join(destination, 'Documents', cr_date))
            shutil.move(file_path, os.path.join(destination, 'Documents', cr_date))
            print(f"{file} has successfully been moved to {os.path.join(destination, 'Documents', cr_date)}")

        elif file_path.endswith('.jpg') or file_path.endswith('.png'):
            cr_date = creation_date(file_path)
            check_directory(os.path.join(destination, 'Pictures', cr_date))
            shutil.move(file_path, os.path.join(destination, 'Pictures', cr_date))
            print(f"{file} has successfully been moved to {os.path.join(destination, 'Pictures', cr_date)}")

        elif file_path.endswith('.mp3'):
            cr_date = creation_date(file_path)
            check_directory(os.path.join(destination, 'Music', cr_date))
            shutil.move(file_path, os.path.join(destination, 'Music', cr_date))
            print(f"{file} has successfully been moved to {os.path.join(destination, 'Music', cr_date)}")

        elif file_path.endswith('.mp4'):
            cr_date = creation_date(file_path)
            check_directory(os.path.join(destination, 'Videos', cr_date))
            shutil.move(file_path, os.path.join(destination, 'Videos', cr_date))
            print(f"{file} has successfully been moved to {os.path.join(destination, 'Videos', cr_date)}")

        else:
            print(f"{file} has not been moved")

def student_mode(source, destination):
    files = os.listdir(source)

    units = units_input()

    for file in files:
        has_been_moved = False
        file_path = os.path.join(source, file)
        destination_path = os.path.join(destination, "University")
        
        if file_path.endswith('.pdf') or file_path.endswith('.docx'):
            for unit in units:
                if unit.upper() in file.upper():
                    check_directory(os.path.join(destination_path, unit))
                    shutil.move(file_path, os.path.join(destination_path, unit))
                    print(f"{file} has successfully been moved to {os.path.join(destination_path, unit)}")
                    has_been_moved = True

            if not has_been_moved:
                print(f"{file} has not been moved")
