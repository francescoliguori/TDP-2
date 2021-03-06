import os
import hashlib
from TdP_collections.hash_table.chain_hash_map import ChainHashMap

def chunk_reader(fileobj, chunk_size=1024):
    """Generator that reads a file in chunks of bytes"""
    while True:
        chunk = fileobj.read(chunk_size)
        if not chunk:
            return
        yield chunk

def find_repetition(folder):
    duplicate = []
    fileMap = ChainHashMap()
    for filename in os.listdir(folder):

        filepath = folder + filename
        if os.path.isfile(filepath):
            sha = hashlib.sha3_256()
            try:
                with open(filepath, 'rb') as file:
                    for chunk in chunk_reader(file):
                        sha.update(chunk)
                    filehash = sha.hexdigest()

            except FileNotFoundError as e:
                print("Impossibile aprire il file. Controllare che il path sia corretto.")
            except KeyError as e:
                print("Impossibile accedere alla chiave.")
            if filehash in fileMap.keys():
                fileMap.get(filehash).append(filename)
            else:
                fileMap[filehash] = [filename]
    for key in fileMap.keys():
        try:
            if len(fileMap.get(key)) > 1:
                duplicate += fileMap.get(key)[1:]  # return solo dal secondo elementotel
        except KeyError as e:
            print("Impossibile accedere alla chiave.")
        # print("dimensione", sys.getsizeof(key))  # measured in bytes
    return duplicate

# def find_repetition(folder):
#     unique, duplicate = [], []
#     hashTable =[]
#     for filename in os.listdir(folder):
#         # print(filename)
#         filepath = folder + filename
#         if os.path.isfile(filepath):
#             md5 = hashlib.md5()
#             try:
#                 with open(filepath, 'rb') as file:
#                     for chunk in chunk_reader(file):
#                         md5.update(chunk)
#                     filehash = md5.hexdigest()
#             except FileNotFoundError as e:
#                 print("Impossibile aprire il file. Controllare che il path sia corretto.")
#             if filehash not in unique:
#                 unique.append(filehash)
#             else:
#                 duplicate.append(filename)
#     return duplicate
#
#
#
#
# # ogni chiamata get andrebbe in un try cath, lancia KeyError
# def find_chain_map(folder):
#     duplicati = []
#     fileMap = ChainHashMap()
#     for filename in os.listdir(folder):
#         print(filename)
#         filepath = folder + filename
#         if os.path.isfile(filepath):
#             try:
#                 with open(filepath, 'r') as file:
#                     key = file.read()
#                     if key in fileMap.keys():
#                         fileMap.get(key).append(filename)
#                     else:
#                         fileMap[key] = [filename]
#             except FileNotFoundError as e:
#                 print("Impossibile aprire il file. Controllare che il path sia corretto.")
#             except KeyError as e:
#                 print("Impossibile accedere alla chiave.")
#     for key in fileMap.keys():
#         try:
#             if len(fileMap.get(key)) > 1:
#                 duplicati += fileMap.get(key)[1:]  # return solo dal secondo elementotel
#         except KeyError as e:
#             print("Impossibile accedere alla chiave.")
#         # print("dimensione", sys.getsizeof(key))  # measured in bytes
#     return duplicati  # STRANO su mixedfile, cambia l'ordine con cui ritorna i valori
#



