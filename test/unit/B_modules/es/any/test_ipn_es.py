"""
Test international phone numbers
"""

from pii_extract_plg_regex.modules.es.any.international_phone_number import PII_TASKS
from pii_extract.defs import LANG_ANY
from taux.taskproc import check_tasks

TESTCASES = [
    # Standard phone number
    ("teléfono: +34 983 453 999",
     "teléfono: <PHONE_NUMBER:+34 983 453 999>"),
    ("tf. +34983453999",
     "tf. <PHONE_NUMBER:+34983453999>"),
    ("numero de telefono +34983453999",
     "numero de telefono <PHONE_NUMBER:+34983453999>"),
    # An invalid country code
    ("teléfono: +99 983 453 999", "teléfono: +99 983 453 999"),
    # No valid contexts
    ("número: +34983453999", "número: +34983453999"),
    ("tff +34983453999", "tff +34983453999"),
]


def test10_phone_number():
    defaults = {"lang": "es", "country": LANG_ANY}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
