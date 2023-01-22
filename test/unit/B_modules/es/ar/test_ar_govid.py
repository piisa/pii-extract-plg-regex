"""
Test Argentinian DNI
"""

from pii_extract_plg_regex.modules.es.ar.govid import PII_TASKS
from taux.taskproc import check_tasks


TESTCASES = [
    # Valid DNI
    (
        "El DNI es 11.123.567",
        "El DNI es <GOV_ID:11.123.567>"
    ),
    (
        "El DNI es 11123567",
        "El DNI es <GOV_ID:11123567>"
    ),
    (
        "El DNI es 1.123.567",
        "El DNI es <GOV_ID:1.123.567>"
    ),
    # Invalid DNI
    (
        "El DNI es 112.123.567",
        "El DNI es 112.123.567"
    ),
    # Missing context
    (
        "El número es 11.123.567",
        "El número es 11.123.567"
    )
]


def test10_govid():
    defaults = {"lang": "es", "country": "ar"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
