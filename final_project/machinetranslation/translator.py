import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv
load_dotenv()

apikey = "x90f_qTiL8fFweD7CzMHKP6IXR7QpFfuINJDpRClNDN5"
url = "https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/e74d024a-e672-44dd-badf-b35410336d26"


authenticator = IAMAuthenticator(apikey=apikey)
language_translator = LanguageTranslatorV3(version='2021-02-18',authenticator=authenticator)
language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    This function translates English text to French Test
    """
    french_text = language_translator.translate(
        text = english_text,
        model_id='en-fr').get_result()
    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    """
    This function translates English text to French Test
    """
    english_text = language_translator.translate(
        text = french_text,
        model_id= 'fr-en').get_result()
    return english_text['translations'][0]['translation']

english_to_french_result = english_to_french(["Hello! How are you madam?"])
french_to_english_result = french_to_english(["Bonjour"])
print("Enlish to French:", english_to_french_result)
print("French to English:", french_to_english_result)