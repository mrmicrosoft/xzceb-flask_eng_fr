import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

version = "2018-05-01"

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url('{url}')

def englishToFrench(englishText):
    """
    English to French Translator
    """
    frenchText = language_translator.translate(
        text=englishText, model_id='en-fr').get_result()
    return frenchText.get("translations")[0].get("translation")

def frenchToEnglish(frenchText):
    """
    French to English Translator
    """
    englishText = language_translator.translate(
        text=frenchText, model_id='fr-en').get_result()
    return englishText.get("translations")[0].get("translation")
