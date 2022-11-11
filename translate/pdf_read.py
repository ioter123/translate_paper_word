import pdfminer
from pdfminer.high_level import extract_text
import os, re
import pandas as pd
import unicodedata
import tika
from tika import parser

path_dir = 'paper_pdf/jpart2021'
file_list = os.listdir(path_dir)
pdf_list = []
for file in file_list:

    PDF_Parse = parser.from_file(path_dir+"/" + file)
    print(file)
    content = unicodedata.normalize("NFKD", PDF_Parse['content']).split("\n\n")

    break