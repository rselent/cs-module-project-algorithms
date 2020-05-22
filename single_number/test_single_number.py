import unittest
import random
from single_number import single_number, single_number2, single_number3

class Test(unittest.TestCase):
    def test_single_number(self):
        arr = []

        for i in range(1000):
            arr.append(i)
            arr.append(i)

        random.shuffle(arr)
        rand_index = random.randint(0, len(arr))
        num = arr.pop(rand_index)

#        self.assertEqual(single_number(arr), num)
#        self.assertEqual(single_number2(arr), num)
        self.assertEqual(single_number3(arr), num)


if __name__ == '__main__':
    unittest.main()