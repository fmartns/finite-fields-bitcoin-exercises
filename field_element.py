from unittest import TestCase


class FieldElement:
    """Element of a finite field F_p."""

    def __init__(self, num, prime):
        self.num = num
        self.prime = prime

    def __repr__(self):
        return f"FieldElement({self.num}, {self.prime})"

    def __eq__(self, other):
        if not isinstance(other, FieldElement):
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        raise NotImplementedError("Implement __ne__")

    def __add__(self, other):
        raise NotImplementedError("Implement __add__")

    def __sub__(self, other):
        raise NotImplementedError("Implement __sub__")

    def __mul__(self, other):
        raise NotImplementedError("Implement __mul__")

    def __pow__(self, exponent):
        raise NotImplementedError("Implement __pow__")

    def __truediv__(self, other):
        raise NotImplementedError("Implement __truediv__")


class FieldElementTest(TestCase):
    def test_eq(self):
        self.assertEqual(FieldElement(3, 11), FieldElement(3, 11))
        self.assertNotEqual(FieldElement(3, 11), FieldElement(4, 11))
        self.assertNotEqual(FieldElement(3, 11), FieldElement(3, 13))

    def test_ne(self):
        self.assertTrue(FieldElement(2, 7) != FieldElement(5, 7))
        self.assertFalse(FieldElement(9, 11) != FieldElement(9, 11))

    def test_init(self):
        FieldElement(0, 11)
        FieldElement(10, 11)
        with self.assertRaises(ValueError):
            FieldElement(11, 11)
        with self.assertRaises(ValueError):
            FieldElement(12, 11)
        with self.assertRaises(ValueError):
            FieldElement(-1, 11)

    def test_add(self):
        self.assertEqual(
            FieldElement(9, 11) + FieldElement(5, 11),
            FieldElement(3, 11),
        )
        self.assertEqual(
            FieldElement(6, 7) + FieldElement(5, 7),
            FieldElement(4, 7),
        )

    def test_sub(self):
        self.assertEqual(
            FieldElement(3, 11) - FieldElement(8, 11),
            FieldElement(6, 11),
        )
        self.assertEqual(
            FieldElement(1, 13) - FieldElement(5, 13),
            FieldElement(9, 13),
        )

    def test_mul(self):
        self.assertEqual(
            FieldElement(9, 11) * FieldElement(5, 11),
            FieldElement(1, 11),
        )
        self.assertEqual(
            FieldElement(7, 13) * FieldElement(7, 13),
            FieldElement(10, 13),
        )

    def test_pow(self):
        self.assertEqual(FieldElement(3, 13) ** 4, FieldElement(3, 13))
        self.assertEqual(FieldElement(2, 7) ** 3, FieldElement(1, 7))
        self.assertEqual(FieldElement(3, 11) ** -1, FieldElement(4, 11))
        self.assertEqual(FieldElement(5, 11) ** -2, FieldElement(4, 11))

    def test_div(self):
        self.assertEqual(
            FieldElement(7, 11) / FieldElement(3, 11),
            FieldElement(6, 11),
        )
        self.assertEqual(
            FieldElement(8, 13) / FieldElement(5, 13),
            FieldElement(12, 13),
        )
        with self.assertRaises(ZeroDivisionError):
            _ = FieldElement(4, 11) / FieldElement(0, 11)
