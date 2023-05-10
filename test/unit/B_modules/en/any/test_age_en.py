"""
Test international phone numbers
"""

from taux.taskproc import check_tasks

# Import the task descriptor
from pii_extract_plg_regex.modules.en.any.age import PII_TASKS

TESTCASES = [
    # Standard phone number
    ("age: 2 years",
     "age: <AGE:2> years"),
    ("I'm 27 years old",
     "I'm <AGE:27> years old"),
    ("Your age is 65.",
     "Your age is <AGE:65>."),
    ("A 1-year-old child",
     "A <AGE:1>-year-old child"),
    
]


def test10_age():
    """
    Test task processing, directly instantiating the task
    """
    defaults = {"lang": "any", "country": "any"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
