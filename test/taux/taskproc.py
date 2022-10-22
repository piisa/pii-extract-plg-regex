
from operator import attrgetter
from itertools import chain

from typing import Dict, List, Tuple, Iterable

from pii_data.types import DocumentChunk, PiiEntity
from pii_extract.build.task import BasePiiTask
from pii_extract.build.parser import build_tasklist, TYPE_TASK_LIST
from pii_extract.load.task_collection import build_task


# -------------------------------------------------------------------------

def pii_build_tasks(tasks: TYPE_TASK_LIST, defaults: Dict = None):
    tl = build_tasklist(tasks, defaults)
    return [build_task(t) for t in tl]


def pii_detect(chunk: DocumentChunk,
               tasklist: List[BasePiiTask]) -> Iterable[PiiEntity]:
    return chain.from_iterable(t(chunk) for t in tasklist)


def pii_replace(pii_list: Iterable[PiiEntity], chunk: DocumentChunk):
    """
    Replace the PII values in a document chunk by an annotated version
           <PII-TYPE:VALUE>
    """
    output = []
    pos = 0
    doc = chunk.data
    for pii in sorted(pii_list, key=attrgetter('pos')):
        # Add all a pair (text-prefix, transformed-pii)
        f = pii.fields
        output += [doc[pos:pii.pos], f'<{f["type"]}:{f["value"]}>']
        pos = pii.pos + len(pii)
    # Reconstruct the document (including the last suffix)
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
    tlist = pii_build_tasks(taskdef, defaults)
    for tc in testcases:
        chunk = DocumentChunk('1', tc[0])
        pii = pii_detect(chunk, tlist)
        got = pii_replace(pii, chunk)
        yield tc[1], got.data
