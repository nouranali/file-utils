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
    
    def find_file_pairs(self,extensions,mapper,move_dir=None):
        """
        Finds and optionally moves files that do not have matching pairs based on their extensions.
        Args:
            extensions (list): A list of two file extensions to be compared.
            mapper (dict): A dictionary mapping file extensions to their respective directories.
            move_dir (str, optional): The directory to move non-matching files to. Defaults to None.
        Returns:
            None
        """
        dir1 = mapper[extensions[0]]    
        dir2 = mapper[extensions[1]]
        dir1_files = sorted(list(Path(dir1).rglob(extensions[0])))
        dir2_files = sorted(list(Path(dir2).rglob(extensions[1])))
        dir1_file_names = [file.name.split(".")[0] for file in dir1_files]
        non_matching_files = [file for file in dir2_files if file.name.split(".")[0] not in dir1_file_names]
        pprint.pprint(f"Non matching files:{non_matching_files}")
        if move_dir:
            for file in non_matching_files:
                file.rename(Path(move_dir) / file.name)
                pprint.pprint(f"Moved {file.name} to {dir1}")

              
        