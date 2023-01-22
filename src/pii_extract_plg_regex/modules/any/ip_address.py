"""
Detection of IP addresses
"""

from pii_data.types import PiiEnum


_IP_PATTERN = r"""
     \b
     (?: (?: 25[0-5] | 2[0-4][0-9] | [01]?[0-9][0-9]? ) \. ){3}
     (?: 25[0-5] | 2[0-4][0-9] | [01]?[0-9][0-9]?)
     \b
"""


PII_TASKS = [
    {
        "class": "regex",
        "task": _IP_PATTERN,
        "name": "ip address",
        "doc": "match IP addresses, with context",
        "pii": PiiEnum.IP_ADDRESS,
        "context": {"value": "ip", "type": "word", "width": 16},
    }
]
