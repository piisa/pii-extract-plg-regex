"""
Some utilities to help when testing tasks
"""

from operator import attrgetter
from itertools import chain

from typing import Dict, List, Tuple, Iterable

from pii_data.types import PiiEntity
from pii_data.types.doc import DocumentChunk
from pii_extract.build.task import BasePiiTask
from pii_extract.gather.parser import parse_task_descriptor
from pii_extract.gather.parser.defs import TYPE_TASKD
from pii_extract.gather.collection.sources.utils import RawTaskDefaults
from pii_extract.build.build import build_task


# -------------------------------------------------------------------------

def pii_build_tasks(tasks: Iterable[TYPE_TASKD],
                    defaults: Dict = None) -> Iterable[BasePiiTask]:
    """
    Build a list of task objects from its raw descriptors
    """
    if isinstance(tasks, dict):
        tasks = [tasks]
    reformat = RawTaskDefaults(defaults, normalize=True)
    for tdesc in reformat(tasks):
        tdef = parse_task_descriptor(tdesc)
        #print("TDESC", tdesc, "TDEF", tdef, sep="\n")
        yield build_task(tdef)


def pii_detect(chunk: DocumentChunk,
               tasklist: List[BasePiiTask]) -> Iterable[PiiEntity]:
    """
    Perform PII detection
    """
    return chain.from_iterable(t(chunk) for t in tasklist)


def pii_replace(pii_list: Iterable[PiiEntity], chunk: DocumentChunk):
    """
    Replace the PII values in a document chunk by an annotated version
    <PII-TYPE:VALUE>
    """
    doc = chunk.data
    pos = 0
    output = []

    # Compose all substitutions
    for pii in sorted(pii_list, key=attrgetter('pos')):
        f = pii.fields
        output += [doc[pos:pii.pos], f'<{f["type"]}:{f["value"]}>']
        pos = pii.pos + len(pii)

    # Reconstruct the fulldocument (including the last suffix)
    doc = "".join(output) + doc[pos:]
    return DocumentChunk(chunk.id, doc, chunk.context)


# ----------------------------------------------------------------------

def check_tasks(taskdef: List, defaults: Dict,
                testcases: List[Tuple[str, str]]) -> Iterable[Tuple[str, str]]:
    """
      Test a task implementation against testcases
        :param taskdef: a list of task definitions
        :param defaults: defaults for task definitions
        :param testcases: a list of pairs (source-text, replaced-text)
    """
    tlist = list(pii_build_tasks(taskdef, defaults))
    for tc in testcases:
        chunk = DocumentChunk('1', tc[0])
        pii = pii_detect(chunk, tlist)
        got = pii_replace(pii, chunk)
        yield tc[1], got.data
