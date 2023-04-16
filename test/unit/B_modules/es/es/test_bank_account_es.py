"""
Test Spanish Bank Accounts
"""

from pii_extract_plg_regex.modules.es.es.bank_account import PII_TASKS
from taux.taskproc import check_tasks


TESTCASES = [
    # A valid bank account number
    (
        "Código cuenta cliente: 2085 8720 60 1902070563",
        "Código cuenta cliente: <BANK_ACCOUNT:2085 8720 60 1902070563>"
    ),
    # No spaces
    (
        "Código cuenta cliente: 20858720601902070563",
        "Código cuenta cliente: <BANK_ACCOUNT:20858720601902070563>"
    ),
    # Invalid bank account numbers
    (
        "Código cuenta cliente: 2085 8720 44 1902070563",
        "Código cuenta cliente: 2085 8720 44 1902070563"
    ),
    (
        "Código cuenta cliente: 2085 8720 60 19020705633",
        "Código cuenta cliente: 2085 8720 60 19020705633"
    ),
    (
        "Código cuenta cliente: 2085 8720 60 1902070563.3",
        "Código cuenta cliente: 2085 8720 60 1902070563.3"
    ),
    (
        "Código cuenta cliente: 2,2085 8720 60 1902070563",
        "Código cuenta cliente: 2,2085 8720 60 1902070563"
    )
]


def test10_bank_account():
    defaults = {"lang": "es", "country": "es"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
