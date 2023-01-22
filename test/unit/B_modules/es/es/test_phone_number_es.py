"""
Test Spanish Phone Numbers
"""

from pii_extract_plg_regex.modules.es.es.phone_number import PII_TASKS
from taux.taskproc import check_tasks


TESTCASES = [
    # Valid phone number
    (
        "Los teléfonos son 983 45 65 72 y 635 576 281",
        "Los teléfonos son <PHONE_NUMBER:983 45 65 72> y <PHONE_NUMBER:635 576 281>"
    ),
    (
        "Llamada al 016 en la lista",
        "Llamada al <PHONE_NUMBER:016> en la lista"
    ),
    (
        "Tf. 913 444 111",
        "Tf. <PHONE_NUMBER:913 444 111>"
    ),
    # Same with no spaces
    (
        "Los teléfonos son 983456572 y 635576281",
        "Los teléfonos son <PHONE_NUMBER:983456572> y <PHONE_NUMBER:635576281>"
    ),
    # Missing context
    (
        "Los números son 983456572 y 635576281",
        "Los números son 983456572 y 635576281"
    ),
    # Invalid numbers
    (
        "El teléfono es 123456789",
        "El teléfono es 123456789"
    )
]


def test10_phone_number():
    defaults = {"lang": "es", "country": "es"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
