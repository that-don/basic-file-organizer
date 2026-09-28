from tkinter import filedialog, Tk
from pathlib import Path
from file_organizer import FileOrganizer

def select_folder():
    root = Tk()
    root.withdraw()
    
    folder = filedialog.askdirectory()
    return folder

def main():
    folder = select_folder()
    if not folder:
        print('nessuna cartella selezionata')
        return
    organize = FileOrganizer(Path(folder))
    organize.organize()
    print('file organizzati con successo')
    
if __name__ == '__main__':
    main()