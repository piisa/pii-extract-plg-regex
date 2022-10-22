"""
Test international phone numbers
"""

from pii_extract_plg_regex.modules.en.any.international_phone_number import PII_TASKS
from taux.taskproc import check_tasks

TESTCASES = [
    # Standard phone number
    ("phone number: +34 983 453 999",
     "phone number: <PHONE_NUMBER:+34 983 453 999>"),
    ("phone number: +34983453999",
     "phone number: <PHONE_NUMBER:+34983453999>"),
    ("ph. +34983453999",
     "ph. <PHONE_NUMBER:+34983453999>"),
    # An invalid country code
    ("phone number: +99 983 453 999", "phone number: +99 983 453 999"),
    # No valid contexts
    ("number: +34983453999", "number: +34983453999"),
    ("phonograph +34983453999", "phonograph +34983453999"),
]


def test10_int_phone_number():
    defaults = {"lang": "any", "country": "any"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
