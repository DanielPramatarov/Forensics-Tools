import os
import argparse
from datetime import date
import stat


class FileForensics:
    def __init__(self):
        self.path = ''

    @staticmethod
    def get_args():
        """Take a look at those args."""
        parser = argparse.ArgumentParser(description='Utility designed to \
           scan all files in a path')
        # parser.add_argument("path", help="Path to file you want to scan")
        parser.add_argument('-p', dest="path", type=str, help='Path to the file', required=True)
        
        return parser.parse_args()

    def scan_file(self):
        file_info = os.stat(self.path)
        print("========================== Permisions ==========================")
        print(stat.filemode(file_info.st_mode))
        print("========================== Time Stamps ==========================")
        print("Time of last access:",date.fromtimestamp(file_info.st_atime))
        print("Time of last modification:",date.fromtimestamp(file_info.st_mtime))
        print("Time of last status change:",date.fromtimestamp(file_info.st_ctime))
        print("Protection:",(file_info.st_mode))
        print("Total size, in bytes:",(file_info.st_size))
        print("Owner id of the file:", file_info.st_uid)
        print("Group id of the file:", file_info.st_uid) 

    def main(self):
        args = self.get_args()
        self.path = args.path

        self.scan_file()


if __name__ == '__main__':
    file_instance = FileForensics()
    file_instance.main()
