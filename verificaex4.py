import unittest
from circularSubstring import *


STRING="ciaomondo"

class TestProjectEx4(unittest.TestCase):
    print("stringa in cui cercare :",STRING)
    print("")

    def test_substring_normal(self):
        print("----test substring normale----")
        substring="c"
        print("substring : ",substring)
        self.assertTrue(circular_substring(substring,STRING))
        print("la sottostringa è presente")

    def test_substring_0(self):
        print("----test substring lunghezza 0 ----")
        substring=""
        print("substring : ",substring)
        self.assertTrue(circular_substring(substring,STRING))
        print("la sottostringa è presente")

    def test_nosubstring(self):
        print("----test substring non presente ----")
        substring="test"
        print("substring : ",substring)
        self.assertFalse(circular_substring(substring,STRING))
        print("la sottostringa non è presente")

    def test_circular_substring(self):
        print("----test circular substring  ----")
        substring="ocia"
        print("substring : ",substring)
        self.assertTrue(circular_substring(substring,STRING))
        print("la sottostringa è presente")

if __name__ == "__main__":
    unittest.main()
