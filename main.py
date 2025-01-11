import argparse
from src.file_handler import FileHandler
def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source_directory', type=str)
    parser.add_argument('--destination_directory', type=str,nargs='+')
    parser.add_argument('--extensions', type=str,nargs='+')
    parser.add_argument('--move_files_by_extension', action='store_true')
    parser.add_argument('--move_by_extension_and_directory', action='store_true')
    parser.add_argument('--find_file_pairs', action='store_true')
    parser.add_argument('--move_dir', type=str,default=None)

    return parser

def main():
    args = make_parser().parse_args()
    source_directory = args.source_directory
    destination_directory = args.destination_directory
    extensions = args.extensions    
    filehandler= FileHandler()
    filehandler.list_files(source_directory,extensions)
    if args.move_files_by_extension:
        filehandler.move_files_by_extension(source_directory,extensions,destination_directory)
    if args.move_by_extension_and_directory:
        mapper = dict(zip(extensions,destination_directory))
        filehandler.move_by_extension_and_directory(source_directory,mapper)
    if args.find_file_pairs:
        mapper = dict(zip(extensions,destination_directory))
        move_dir=args.move_dir
        filehandler.find_file_pairs(extensions,mapper,move_dir)

if __name__ == '__main__':
    main()