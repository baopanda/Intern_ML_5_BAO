import string

from nltk import WordNetLemmatizer, PorterStemmer, word_tokenize
from nltk.corpus import stopwords
from pyvi import ViTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

#Load Data và chia data và label riêng
def load_data():
    with open("train.txt", 'r', encoding="latin-1") as f:
        lines = f.readlines()

    data = []
    label = []

    for line in lines:
        line = line.strip()
        splitted_line = line.split(None, 1)
        label.append(int(splitted_line[0]))
        data.append(ViTokenizer.tokenize(splitted_line[1]))

    print("Read file {} done : {} lines".format("train.txt", len(data)))
    # print(data)
    # print(label)
    return data, label

def main():

    data, label = load_data()
    X_train, X_valid, y_train, y_valid = train_test_split(data, label, test_size=0.2, random_state=50) #spilit data ra để train và test

    vectorizer = CountVectorizer()#chuyen doi dinh dang text thanh vector
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


    #Thử áp dụng Grid_Search để xem có tăng độ chính xác không!
    params = {'alpha': [0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4]}
    clf = MultinomialNB()
    clf = GridSearchCV(clf, params, cv=5)
    clf.fit(transformed_x_train, y_train)

    print(clf.best_params_)
    best_clf = clf.best_estimator_
    y_pred = best_clf.predict(transformed_x_valid)
    print('Training size = %d, accuracy = %.2f%%' % \
          (len(X_train), accuracy_score(y_valid, y_pred) * 100))

if __name__ == "__main__":
    main()
