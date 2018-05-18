from pathlib import Path
from shutil import copy2


class DirectoryFlattener:
    def __init__(self, src_dir, dist_dir):
        self.src_dir = Path(src_dir)
        self.dist_dir = Path(dist_dir)

    def process_directory(self, start_dir=None):
        if (not start_dir):
            start_dir = self.src_dir

        for child in start_dir.iterdir():
            if child.is_dir():
                self.process_directory(child)
            elif child.is_file():
                print(f'copying file: {child} to {self.dist_dir}')
                self.copy_file(child)
            else:
                print('ERROR: found smth that is not either a file or a dir. \n Skipping it')

    def copy_file(self, file):
        copy2(file, self.dist_dir)
