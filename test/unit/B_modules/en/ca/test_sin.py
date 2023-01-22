"""
Test Canadian Social Insurance Number
"""

from taux.taskproc import check_tasks

from pii_extract_plg_regex.modules.en.ca.social_insurance_number import PII_TASKS

TESTCASES = [
    # A valid SIN
    ("SIN: 963-553-151",
     "SIN: <GOV_ID:963-553-151>"),
    # A valid SIN with spaces
    ("SIN: 339 892 317 number",
     "SIN: <GOV_ID:339 892 317> number"),
    # An invalid SIN (fails checksum)
    ("not a SIN: 123-456-781",
     "not a SIN: 123-456-781")
]


def test10_ssn():
    defaults = {"lang": "any", "country": "ca"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
