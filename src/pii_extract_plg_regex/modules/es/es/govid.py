"""
Spanish Government-issued IDs:
  - DNI (Documento Nacional de Identidad)
  - NIE (Número de Identificación de Extranjero)
"""

import re

from typing import Iterable

from stdnum.es import dni, nie

from pii_data.types import PiiEnum, PiiEntity
from pii_data.types.doc import DocumentChunk
from pii_extract.build.task import BaseMultiPiiTask

# Regex for DNI & NIE
_DNI_PATTERN = r"(?: \b | (?<= DNI) ) \d{6,8} -? [A-KJ-NP-TV-Z] \b"
_NIE_PATTERN = r"(?: \b | (?<= NIE) ) [X-Z] \d{7} -? [A-KJ-NP-TV-Z] \b"


class Spanish_DNI_NIE(BaseMultiPiiTask):
    """
    Spanish Government-issued identifiers: Documento Nacional de Identidad (DNI) & Número de Identificación de Extranjero (NIE)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regexes
        self.dni = re.compile(_DNI_PATTERN, flags=re.X)
        self.nie = re.compile(_NIE_PATTERN, flags=re.X)


    def find(self, chunk: DocumentChunk) -> Iterable[PiiEntity]:
        """
        Find & validate instances of either DNI or NIE
        """
        info_dni, info_nie = self.pii_info

        # DNI
        for item in self.dni.finditer(chunk.data):
            item_value = item.group()
            if dni.is_valid(item_value):
                yield PiiEntity(info_dni, item_value, chunk.id, item.start())

        # NIE
        for item in self.nie.finditer(chunk.data):
            item_value = item.group()
            if nie.is_valid(item_value):
                yield PiiEntity(info_nie, item_value, chunk.id,item.start())


# ---------------------------------------------------------------------

# Task descriptor
PII_TASKS = {
    "class": "PiiTask",
    "task": Spanish_DNI_NIE,
    "name": "Spanish DNI and NIE numbers",
    "pii": {
        "type": PiiEnum.GOV_ID,
        "subtype": ["Spanish DNI", "Spanish NIE"],
        "method": "regex,checksum"
    }
}
