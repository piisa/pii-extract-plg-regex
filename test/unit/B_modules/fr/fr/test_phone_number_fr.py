"""
Test FR phone numbers
"""

from taux.taskproc import check_tasks

from pii_extract_plg_regex.modules.fr.fr.phone_number import PII_TASKS

TESTCASES = [
    # Valid phone number
    (
        "Les numéros de téléphone sont 09 83 45 65 72 et 06 35 57 62 81",
        "Les numéros de téléphone sont <PHONE_NUMBER:09 83 45 65 72> et <PHONE_NUMBER:06 35 57 62 81>",
    ),
    ("Tél. 06 12 34 56 78", "Tél. <PHONE_NUMBER:06 12 34 56 78>"),
    # Same with no spaces
    (
        "Les téléphones sont 06 12345678 et 0512345678",
        "Les téléphones sont <PHONE_NUMBER:06 12345678> et <PHONE_NUMBER:0512345678>",
    ),
    # Missing context
    (
        "Les numéros sont 0983456572 et 0635576281",
        "Les numéros sont 0983456572 et 0635576281",
    ),
    # Invalid numbers
    ("Le numéro de téléphone est 123456789", "Le numéro de téléphone est 123456789"),
]


def test10_phone_number():
    defaults = {"lang": "fr", "country": "fr"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
