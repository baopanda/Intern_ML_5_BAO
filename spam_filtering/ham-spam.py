import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from pyvi import ViTokenizer

def load_data():
    with open("train1.txt", 'r', encoding="latin-1") as f:
        lines = f.readlines()

    data = []
    label = []

    for line in lines:
        line = line.strip()
        splitted_line = line.split(None, 1)
        label.append(int(splitted_line[0]))
        data.append(ViTokenizer.tokenize(splitted_line[1]))
        for i in data:
            print(data)

    print("Read file {} done : {} lines".format("train.txt", len(data)))
    return data, label

def train_data():
    training_data, training_label = load_data()

    train_size = len(training_data)
    num_hams = np.sum(np.array(training_label) == 1)
    num_spams = np.sum(np.array(training_label) == -1)

    print("Number hams  : ", num_hams)
    print("Number spams : ", num_spams)
    print("Train size   : ", train_size)
    print(training_data)

    # Naive Bayes
    model_name = "MNB"

    # # Training
    # param_grid = {"alpha": [0.01, 0.03, 0.1, 0.3, 1]}
    # mnb_clf = GridSearchCV(MultinomialNB(), param_grid=param_grid, cv=5)
    # mnb_clf.fit(training_data, training_label)
    # print("{}: Best param : {}".format(model_name, mnb_clf.best_params_))
    # print("Best accuracy score : {}".format(mnb_clf.best_score_))


def main():
    train_data()

if __name__ == "__main__":
    main()

