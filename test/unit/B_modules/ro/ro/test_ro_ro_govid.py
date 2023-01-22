"""
Test Romanian CNP
"""

from pii_extract_plg_regex.modules.ro.ro.govid import PII_TASKS
from taux.taskproc import check_tasks


TESTCASES = [
    # A valid CNP
    (
        "CNP: 1800101221144",
        "CNP: <GOV_ID:1800101221144>"
    ),
    # An invalid CNP
    (
        "CNP: 1800101221142",
        "CNP: 1800101221142"
    ),
]


def test10_curp():
    defaults = {"lang": "ro", "country": "ro"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
