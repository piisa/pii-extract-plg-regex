"""
Test Mexican CURP
"""

from pii_extract_plg_regex.modules.es.mx.curp import PII_TASKS
from taux.taskproc import check_tasks


TESTCASES = [
    # A valid CURP
    ("Mi número de CURP es PEPP700101HASRRD09",
     "Mi número de CURP es <GOV_ID:PEPP700101HASRRD09>"),
    # An invalid CURP
    (
        "Mi número de CURP es PEPP700101HASRRD01",
        "Mi número de CURP es PEPP700101HASRRD01",
    ),
]


def test10_curp():
    defaults = {"lang": "es", "country": "mx"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
