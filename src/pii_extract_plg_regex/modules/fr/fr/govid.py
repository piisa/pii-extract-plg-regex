"""
French Goverment-issued IDs:
  - NIR (Numero d'Inscription au Repertoire national d'identification des
    personnes physiques) aka INSEE code
  - NIF (Numéro d'Immatriculation Fiscale or Numéro d'Identification Fiscale)
    aka SPI (Simplification des Procédures d'Identification)
"""

import re

from typing import Iterable

from stdnum.fr import nif, nir

from pii_data.types import PiiEnum, PiiEntity
from pii_data.types.doc import DocumentChunk
from pii_extract.build.task import BaseMultiPiiTask


# Regex for NIR & NIF
_NIR_PATTERN = r"""
  (?<! \d )
  [12] \ ?                                    # male/female
  \d{2} \ ?                                   # year of birth
  (?: 0[1-9] | 1[0-2]  | 2\d ) \ ?            # month of birth
  (?: \d{2}\ ?\d{3} | \d[A-Z]\ ?\d{3} ) \ ?   # COG
  \d{3} \ ? \d{2}                             # order number + control key
  \b
"""

_NIF_PATTERN = r"""
  (?<! \d )
  [0123]\d
  (?: \d{11} |
      \  \d{2} \  \d{3} \  \d{3} \  \d{3}
  )
  \b
"""


class FrenchNirNif(BaseMultiPiiTask):
    """
    French Government-issued identifiers:
     - NIR (Numero d'Inscription au Repertoire national d'identification des
       personnes physiques) aka INSEE code
     - NIF (Numéro d'Immatriculation Fiscale or Numéro d'Identification
       Fiscale) aka SPI (Simplification des Procédures d'Identification)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regexes
        self.nir = re.compile(_NIR_PATTERN, flags=re.X)
        self.nif = re.compile(_NIF_PATTERN, flags=re.X)


    def find(self, chunk: DocumentChunk) -> Iterable[PiiEntity]:
        """
        Find & validate instances of either NIR or NIF
        """
        info_nir, info_nif = self.pii_info

        # NIR
        for item in self.nir.finditer(chunk.data):
            item_value = item.group()
            if nir.is_valid(item_value):
                yield PiiEntity(info_nir, item_value, chunk.id, item.start())

        # NIF
        for item in self.nif.finditer(chunk.data):
            item_value = item.group()
            if nif.is_valid(item_value):
                yield PiiEntity(info_nif, item_value, chunk.id, item.start())


# ---------------------------------------------------------------------

# Task descriptor
PII_TASKS = {
    "class": "PiiTask",
    "task": FrenchNirNif,
    "name": "Fench NIR & NIF numbers",
    "pii": [
        {
            "type": PiiEnum.GOV_ID,
            "subtype": "French NIR",
            "method": "regex,checksum"
        },
        {
            "type": PiiEnum.GOV_ID,
            "subtype": "French NIF",
            "method": "weak-regex"
        }
    ]
}
