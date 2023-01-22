"""
Test Argentinian CUIL
"""

from pii_extract_plg_regex.modules.es.ar.cuil import PII_TASKS
from taux.taskproc import check_tasks


TESTCASES = [
    # Valid CUIL
    (
        "El CUIL es 20-08490848-8",
        "El CUIL es <GOV_ID:20-08490848-8>"
    ),
    # Invalid CUIL
    (
        "El CUIL es 20-08490848-7",
        "El CUIL es 20-08490848-7"
    ),
    (
        "El CUIL es 20-08490848-88",
        "El CUIL es 20-08490848-88"
    )
]


def test10_govid():
    defaults = {"lang": "es", "country": "ar"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
