# import os
# import hashlib
# import _md5
# import sys
# import filecmp
# import stat
# import io
# def find_repetition(dir):
#     unique = []
#     list=[]
#     for filename in os.listdir(dir):
#
#         filepath=dir+filename
#         if os.path.isfile(filepath):
#
#             filehash = _md5.md5(io.StringIO(filename).read().encode('utf-8')).hexdigest()
#
#         if filehash not in unique:
#
#             unique.append(filehash)
#         else:
#
#             list.append(filename)
#     return list
#
# if __name__=="__main__":
#     #dir="../filetest/"
#     dir = "./filetest/"
#     print(find_repetition(dir))

import os
import hashlib
import _md5
import sys
import filecmp
import stat
import io
def find_repetition(dir):
    unique = []
    list=[]
    for filename in os.listdir(dir):
        print(filename)
        filepath=dir+filename
        if os.path.isfile(filepath):

            filehash = hashlib.md5(open(filepath, 'rb').read()).hexdigest()  #modificato qui

        if filehash not in unique:

            unique.append(filehash)
        else:

            list.append(filename)
    return list

if __name__=="__main__":
    dir="./filetest/"

    print(find_repetition(dir))