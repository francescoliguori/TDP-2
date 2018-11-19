import os
import hashlib


def chunk_reader(fileobj, chunk_size=1024):
    """Generator that reads a file in chunks of bytes"""
    while True:
        chunk = fileobj.read(chunk_size)
        if not chunk:
            return
        yield chunk


def find_repetition(folder):
    unique, duplicate = [], []
    for filename in os.listdir(folder):
        # print(filename)
        filepath = folder + filename
        if os.path.isfile(filepath):
            md5 = hashlib.md5()
            try:
                with open(filepath, 'rb') as file:
                    for chunk in chunk_reader(file):
                        md5.update(chunk)
                    filehash = md5.hexdigest()
            except FileNotFoundError as e:
                print("Impossibile aprire il file. Controllare che il path sia corretto.")
            if filehash not in unique:
                unique.append(filehash)
            else:
                duplicate.append(filename)
    return duplicate


if __name__ == "__main__":
    folder = "./samefile/"

    print("File replicati:", find_repetition(folder))
