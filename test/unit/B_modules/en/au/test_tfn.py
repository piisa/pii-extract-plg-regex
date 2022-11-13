"""
Test Australian Tax File Number
"""

from taux.taskproc import check_tasks

# Import the task descriptor
from pii_extract_plg_regex.modules.en.au.tfn import PII_TASKS

TESTCASES = [
    # A valid ABN
    ("tax file number: 963 553 151.",
     "tax file number: <GOV_ID:963 553 151>."),
    ("the tfn is: 123 456 782",
     "the tfn is: <GOV_ID:123 456 782>"),
    # TFN without spaces
    ("tax file number: 963553151.",
     "tax file number: <GOV_ID:963553151>."),
    # An invalid TFN
    ("not a TFN: 123 456 781", "not a TFN: 123 456 781"),
]


def test10_tfn():
    """
    Test task processing, directly instantiating the task
    """
    defaults = {"lang": "any", "country": "au"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
