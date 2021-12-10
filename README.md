# monash-hackathon-2021

## PURPOSE:

    1. Organize all the files in a specified folder, or Downloads folder by default, by their file type and date of creation.
    Most useful for users who are photographers taking dozens of photos everyday or content creators recording dozens of photos everyday.
    Also useful for general use to organized a cluttered Downloads folder or any other folder.
    
    2. Organize all the files in a specified folder, or Downloads folder by default, by a list of keywords entered by the user.
    Most useful for students who wants to group all their study related documents by unit (eg. FIT1045, MAT1830), or by class type (eg. Lecture, Assignment) to a single folder

## INSTRUCTIONS:

    1. For the purpose of testing, please create an empty folder in the user folder named "Hackathon" (eg. "C:\Users\user\Hackathon")
    and a subfolder in the newly created folder named "Downloads" (eg. "C:\Users\user\Hackathon\Downloads")
    In the future, this will be changed to the local user folder, "C:\Users\user", and local Downloads folder, "C:\Users\user\Downloads", respectively.
    
    2. For the purpose of testing, add or create dummy files of various types (can check extensions.py to view all compatible the file types) into this folder: 
    "C:\Users\user\Hackathon\Downloads".
    
    3. Run the program by double clicking gui.py
    
    4. For quick organization, click the Run button with all the entries left empty. This will move your files to subfolders based on their file type.
    
    5. To organize the files by keywords, refill the folder with test files. Then type in keywords that some of the file names have in common.
    (When organizing with multiple keywords, please separate each keyword by a comma)
    Can also try to enter keywords that appears in a single file name or keywords that are not found in any file names.
    
    6. Optional: try running the program on local downloads folder by filling the "Source directory path" entry with "C:\Users\user\Downloads" and take note of the differences.
    Or other files that you have in mind that you want to sort, just copy paste the source and destination paths from the address bar to the respective entries.
    
## FUTURE IMPLEMENTATIONS:

    1. Provide user recommendations on which files to delete (duplicate files, files that haven't been opened for a long period of time)
    
    2. Analysis on file sizes, file count, total storage cleared from recommendations
    
    3. Consider having the program constantly running in the background, such that whenever a file is downloaded it will immediately be moved to the folder it belongs
    
    4. Create a log file for history of where files have been moved
