import re
import string

import nltk
import numpy as np
from nltk import WordNetLemmatizer, PorterStemmer, word_tokenize
from nltk.corpus import stopwords
from pyvi import ViTokenizer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

patterns = {
    '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹêềếểễệ]': 'e',
    '[ìíỉĩị]': 'i',
    '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụưừứửữự]': 'u',
    '[ỳýỷỹỵ]': 'y'
}

def convert(text):
    output = text
    for regex, replace in patterns.items():
        output = re.sub(regex, replace, output)
        # deal with upper case
        output = re.sub(regex.upper(), replace.upper(), output)
    return output

#Load Data và chia data và label riêng
def load_data(path):
    with open(path, 'r', encoding='latin-1') as f:
        lines = f.readlines()

    data = []
    label = []

    for line in lines:
        line = line.strip()
        splitted_line = line.split(None, 1)
        label.append(int(splitted_line[0]))
        data1 = ViTokenizer.tokenize(splitted_line[1])
        data1 = convert(data1)
        # print(data1)
        data.append(data1)

        # data.append(nltk.word_tokenize(splitted_line[1]))
        # data.append(splitted_line[1])

    print("Read file {} done : {} lines".format(path, len(data)))
    # print(data)
    # print(label)
    return data, label

wordnet_lemmatizer = WordNetLemmatizer()
def stemming_tokenizer(text):
    stemmer = PorterStemmer()
    return [stemmer.stem(w) for w in word_tokenize(text)]

def main():
    train = "train.txt"
    test_ham = "ham_test.txt"
    test_spam = "spam_test.txt"
    test_all = "test.txt"

    # data, label = load_data(train)
    # X_train, X_valid, y_train, y_valid = train_test_split(data, label, test_size=0.2, random_state=50) #spilit data ra để train và test
    X_train,y_train = load_data(train)
    X_valid,y_valid = load_data(test_all)


    # vectorizer = CountVectorizer()#chuyen doi dinh dang text thanh vector
    vectorizer = CountVectorizer(
        tokenizer=stemming_tokenizer,
        stop_words=stopwords.words('english') + list(string.punctuation)
        # stop_words=stopwords.words('english') + list(string.punctuation)
    )
    transformed_x_train = vectorizer.fit_transform(X_train).toarray() #chuyển X_train về dạng array
    # print(vectorizer.get_feature_names()) #Đó chính là các từ xuất hiện ít nhất 1 lần trong tất cả các string
    trainVocab = vectorizer.vocabulary_ #export tập từ vựng
    # print(len(trainVocab))

    vectorizer = CountVectorizer(vocabulary=trainVocab)
    transformed_x_valid = vectorizer.fit_transform(X_valid).toarray() #chuyển X_valid về dạng array


    best_clf = MultinomialNB()
    best_clf.fit(transformed_x_train, y_train)
    y_pred = best_clf.predict(transformed_x_valid)

    # print(np.asarray(y_valid))
    # print(np.asarray(y_pred))
    print('Training size = %d, accuracy = %.2f%%' % \
          (len(X_train), accuracy_score(y_valid, y_pred) * 100))

    # Thử áp dụng Grid_Search để xem có tăng độ chính xác không!
    params = {'alpha': [0.38,0.39,0.40,0.41,0.42,0.43]}
    clf = MultinomialNB()
    clf = GridSearchCV(clf, params, cv=5)
    clf.fit(transformed_x_train, y_train)

    print(clf.best_params_)
    best_clf = clf.best_estimator_
    y_pred = best_clf.predict(transformed_x_valid)
    print('Training size = %d, accuracy = %.2f%%' % \
          (len(X_train), accuracy_score(y_valid, y_pred) * 100))


    #Thử áp dụng Grid_Search vs SVM để xem có tăng độ chính xác không!
    clf = SVC()
    param_grid = {
        "C": [0.50,0.51,0.52,0.53,0.54,0.55],
        "kernel": ["rbf", "sigmoid"],
        "gamma": np.linspace(0.1, 1, 4),
    }
    clf = GridSearchCV(clf, param_grid=param_grid, cv=5)
    clf.fit(transformed_x_train, y_train)

    print(clf.best_params_)
    best_clf = clf.best_estimator_
    y_pred = best_clf.predict(transformed_x_valid)
    print('Training size = %d, accuracy = %.2f%%' % \
          (len(X_train), accuracy_score(y_valid, y_pred) * 100))

if __name__ == "__main__":
    main()
