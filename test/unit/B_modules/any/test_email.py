"""
Test email addresses
"""

import pytest

from pii_data.types import PiiEnum
from pii_data.types.doc.localdoc import SequenceLocalSrcDocument
from pii_extract.api import PiiProcessor

from taux.auxpatch import patch_entry_points
from taux.taskproc import check_tasks

# Import the task descriptor
from pii_extract_plg_regex.modules.any.email import PII_TASKS


TESTCASES = [
    # A valid email address
    (
        "My email is anyone@whatever.com.",
        "My email is <EMAIL_ADDRESS:anyone@whatever.com>."
    ),
    # An invalid email address
    (
        "My email is anyone@whatever.",
        "My email is anyone@whatever."
    ),
    # Several email addresses
    (
        "I need to email hUEIOA.Ajfd@poop.poop.poo, MegMeg@aol, and जॉन@माइक्रोसॉफ्टहै.कॉम.",
        "I need to email <EMAIL_ADDRESS:hUEIOA.Ajfd@poop.poop.poo>, MegMeg@aol, and <EMAIL_ADDRESS:जॉन@माइक्रोसॉफ्टहै.कॉम>."
    ),
    # Similar to emails, but not quite
    (
        "No emails to see here: dusk-network/menu@4.6.12 and //cdn.jsdelivr.net/gh/konpa/devicon@master/devicon.min.css",
        "No emails to see here: dusk-network/menu@4.6.12 and //cdn.jsdelivr.net/gh/konpa/devicon@master/devicon.min.css"
    ),
    # Embedded emails
    (
        "email is <zcwzzwc@uwaterloo.ca>",
        "email is <<EMAIL_ADDRESS:zcwzzwc@uwaterloo.ca>>"
    ),
    (
        """<p><i class="fa fa-envelope-o"></i> <a href="mailto:okidoki@gmail.com">""",
        """<p><i class="fa fa-envelope-o"></i> <a href="mailto:<EMAIL_ADDRESS:okidoki@gmail.com>">"""
    )
]


# -----------------------------------------------------------------------

@pytest.fixture
def fixture_entry_points(monkeypatch):
    patch_entry_points(monkeypatch)


def test10_email():
    """
    Test task processing, directly instantiating the task
    """
    defaults = {"lang": "any", "country": "any"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g


def test20_email_stats(fixture_entry_points):
    """
    Test stats on task processing, launching through a PiiProcessor
    """
    obj = PiiProcessor()
    obj.build_tasks("any", pii=PiiEnum.EMAIL_ADDRESS)
    doc = SequenceLocalSrcDocument(chunks=[c[0] for c in TESTCASES])
    obj(doc)
    assert obj.get_stats() == {"num": {"calls": 1, "entities": 5},
                               "entities": {"EMAIL_ADDRESS": 5}}
