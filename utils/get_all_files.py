import os


def getAllFile(path):
    all_files = os.listdir(path)
    all_files.sort()
    return all_files
