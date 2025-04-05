import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import check_password_strength

def test_weak_password():
    result = check_password_strength("123")
    assert result["strength"] == "weak"

def test_strong_password():
    result = check_password_strength("S3cur3P@ss!")
    assert result["strength"] == "strong"

