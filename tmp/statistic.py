import jieba
import jieba.analyse

jieba.set_dictionary('tmp/dict.txt.big')
# jieba.analyse.set_stop_words('tmp/baidu_stopwords.txt')

jieba.initialize()
jieba.suggest_freq('润和', True)
jieba.suggest_freq('物产中大', True)


def stopwordslist(filepath= 'tmp/baidu_stopwords.txt'):
    stopwords_ = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return frozenset(stopwords_)
STOP_WORDS = stopwordslist()

def movestopwords(sentence, stopwords):
    return [word for word in sentence if word not in stopwords]



a='全裸导演第二季出来了 ！'
print('/'.join(jieba.cut(a, HMM=True)))
movestopwords(jieba.cut(a, HMM=True),STOP_WORDS)

# 使用 add_word(word, freq=None, tag=None) 和 del_word(word) 可在程序中动态修改词典。
# 使用 suggest_freq(segment, tune=True) 可调节单个词语的词频，使其能（或不能）被分出来。
