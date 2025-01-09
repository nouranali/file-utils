import argparse
from src.file_handler import FileHandler
def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source_directory', type=str)
    parser.add_argument('--destination_directory', type=str,nargs='+')
    parser.add_argument('--extensions', type=str,nargs='+')
    parser.add_argument('--move_files_by_extension', action='store_true')
    return parser

def main():
    args = make_parser().parse_args()
    source_directory = args.source_directory
    destination_directory = args.destination_directory
    extensions = args.extensions
    if len(destination_directory) == 1:
        destination_directory = destination_directory[0]
    print(f"source_directory: {source_directory}")
    print(f"destination_directory: {destination_directory}")
    print(f"extensions: {extensions}")
    
    filehandler= FileHandler()
    filehandler.list_files(source_directory,extensions)
    filehandler.move_files_by_extension(source_directory,extensions,destination_directory)
    # filehandler.move_by_extension_and_directory("/home/nouran/dl_utils/tmp",{"*.txt":"/home/nouran/dl_utils/tmp2","*.json":"/home/nouran/dl_utils/tmp3"})

main()
