from nltk import pos_tag
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


ACTION_TOKENS = ['open', 'execut', 'run', 
                'show', 'read', 'go', 'updat']

def get_actions_with_args(sentence: str):
    words = word_tokenize(sentence)
    tokens = pos_tag(words)
    stemmed = stem(tokens)
    results = retokenize_args_and_split_actions(words, stemmed)
    return results

def stem(tokens: list):
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(token[0]) for token in tokens]
    return stemmed

def retokenize_args_and_split_actions(words: list, stemmed: list):
    result = []
    temp = []
    for i in range(len(stemmed)):
        if stemmed[i] in ACTION_TOKENS:
            if temp:
                result.append(temp)
                temp = []
            temp.append(stemmed[i])
        else:
            temp.append(words[i])
    result.append(temp)
    if result[0][0] not in ACTION_TOKENS:
        return result[1:]
    return result
