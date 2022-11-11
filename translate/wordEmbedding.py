from gensim.models.word2vec import Word2Vec
import os, re
import pandas as pd
from pdfminer.high_level import extract_text
from nltk.tokenize import word_tokenize, sent_tokenize

path_dir = 'paper_pdf'
file_list = os.listdir(path_dir)
snet_list = []
for file in file_list:
    temp_df = extract_text(path_dir+'/'+file)
    temp_df2 = temp_df.replace("\n", " ")
    #compile = re.compile("[^a-zA-Z]+")
    #temp_df3 = compile.sub(" ", temp_df2)
    contentText = re.sub('\([^)]*\)', '', temp_df2)
    # (배경음) 제거
    sentText = sent_tokenize(contentText)
    snet_list += sentText
#print(snet_list)

normalizedText = []
for sent in snet_list:
    tokens = re.sub("[^a-z0-9]+", " ", sent.lower())
    normalizedText.append(tokens)
result  = [word_tokenize(s) for s in normalizedText]
print(result)
model = Word2Vec(sentences=result, window = 5, min_count=5 , workers = 4 , sg = 0)
#print(model.wv.most_similar("policy"))
