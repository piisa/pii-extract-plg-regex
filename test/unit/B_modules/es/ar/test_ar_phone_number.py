"""
Test Argentinian phone numbers
"""

from pii_extract_plg_regex.modules.es.ar.phone_number import PII_TASKS
from taux.taskproc import check_tasks


TESTCASES = [
    # Valid phone number
    (
        "Los teléfonos son 11 1234-5678 y 341 523-4567",
        "Los teléfonos son <PHONE_NUMBER:11 1234-5678> y <PHONE_NUMBER:341 523-4567>"
    ),
    (
        "Llamé al 9 362 547-3541",
        "Llamé al <PHONE_NUMBER:9 362 547-3541>"
    ),
    (
        "Tf. 3541 15 52-3456",
        "Tf. <PHONE_NUMBER:3541 15 52-3456>"
    ),
    # No spaces
    (
        "Los teléfonos son 1112345678 y 3415234567",
        "Los teléfonos son <PHONE_NUMBER:1112345678> y <PHONE_NUMBER:3415234567>"
    ),
    # Missing context
    (
        "Los números son 1112345678 y 3415234567",
        "Los números son 1112345678 y 3415234567"
    ),
    # Invalid numbers
    (
        "El teléfono es 1234567890",
        "El teléfono es 1234567890"
    )
]


def test10_phone_number():
    defaults = {"lang": "es", "country": "ar"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
