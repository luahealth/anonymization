from flair.data import Sentence
from flair.models import SequenceTagger
import nltk
import re
import truecase
from langdetect import detect
import ctranslate2
import sentencepiece as spm
import urllib.request
import os

try:
   import en_core_web_lg
except ModuleNotFoundError:
    import spacy.cli
    spacy.cli.download("en_core_web_lg")
    import en_core_web_lg

nlp = en_core_web_lg.load()

if not os.path.isfile('ct2_model/model.bin'):
    urllib.request.urlretrieve("https://server1.nlp.insight-centre.org/pp/model.bin", "ct2_model/model.bin")


nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('maxent_ne_chunker', quiet=True)
nltk.download('words', quiet=True)

tagger = SequenceTagger.load("flair/ner-english")

dicti = {}
translator = ctranslate2.Translator("ct2_model/")
sp_estl = spm.SentencePieceProcessor("ct2_model/spm.estl.model")
sp_en = spm.SentencePieceProcessor("ct2_model/spm.en.model")

def lang_id(string: str):
    """
    language idetigfcation using ???
    :param string: string used to detected language
    :return: detected language id
    """
    detect_language = detect(string)
    return detect_language

def spacy_ano(string: str):
    """
    named entity recognition with spacy
    :param string: string used to extract the named entities
    :return: populating dictionary with NEs extracted by spacy
    """
    text = nlp(string)
    for X in text.ents:
        dicti[X.text.lower()] = X.label_


def nltk_ano(string: str):
    """
    named entity recognition with nltk
    :param string: string used to extract the named entities
    :return: populating dictionary with NEs extracted by nltk
    """
    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(string))):
        if hasattr(chunk, 'label'):
            label = chunk.label()
            lex = " ".join(c[0] for c in chunk)
            dicti[lex.lower()] = label


def flair_ano(string: str):
    """
    named entity recognition with flair
    :param string: string used to extract the named entities
    :return: populating dictionary with NEs extracted by flair
    """
    sentence = Sentence(string)
    tagger.predict(sentence)
    for entity in sentence.get_spans('ner'):
        dicti[entity.text.lower()] = entity.get_label("ner").value


def read_company_thesaurus(thesaurus: str):
    """
    fuction to construct dictionary with company names
    :param thesaurus: path to thesaurus file with company names
    :return: dictionary
    """
    with open(thesaurus) as thesaurus_file:
        for line in thesaurus_file.readlines():
            dicti[line.replace('\n', '').lower()] = "COMP"

def do_translation(string: str):
    """
    translation module
    :param string: string to be translated
    :return: translated text
    """
    input_tokens = sp_estl.encode(string, out_type=str)
    results = translator.translate_batch([input_tokens])
    output_tokens = results[0].hypotheses[0]
    output_text = sp_en.decode(output_tokens)
    return output_text

def main_ano(string: str, thesaurus: str):
    """
    main function for initialising named entity recognition
    :param string: string used to extract the named entities
    :param thesaurus: path to company names
    :return: dictionary with all NEs
    """

    read_company_thesaurus(thesaurus)


    # string = re.sub(r'htt\S+', '', string)
    m = re.search(r'\w+$', string)
    if m is not None:
        string = string + "."

    lowerstring = ""


    string = re.sub(r'\S*@\S*\s?|http\S+|www\S+|[s]ftp\S+', '', string)

    if re.search('[a-zA-Z]', string):
        output_text = string
        if (not (lang_id(string)) and (lang_id(string) != "en")): output_text = (do_translation(string))

        string_tc = truecase.get_true_case(output_text)

        spacy_ano(string_tc)
        nltk_ano(string_tc)
        flair_ano(string_tc)

        lowerstring = string_tc.lower()

        for key in dicti:
            lowerstring = re.sub(r"\b%s\b" % key, dicti[key], lowerstring)

        pattern = r'[0-9]'
        lowerstring = re.sub(pattern, "X", lowerstring)

    return lowerstring
