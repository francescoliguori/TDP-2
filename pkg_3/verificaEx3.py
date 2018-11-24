import unittest
from Repetition import *


class TestProjectEx3(unittest.TestCase):

    def test_differentFile(self):
        print("---test tutti file differenti---")
        result=find_repetition("./differentfile/")
        print(result)
        self.assertEqual(result,[])

    def test_sameFile(self):
        print("---test tutti file uguali---")
        result=find_repetition("./samefile/")
        print(result)
        self.assertEqual(result,['prova3.txt', 'prova4 - Copia.txt', 'prova4.txt'])

    def test_mixedFile(self):
        print("---test file differenti ed uguali---")
        result=find_repetition("./mixedfile/")
        print(result)
        self.assertEqual(result,['prova1.txt', 'prova2.txt', 'prova4.txt'])

if __name__ == "__main__":
    unittest.main()

