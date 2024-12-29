from dataclasses import dataclass
from typing import Dict, List

@dataclass
class MemDot:

    ents: List[str]# basic idea.. let spacy tag stuff, and then weight them by context
    
    structDots: Dict[str, str]

    summas: List[str]

    # bam

    # bom

    # store and recall based on those weights, summarize and recontextualizzler

    # [0.1][0.02][0.69][0.24][0.48][0.151][0.62]

    # do some ops and add a bit randomness to the prompt

    # tho always keep the prompt at the optimum size: context rich tho ready for more

    # ps. prompt -> stm <-> ltm -> response

    # memory is a flat earth
