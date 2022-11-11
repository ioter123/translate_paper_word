from nltk.tokenize import word_tokenize
import nltk
import re
from nltk.tokenize import TreebankWordTokenizer


def filter_words(word):

    compile = re.compile("[^a-zA-Z]+")
    #for w in word:
    word = compile.sub(" ", word)
    word = word_tokenize(word.lower())
    word_tag = nltk.tag.pos_tag(word)

    filtered_word = []
    for word in word_tag:
        if len(word[0])==1:
            continue
        if word[1] not in ['CC', 'DT', 'EX', 'IN', 'LS', 'MD', 'WDT', 'WP', 'WP$','WRB', 'TO', 'PRP', 'PRP$']:  # 접속사(and), 관사(a,the), 소유형용사(his, her), 지시형용사(this, that), 부정형용사(some), 수량형용사(many), 관계형용사(what), 전치사(in, on), 리스트마커(1)), 조동사(could), 관계부사(which) 제외
            filtered_word.append(word)
    return filtered_word
