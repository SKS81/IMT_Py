import unittest
import ImtServ


class MyTestCase(unittest.TestCase):
    def test_imtCalc(self):
        exp1 = 4
        act1 = int(ImtServ.imtCalc(12, 1.6))
        self.assertEqual(exp1, act1)

    def test_imtRez(self):
        exp2 = "У Вас нормальный вес"
        act2 = ImtServ.imtRez(20)
        self.assertEqual(exp2, act2)
