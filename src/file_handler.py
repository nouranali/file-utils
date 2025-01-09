
from pathlib import Path
import pprint
class FileHandler:
    def __init__(self):
        pass
    
    def list_files(self,directory,extensions):
        """
        Lists and prints files in the specified directory with the given extensions.

        Args:
            directory (str or Path): The directory to search for files.
            extensions (list of str): List of file extensions to search for.
        """
        directory = Path(directory)
        for extension in extensions:
            files = list(directory.rglob(extension))
            files=list(map(lambda file: f"File: {file.name}", files))
            pprint.pprint(f"files with {extension} extension:{files}")
    def move_files_by_extension(self,directory,extensions,destination,copy=False):
        """
        Moves files in the specified directory with the given extensions to the destination directory.

        Args:
            directory (str or Path): The directory to search for files.
            extensions (list of str): List of file extensions to search for.
            destination (str or Path): The directory to move the files to.
        """
        directory = Path(directory)
        destination = Path(destination)
        if not destination.exists():
            destination.mkdir(parents=True)
        for extension in extensions:
            files = list(directory.rglob(extension))
            for file in files:
                file.rename(destination / file.name)
                pprint.pprint(f"Moved {file.name} to {destination}")
    def move_by_extension_and_directory(self,directory_from,mapper,copy=False):
        """
        Moves files in the specified directory with the given extensions to the destination directory.

        Args:
            directory (str or Path): The directory to search for files.
            extensions (list of str): List of file extensions to search for.
            destination (str or Path): The directory to move the files to.
        """
        directory_from = Path(directory_from)
        for extension,destination in mapper.items():
            destination = Path(destination)
            if not destination.exists():
                destination.mkdir(parents=True)
            files = list(directory_from.rglob(extension))
            for file in files:
                file.rename(destination / file.name)
                pprint.pprint(f"Moved {file.name} to {destination}")

