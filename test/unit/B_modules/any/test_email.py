"""
Test email addresses
"""

from pii_extract_plg_regex.modules.any.email import PII_TASKS
from taux.taskproc import check_tasks


TESTCASES = [
    # A valid email address
    (
        "My email is anyone@whatever.com.",
        "My email is <EMAIL_ADDRESS:anyone@whatever.com>.",
    ),
    # An invalid email address
    (
        "My email is anyone@whatever.",
        "My email is anyone@whatever.",
    ),
    # Several email addresses
    (
        "I need to email hUEIOA.Ajfd@poop.poop.poo, MegMeg@aol, and जॉन@माइक्रोसॉफ्टहै.कॉम.",
        "I need to email <EMAIL_ADDRESS:hUEIOA.Ajfd@poop.poop.poo>, MegMeg@aol, and <EMAIL_ADDRESS:जॉन@माइक्रोसॉफ्टहै.कॉम>."
    )
]


def test10_email():
    defaults = {"lang": "any", "country": "any"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
