# monash-hackathon-2021

## FUNCTIONS:

    1. Organize all the files in a folder (Downloads folder by default) by their file type and date of creation.
    
    2. Organize all the files in a folder (Downloads folder by default) by a list of keywords entered by the user.
    
## INSTRUCTIONS:

    1. For the purpose of testing, create an empty folder in the user folder named "Hackathon" (eg. "C:\Users\username\Hackathon")
    and a subfolder in the newly created folder named "Downloads" (eg. "C:\Users\user\Hackathon\Downloads")
    In the future, this will be changed to the local user folder, "C:\Users\username", and local Downloads folder, "C:\Users\username\Downloads", respectively.
    
    2. Then, add or create dummy files of various types (can check extensions.py to view all compatible the file types) into the Downloads folder 
    "C:\Users\user\Hackathon\Downloads".
    
    3. Run app.py
    
    4. To organize the files by file type, simply click the Run button with all the entries left empty.
    This will move your files to subfolders based on their file type and creation date by default.
    
    5. To organize the files by keywords, tick the "Organize by keywords" checkbox and enter the keywords that you want to group your files with.
    IMPORTANT: separate each keyword with a comma.
    
    6. Optional: try running the program on youur local downloads folder by filling the "Source folder" entry with "C:\Users\username\Downloads".
    Or other files that you have in mind that you want to organize, just copy paste the source and destination paths from the address bar to the respective entries.
    
    7. To view where all your files have been moved, go to "History" and to clear your history, go to "Settings" and click "Clear history".
    
    8. To switch between light mode and dark mode, go to "Settings" and switch between themes
    
## FUTURE IMPLEMENTATIONS:

    1. Publish a website to install the program
    
    2. Add a Browse button for the source and destination folder entry
    
    3. Add an Analysis menu to show total files moved and deleted (total storage cleared), as data collected will be useful and
    notify the user of files that haven't been opened for a long period of time and large files.
    
    4. Add more settings in the Settings menu to make the program more dynamic 
    (eg. option to disable creating the date folder, option to disable deleting files automatically, option to restore a deleted file, etc.)
    
    5. Furthur beautify the gui
