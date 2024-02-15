"""
Author:
Carlo Lipizzi
Info at clipizzi@stevens.edu


This file will extract raw textual information from pdf files located
    in the working directory and save it in .txt files.

"""

from tika import parser
from datetime import datetime
import string

def extract_text_pdf(file_name, len):
    """
    Extract a text from a given pdf file (full path required)
    It returns a list with single words and a list of paragraphs
    """

    rawText = parser.from_file(file_name)

    text_parag = rawText['content'].splitlines()
    raw_parag_lst = []
    for parag in text_parag:
        if parag != '' and parag != ' ':
            para_clean = txt_clean(parag, len)
            raw_parag_lst. append(para_clean)
    return raw_parag_lst


def txt_clean(words_str, min_len):
    """
    Performs a first cleaning to a list of words.

    :param words_str: string of words
    :type: string
    :param min_len: minimum length of a word to be acceptable
    :type: integer
    :return: clean_words string of clean words
    :type: string

    """
    clean_words = ''
    for word in words_str.split(' '):
        word_l = word.lower()
        if len(word_l) > min_len:
            word_l1 = word_l.translate(str.maketrans('', '', string.punctuation))
            clean_words = clean_words + ' ' + word_l1.strip()

    return clean_words


'''
----------- Main
'''

print ('\n-Starting the pdf to txt conversion process-\n')
start_time = datetime.now()
print('--- starting time: {}'.format(start_time))
file_name_in = '2021-09-28-EU-Artificial-Intelligence-Act-The-European-Approach-to-AI'

min_word_len = 2
# extracting text from all .pdf files in the specified folder path
parag_in_lst = extract_text_pdf(file_name_in + '.pdf', min_word_len)

with open(file_name_in + '_parag.txt', "w") as outfile:
    outfile.write("\n".join(parag_in_lst))

print ('\n--- this is the end of the process ---\n')

print('--- total duration: {}'.format(datetime.now() - start_time))

