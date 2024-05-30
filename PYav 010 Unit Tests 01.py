import unittest


class Pruebas(unittest.TestCase):
    def test_ok(self):
        pass

    def test_fail(self):
        raise AssertionError()

    def test_error(self):
        3/0


if __name__ == '__main__':
    unittest.main()