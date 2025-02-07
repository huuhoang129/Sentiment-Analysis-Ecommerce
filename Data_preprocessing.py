import demoji as emoji
import re

def remove_emo(text):
    emo = emoji.replace(text, '')
    return emo

def remove_urls(text):
    urls = re.sub(r'http/S+', '', text)
    return urls

def remove_email_and_username(text):
    user = re.sub(r'@\w+', '', text)
    email = re.sub(r'\b[A-Za-z0-9._%+-]@[A-Za-z0-9.-].[A-Z|a-z{2,}]\b')
    return user, email

def remove_punctuation(text):
    punc = re.sub(r'[\w\s]', '', text)
    return punc

def lower_case (text):
    lower_text = text.lower()
    return lower_text