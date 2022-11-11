import os, re
import pandas as pd
import numpy as np
import pdfminer
from pdfminer.high_level import extract_text
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import pymysql
import pymysql.cursors
from nltk.tokenize import TreebankWordTokenizer

# 논문 pdf 읽어오기
path_dir = 'paper_pdf'
file_list = os.listdir(path_dir)
pdf_list = []
for file in file_list:
    pdf_list.append(re.compile("[^a-zA-Z]+").sub(" ", extract_text(path_dir+'/'+file).replace("\n", " ")))

# nltk 데이터 다운로드 : 한번만 실행
#nltk.download()

# 형태소 분석
stop_word_eng = set(stopwords.words('english'))
#ps_stemmer = PorterStemmer() # 어근 동일화
lemmatizer = WordNetLemmatizer() # 표제어 추출
#token = RegexpTokenizer('[\w]+')
#results = [nltk.tokenize.word_tokenize(pdf) for pdf in pdf_list]
results = [nltk.tokenize.TreebankWordTokenizer(pdf) for pdf in pdf_list]
#results = [token.tokenize(pdf) for pdf in pdf_list]
middle_result= [r for i in results for r in i]
final_result = [lemmatizer.lemmatize(i) for i in middle_result if not i in stop_word_eng] # 불용어 제거
word_tag = nltk.tag.pos_tag(final_result)
word_tag_df = pd.DataFrame(word_tag, columns=['word','tag'])

# 단어/태그 별 갯수 카운팅
word_tag_df['count']=1
word_tag_count = word_tag_df.groupby(['word','tag']).count()
word_tag_count.reset_index(drop=False, inplace=True)
word_tag_count.sort_values('count', ascending=False, inplace=True)
word_tag_count['id'] = [i for i in range(word_tag_count.shape[0])]
word_tag_count = word_tag_count[['id','word','tag','count']]
word_tag_count.to_excel('testdb.xlsx', index=False)


"""
# n-gram 사전 개발
from nltk.collocations import BigramAssocMeasures
from nltk.collocations import TrigramAssocMeasures
from nltk.metrics.association import QuadgramAssocMeasures
from nltk.collocations import BigramCollocationFinder
from nltk.collocations import TrigramCollocationFinder
from nltk.collocations import QuadgramCollocationFinder
from collections import Counter


ngram = [(BigramAssocMeasures(),BigramCollocationFinder),
         (TrigramAssocMeasures(),TrigramCollocationFinder),
         (QuadgramAssocMeasures(),QuadgramCollocationFinder)]

#print(middle_result)
founds_from_4measure = []
for measure, finder in ngram:
    finder = finder.from_words(middle_result)    # 단어 찾기
    founds = finder.nbest(measure.pmi, 100)       # pmi - 상위 10개 추출
    founds += finder.nbest(measure.chi_sq, 100)   # chi_sq - 상위 10개 추출
    founds += finder.nbest(measure.mi_like, 100)  # mi_like - 상위 10개 추출
    founds += finder.nbest(measure.jaccard, 100)  # jaccard - 상위 10개 추출

    founds_from_4measure += founds

#print(founds_from_4measure)
collocations = [' '.join([w for w in collocation]) for collocation in founds_from_4measure]
collocations = [(w,f) for w,f in Counter(collocations).most_common() if f > 2]
#print(collocations)
"""

# mysql 저장
host = 'localhost'
port = 3306
username = 'root'
password = 'hai8993!'
db = 'paper_bigdata_db'


# library import : sqlalchemy
from sqlalchemy import create_engine

# engine : AWS connecting
engine = create_engine("mysql+pymysql://root:hai8993!@localhost:3306/paper_bigdata_db?charset=utf8", encoding='utf-8')
conn = engine.connect()

# to_sql (user : Dataframe / name = tablename, con = connection)
word_tag_count.to_sql(name="word_count_table", con=engine, if_exists='replace', index=False)
conn.close()