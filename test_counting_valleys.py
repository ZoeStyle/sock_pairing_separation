from unittest import TestCase
from counting_valleys import sock_merchant


class teste(TestCase):

    def test_number_of_pairs_1(self):
        list = [10, 20, 20, 10, 10, 30, 50, 10, 20]
        result = sock_merchant(list)
        self.assertEqual(result, 3)

    def test_number_of_pairs_2(self):
        list = [6, 5, 2, 3, 5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5]
        result = sock_merchant(list)
        self.assertEqual(result, 6)

    def test_number_of_pairs_3(self):
        list = [50, 49, 38, 49, 78,
                36, 25, 96, 10, 67, 78, 58, 98, 8, 53, 1, 4, 7,
                29, 6, 59, 93, 74, 3, 67, 47, 12, 85, 84, 40,
                81, 85, 89, 70, 33, 66, 6, 9, 13, 67, 75, 42,
                24, 73, 49, 28, 25, 5, 86, 53, 10, 44, 45, 35,
                47, 11, 81, 10, 47, 16, 49, 79, 52, 89, 100, 36,
                6, 57, 96, 18, 23, 71, 11, 99, 95, 12, 78, 19, 16,
                64, 23, 77, 7, 19, 11, 5, 81, 43, 14, 27, 11, 63,
                57, 62, 3, 56, 50, 9, 13, 45]
        result = sock_merchant(list)
        self.assertEqual(result, 28)

    def test_number_of_pairs_4(self):
        list = [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]
        result = sock_merchant(list)
        self.assertEqual(result, 9)

    def test_number_of_pairs_5(self):
        list = [44, 55, 11, 15, 4, 72, 26, 91, 80, 14, 43, 78, 70, 75,
                36, 83, 78, 91, 17, 17, 54, 65, 60, 21, 58, 98, 87, 45,
                75, 97, 81, 18, 51, 43, 84, 54, 66, 10, 44, 45, 23, 38,
                22, 44, 65, 9, 78, 42, 100, 94, 58, 5, 11, 69, 26, 20,
                19, 64, 64, 93, 60, 96, 10, 10, 39, 94, 15, 4, 3, 10, 1,
                77, 48, 74, 20, 12, 83, 97, 5, 82, 43, 15, 86, 5, 35, 63,
                24, 53, 27, 87, 45, 38, 34, 7, 48, 24, 100, 14, 80, 54]
        result = sock_merchant(list)
        self.assertEqual(result, 30)

    def test_number_of_pairs_6(self):
        list = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
        result = sock_merchant(list)
        self.assertEqual(result, 4)
