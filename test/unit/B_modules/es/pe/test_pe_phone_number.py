"""
Test Peruvian phone numbers
"""

from pii_extract_plg_regex.modules.es.pe.phone_number import PII_TASKS
from taux.taskproc import check_tasks


TESTCASES = [
    # Valid phone number
    (
        "Los teléfonos son 1 234 56 78 y 933 123 567",
        "Los teléfonos son <PHONE_NUMBER:1 234 56 78> y <PHONE_NUMBER:933 123 567>"
    ),
    (
        "Llamé al 43 76 43 12",
        "Llamé al <PHONE_NUMBER:43 76 43 12>"
    ),
    (
        "Tf. 53 31 24 31",
        "Tf. <PHONE_NUMBER:53 31 24 31>"
    ),
    # No spaces
    (
        "Los teléfonos son 12345678 y 933123567",
        "Los teléfonos son <PHONE_NUMBER:12345678> y <PHONE_NUMBER:933123567>"
    ),
    # Missing context
    (
        "Los números son 12345678 y 933123567",
        "Los números son 12345678 y 933123567"
    ),
    # Invalid numbers
    (
        "Tf. 111 3124312",
        "Tf. 111 3124312"
    ),
    (
        "Tf. 78 34 12 42",
        "Tf. 78 34 12 42"
    ),
    (
        "El teléfono es +34983453999",
        "El teléfono es +34983453999"
    )
]


def test10_phone_number():
    defaults = {"lang": "es", "country": "pe"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
