from unittest import TestCase


def clock_add(hour, delta, modulo=12):
    raise NotImplementedError("Implement clock_add")


def multiplicative_inverse(n, prime):
    raise NotImplementedError("Implement multiplicative_inverse")


def assert_fermat_holds(prime):
    raise NotImplementedError("Implement assert_fermat_holds")


class FiniteFieldsTest(TestCase):
    def test_clock_add(self):
        self.assertEqual(clock_add(3, 47, 12), 2)
        self.assertEqual(clock_add(3, -16, 12), 11)
        self.assertEqual(clock_add(23, 97, 60), 0)

    def test_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(3, 11), 4)
        self.assertEqual(multiplicative_inverse(7, 13), 2)
        prime = 31
        n = 17
        inv = multiplicative_inverse(n, prime)
        self.assertEqual((n * inv) % prime, 1)

    def test_fermat(self):
        for prime in (7, 11, 13, 31):
            with self.subTest(prime=prime):
                assert_fermat_holds(prime)
