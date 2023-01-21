"""
Test Argentinian phone numbers
"""

from pii_extract_plg_regex.modules.es.mx.phone_number import PII_TASKS
from taux.taskproc import check_tasks


TESTCASES = [
    # Valid phone number
    (
        "Los teléfonos son 55 12345678 y 333 1234567",
        "Los teléfonos son <PHONE_NUMBER:55 12345678> y <PHONE_NUMBER:333 1234567>"
    ),
    (
        "Llamé al 222 8764312",
        "Llamé al <PHONE_NUMBER:222 8764312>"
    ),
    (
        "Tf. 656 3124312",
        "Tf. <PHONE_NUMBER:656 3124312>"
    ),
    # No spaces
    (
        "Los teléfonos son 5512345678 y 3331234567",
        "Los teléfonos son <PHONE_NUMBER:5512345678> y <PHONE_NUMBER:3331234567>"
    ),
    # Missing context
    (
        "Los nùmeros son 5512345678 y 3331234567",
        "Los nùmeros son 5512345678 y 3331234567"
    ),
    # Invalid numbers
    (
        "Tf. 111 3124312",
        "Tf. 111 3124312"
    ),
    (
        "Tf. 656 31243121",
        "Tf. 656 31243121"
    )
]


def test10_phone_number():
    defaults = {"lang": "es", "country": "mx"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
