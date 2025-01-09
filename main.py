import argparse
from src.file_handler import FileHandler
def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source_directory', type=str)
    parser.add_argument('--destination_directory', type=str,nargs='+')
    parser.add_argument('--extensions', type=str,nargs='+')
    parser.add_argument('--move_files_by_extension', action='store_true')
    parser.add_argument('--move_by_extension_and_directory', action='store_true')
    return parser

def main():
    args = make_parser().parse_args()
    source_directory = args.source_directory
    destination_directory = args.destination_directory
    extensions = args.extensions
    print(f"source_directory: {source_directory}")
    print(f"destination_directory: {destination_directory}")
    print(f"extensions: {extensions}")
    
    filehandler= FileHandler()
    filehandler.list_files(source_directory,extensions)
    if args.move_files_by_extension:
        filehandler.move_files_by_extension(source_directory,extensions,destination_directory)
    if args.move_by_extension_and_directory:
        mapper = dict(zip(extensions,destination_directory))
        filehandler.move_by_extension_and_directory(source_directory,mapper)

main()
