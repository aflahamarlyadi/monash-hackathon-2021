import itertools
import os
import shutil


def group_file(file_list):
    file_list.sort()

    res = []
    for key, group in itertools.groupby(file_list, lambda file: file.split("_")[0]):
        lst = list(group)
        res.append((key, lst))

    return res


def run():
    path = "C:/Users/Asus/Desktop/hackathon/test_file"
    files = os.listdir(path)
    grouped_files = group_file(files)

    for item in grouped_files:
        keyword = item[0]
        group = item[1]
        if len(group) > 1:
            for file in group:
                name, ext = os.path.splitext(file)
                ext = ext[1:]

                if os.path.exists(path + "/" + keyword):
                    shutil.move(path + "/" + file, path + "/" + keyword + "/" + file)

                else:
                    os.makedirs(path + "/" + keyword)
                    shutil.move(path + "/" + file, path + "/" + keyword + "/" + file)


if __name__ == "__main__":
    run()
