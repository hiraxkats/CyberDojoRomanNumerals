import sys
import os 
import pytest

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from roman_numeral import RomanNumeral

@pytest.mark.parametrize(
    "arabic_digit, roman_numeral",
    [
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (5, "V"),
        (6, "VI"),
        (7, "VII"),
        (8, "VIII"),
        (9, "IX"),
        (10, "X"),
        (11, "XI"),
        (12, "XII"),
        (13, "XIII"),
        (14, "XIV"),
        (15, "XV"),
        (16, "XVI"),
        (17, "XVII"),
        (18, "XVIII"),
        (19, "XIX"),
        (20, "XX"),
        (22, "XXII"),
        (30, "XXX"),
        (35, "XXXV"),
        (40, "XL"),
        (45, "XLV"),
        (50, "L"),
        (55, "LV"),
        (60, "LX"),
        (69, "LXIX"),
        (70, "LXX"),
        (80, "LXXX"),
        (90, "XC"),
        (99, "XCIX"),
        (100, "C"),
        (101, "CI"),
        (111, "CXI"),
        (121, "CXXI"),
        (134, "CXXXIV"),
        (156, "CLVI"),
        (200, "CC"),
        (300, "CCC"),
        (400, "CD"),
        (500, "D"),
        (600, "DC"),
        (700, "DCC"),
        (800, "DCCC"),
        (900, "CM"),
        (912, "CMXII"),
        (998, "CMXCVIII"),
        (999, "CMXCIX"),
        (1000, "M"),
        (1001, "MI"),
        (1101, "MCI"),
    ]
)
def test_convert(arabic_digit, roman_numeral):
    assert RomanNumeral().convert(arabic_digit) == roman_numeral
