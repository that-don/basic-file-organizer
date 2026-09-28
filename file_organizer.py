from pathlib import Path
import shutil


class FileOrganizer:
    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.categories = {
            "Immagini": [".png", ".jpeg", ".jpg", ".webp"],
            "Documenti": [".docx", ".pdf", ".txt", ".doc", ".odt"]
        }

    def organize(self):
        for file in self.base_path.iterdir():
            if file.is_file():
                category = self.get_category(file)               
                if category == "Altro": continue             
                destination_folder = self.base_path / category
                self.create_folder(destination_folder)
                new_path = self.resolve_conflict(destination_folder / file.name)
                self.move_file(file, new_path)
                
    def get_category(self, file: Path):
        for category, extension in self.categories.items():
            if file.suffix in extension:
                return category
        return "Altro"
    
    def create_folder(self, folder: Path):
        folder.mkdir(exist_ok=True)
            
    def resolve_conflict(self, destination: Path):
        counter = 1
        new_destination = destination
        while destination.exists():
            new_name = f"{destination.stem}({counter}){destination.suffix}"
            new_destination = destination.parent / new_name
            counter += 1
        return new_destination
    
    def move_file(self, source: Path, destination: Path):
        shutil.move(str(source),str(destination))