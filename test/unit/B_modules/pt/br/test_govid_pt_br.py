"""
Test Brazilian CPF
"""

from pii_extract_plg_regex.modules.pt.br.cpf import PII_TASKS
from taux.taskproc import check_tasks

TESTCASES = [
    # A valid CPF
    ("O número do CPF é 263.946.533-30",
     "O número do CPF é <GOV_ID:263.946.533-30>"),
    # An invalid CPF
    ("O número do CPF é 000.000.000-12",
     "O número do CPF é 000.000.000-12"),
]


def test10_cpf():
    defaults = {"lang": "pt", "country": "br"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
    
