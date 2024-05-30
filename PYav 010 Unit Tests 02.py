import unittest

def test_comparac(n1, n2):
    if n1 < n2:
        return True
    else:
        return False

class Pruebas(unittest.TestCase):
    def test(self):
        self.assertTrue(test_comparac(7,5))

if __name__ == '__main__':
    unittest.main()