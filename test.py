import os

path = "/Users/hazmini/Dropbox/Mac/Documents/Endnote/"

file_list = []
for current_dir, sub_dirs, files in os.walk(path):
    print(len(files))
    for file in files:
        file_list.append(file)

import pandas as pd

df = pd.DataFrame(file_list)

import os
import datetime
import pandas as pd
import shutil

from_path = "/Users/haz/Downloads"
to_path = "/Volumes/Ubuntu/Video/xxx"


class FileManager():
    def __init__(self, directory):
        self.directory = directory
        self.df = None

    def initialize(self):
        self.check_files()

    def check_files(self):
        self.df = self._extract_file('mp4')

    def _get_updatetime(self, file, format):
        t = os.path.getmtime(file)
        d = datetime.datetime.fromtimestamp(t)
        return d.strftime(format)

    def _extract_file(self, extension):
        files = []
        file_paths = []
        updatetimes = []
        for current_dir, sub_dirs, file_list in os.walk(self.directory):
            for file_name in file_list:
                ext = file_name.split(".")[-1]
                if ext == extension:
                    fullpath = os.path.join(current_dir, file_name)
                    format = '%Y-%m-%d %H:%M:%S'
                    update_stamps = self._get_updatetime(fullpath, format)
                    files.append(file_name)
                    file_paths.append(fullpath)
                    updatetimes.append(update_stamps)
                elif ext == 'cfdownload':
                    print('not needed.')

        df = pd.DataFrame(list(zip(files, file_paths, updatetimes)),
                          columns=['fileName', 'path', 'updatetime'])

        return df

    def show_head(self):
        print(self.df.head())

    def move_extHdd(self):
        files = self.df.iloc[:, 1].to_list()
        for file in files:
            print(f'going to process: {file}')
            new_path = shutil.move(file, to_path)
            print("================")


if __name__ == '__main__':

    # read download file extract 'mp4'
    fM = FileManager(from_path)
    fM.initialize()

    # update -
    fM.show_head()
    fM.move_extHdd()

    fM.initialize()
    fM.show_head()
