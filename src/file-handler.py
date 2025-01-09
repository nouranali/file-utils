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


def main():
    filehandler= FileHandler()
    filehandler.list_files("/home/nouran/dl_utils/tmp",["*.json","*.txt"])
main()