import unittest
from app import check_password_strength

class TestPasswordStrength(unittest.TestCase):
    def test_weak_password(self):
        result = check_password_strength("123")
        self.assertEqual(result["strength"], "weak")

    def test_strong_password(self):
        result = check_password_strength("S3cur3P@ss!")
        self.assertEqual(result["strength"], "strong")

if __name__ == '__main__':
    unittest.main()

