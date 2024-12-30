from typing import List

import spacy
nlp = spacy.load("en_core_web_lg")

from util.logg import logInfo, logError

class DotController:

    # basic processes will be here, but exposed to Piper

    # found out about spacy KB, will do groclaCy KB
    def __init__(self):
        logInfo("just Nothing rn => idk")

    def prepText(self, text: str) -> str:
        logInfo("prepping text")

        proText = nlp(text)

        supText = [token.lemma_ for token in proText
                   if not token.is_stop and not token.is_punct]

        return " ".join(supText)

    def getEnts(self, text: str) -> List[str]:
        logInfo("ents extraction")

        proText = nlp(text)

        ents = []

        for ent in proText.ents:
            ents.append(\
                    f"entity: {ent.text}, label: {ent.label_}"
            )

        return ents

    def analyzeStruct(self, text: str):
        logInfo("struct anal vol2. electric boogaloo")

        proText = nlp(text)

        anal = []

        for sent in proText.sents:
            struct = {
                "text": sent.text,
                "rootVerb": None,
                "subjects": [],
                "objects": [],
                "modifiers": []
            }

            for token in sent:
                if token.dep_ == "ROOT":
                    struct["rootVerb"] = token.text
                elif "subj" in token.dep_:
                    struct["subjects"].append(token.text)
                elif "obj" in token.dep_:
                    struct["objects"].append(token.text)
                elif token.dep_ in ["amod", "advmod"]:
                    struct["modifiers"].append(token.text)

            anal.append(struct) # all that junk, all that junk

        return anal 


    async def processMessage(self, message: str):
        logInfo("thinking rn")

        # alright, spacy time

        # remove stops and puncts

        spacedOut = self.prepText(message)

        logInfo("spaced out text:\n" + spacedOut)

        # get ents

        spacedOutEnts = self.getEnts(spacedOut)

        logInfo("ents in the pants:\n" + str(spacedOutEnts))

        # anal time

        spacedAnal = self.analyzeStruct(message) # and spaced anal 2.5

        for anal in spacedAnal:
            logInfo(\
                    f"""
                    spaced anal: {anal["text"]}
                    root verbs: {anal["rootVerb"]}
                    subjects: {anal["subjects"]}
                    objects anal: {anal["objects"]}
                    modifiers: {anal["modifiers"]}
                    """
            )

        # lmao this ain't nothing but not a thing... yet?

        # tho.. 5 sums with ents and pants stays in "working memory" (short term)
        # the rest gets placed as per weights in the ltm mem table

        # every associated memdot that is recalled gets weighted and tagged and stored
        # rinse and repeat

        # gen memDot

        # currentMemDot = MemDot() 

        # generate ass's, summary

        # generate 1resps

        # resp 1resps

        # 
        # EmoteV
        #

        #
        # ThoughtU
        #

        #
        #
        #

        # sent1 -> [ass's..][summ]

        # sent2
