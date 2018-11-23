from Statistics import Statistics
import unittest


class TestStatics(unittest.TestCase):
    def test_popola_albero_da_file(self):
        with self.assertRaises(FileNotFoundError):
            stat = Statistics("Path_errato")

        with self.assertRaises(ValueError):
            stat = Statistics("data_set_corrotto.txt")

        stat = Statistics("data_set.txt")
        for e in stat.avl.preorder():
            print(e.key(), " ", e.value())

    def test_add(self):
        print("TEST add()\n")
        stat = Statistics("data_set_test.txt")
        with self.assertRaises(TypeError):
            stat.add("ciao", 5)
            stat.add("ciao", "ciao")
            stat.add(5, "ciao")

        print("\n\nAggiungo 5, 10\n")
        stat.add(5, 10)
        for e in stat.avl.preorder():
            print(e.key(), " ", e.value())

        print("\n\nAggiungo 54, 24\n")
        stat.add(54, 24)
        for e in stat.avl.preorder():
            print(e.key(), " ", e.value())

        print("\n\nAggiungo 54, 16\n")
        stat.add(54, 16)
        for e in stat.avl.preorder():
            print(e.key(), " ", e.value())

    def test_occurrences(self):
        print("TEST occurrences()\n")
        stat = Statistics("data_set_test.txt")

        for e in stat.avl.preorder():
            print(e.key(), " ", e.value())

        self.assertEqual(stat.occurrences(), 10)
        print("\nOccorrenze: ", stat.occurrences())

        print("\n\nAggiungo 54, 16\n")
        stat.add(54, 16)
        for e in stat.avl.preorder():
            print(e.key(), " ", e.value())

        self.assertEqual(stat.occurrences(), 11)
        print("\nOccorrenze: ", stat.occurrences())

        print("\n\nAggiungo 13, 10\n")
        stat.add(13, 10)
        for e in stat.avl.preorder():
            print(e.key(), " ", e.value())
        self.assertEqual(stat.occurrences(), 12)
        print("\nOccorrenze: ", stat.occurrences())

    def test_average(self):
        print("TEST average()\n")
        stat = Statistics("data_set_test.txt")
        self.assertEqual(10.8, stat.average())
        print("Media: ", stat.average())

        print("\nAggiungo 54, 16\n")
        stat.add(54, 16)
        self.assertEqual(11.272727272727273, stat.average())
        print("Media: ", stat.average())

        print("\nAggiungo 13, 10\n")
        stat.add(13, 10)
        self.assertEqual(11.166666666666666, stat.average())
        print("Media: ", stat.average())

    def test_median(self):
        print("TEST median()\n")
        stat = Statistics("data_set_test.txt")
        self.assertEqual(4, stat.median())
        print("Mediana: ", stat.median())

        print("\nAggiungo 54, 16\n")
        stat.add(54, 16)
        self.assertEqual(4, stat.median())
        print("Mediana: ", stat.median())

        print("\nAggiungo 13, 10\n")
        stat.add(13, 10)
        self.assertEqual(4, stat.median())
        print("Mediana: ", stat.median())

        print("\nAggiungo 2, 4\n")
        stat.add(2, 4)

        self.assertEqual(4, stat.median())
        print("Mediana: ", stat.median())

        print("\nAggiungo 2, 4\n")
        stat.add(2, 4)

        self.assertEqual(4, stat.median())
        print("Mediana: ", stat.median())

        print("\nAggiungo 2, 4\n")
        stat.add(2, 4)

        self.assertEqual(4, stat.median())
        print("Mediana: ", stat.median())

        print("\nAggiungo 2, 4\n")
        stat.add(2, 4)

        self.assertEqual(3, stat.median())
        print("Mediana: ", stat.median())

    def test_percentile(self):
        print("TEST percentile()\n")
        stat = Statistics("data_set_test.txt")
        with self.assertRaises(ValueError):
            percentile = stat.percentile(0)
            percentile = stat.percentile(100)
            percentile = stat.percentile(-5)
            percentile = stat.percentile(105)

        with self.assertRaises(TypeError):
            percentile = stat.percentile("ciao")
            percentile = stat.percentile(50.5)

        self.assertEqual(1, stat.percentile(1))
        print("Percentile a 1: ", stat.percentile(1))

        self.assertEqual(1, stat.percentile(10))
        print("Percentile a 10: ", stat.percentile(10))

        self.assertEqual(3, stat.percentile())
        print("Percentile a 20: ", stat.percentile())

        self.assertEqual(3, stat.percentile(30))
        print("Percentile a 30: ", stat.percentile(30))

        self.assertEqual(3, stat.percentile(40))
        print("Percentile a 40: ", stat.percentile(40))

        self.assertEqual(4, stat.percentile(50))
        print("Percentile a 50: ", stat.percentile(50))

        self.assertEqual(4, stat.percentile(60))
        print("Percentile a 60: ", stat.percentile(60))

        self.assertEqual(5, stat.percentile(70))
        print("Percentile a 70: ", stat.percentile(70))

        self.assertEqual(8, stat.percentile(80))
        print("Percentile a 80: ", stat.percentile(80))

        self.assertEqual(13, stat.percentile(90))
        print("Percentile a 90: ", stat.percentile(90))

        self.assertEqual(15, stat.percentile(99))
        print("Percentile a 9: ", stat.percentile(99))

    def test_most_frequent(self):
        print("TEST mostFrequent(j)\n")
        stat = Statistics("data_set_test.txt")
        with self.assertRaises(ValueError):
            most_frequent = stat.mostFrequent(-1)
            most_frequent = stat.mostFrequent(stat.len() + 1)

        with self.assertRaises(TypeError):
            most_frequent = stat.mostFrequent(5.3)
            most_frequent = stat.mostFrequent("ciao")

        self.assertEqual("[]", stat.mostFrequent(0).__str__())
        print("Most frequent 0: ", stat.mostFrequent(0))

        self.assertEqual("[3]", stat.mostFrequent(1).__str__())
        print("Most frequent 1: ", stat.mostFrequent(1))

        self.assertEqual("[3, 4, 1, 13, 8, 5]", stat.mostFrequent(stat.len() - 1).__str__())
        print("Most frequent {} : ".format(stat.len() - 1), stat.mostFrequent(stat.len() - 1))

        self.assertEqual("[3, 4, 1, 13, 8, 5, 15]", stat.mostFrequent(stat.len()).__str__())
        print("Most frequent {} : ".format(stat.len()), stat.mostFrequent(stat.len()))


if __name__ == "__main__":
    unittest.main()
