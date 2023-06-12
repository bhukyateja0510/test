import re
import numpy as np
import pandas as pd
from django.conf import settings
from sklearn.metrics import f1_score, accuracy_score, recall_score, precision_score


class Algorithms:

    path = settings.MEDIA_ROOT + "\\" + "FoodRecipeRating.csv"
    data = pd.read_csv(path)
    data = data.drop(['RecipeId'], axis=1)
    data = data.fillna('')
    data['new'] = np.where(data['AggregatedRating'] >= float(2.5), 1, 0)
    data = data.drop(['AggregatedRating'], axis=1)
    x = data.iloc[:, 0:-1]
    y = data.iloc[:, -1]

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=1)
    from sklearn.preprocessing import StandardScaler

    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.fit_transform(x_test)

    x_train = pd.DataFrame(x_train)
    y_train = pd.DataFrame(y_train)
    x_train = x_train.astype(int)
    y_train = y_train.astype(int)
    print(' train type:', type(y_train))

    def calc_random_forest_Classifier(self):
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier()

        self.x_train = self.x_train.fillna(self.x_train.mean())
        model.fit(self.x_train, self.y_train)

        y_pred = model.predict(self.x_test)

        precision = precision_score(y_pred, self.y_test, average='weighted')

        recall = recall_score(y_pred, self.y_test, average='weighted')

        f1 = f1_score(y_pred, self.y_test, average='weighted')
        return precision, recall, f1

    #  nb

    def calc_naive_bayes_Classifier(self):
        from sklearn.neighbors import KNeighborsClassifier
        model = KNeighborsClassifier()

        self.x_train = self.x_train.fillna(self.x_train.mean())
        model.fit(self.x_train, self.y_train)

        y_pred = model.predict(self.x_test)
        accuracy = accuracy_score(y_pred, self.y_test)
        print('accuracy=', accuracy)

        precision = precision_score(y_pred, self.y_test, average='weighted')

        recall = recall_score(y_pred, self.y_test, average='weighted')

        f1 = f1_score(y_pred, self.y_test, average='weighted')

        return precision, recall, f1

    def calc_support_vector_machine_Classifier(self):
        from sklearn.svm import SVC
        model = SVC()

        self.x_train = self.x_train.fillna(self.x_train.mean())
        model.fit(self.x_train, self.y_train)

        y_pred = model.predict(self.x_test)

        precision = precision_score(y_pred, self.y_test, average='micro')

        recall = recall_score(y_pred, self.y_test, average='micro')

        f1 = f1_score(y_pred, self.y_test, average='weighted')

        return precision, recall, f1

    def calc_logistic_Regression(self):
        from sklearn.linear_model import LogisticRegression
        model = LogisticRegression()

        self.x_train = self.x_train.fillna(self.x_train.mean())
        model.fit(self.x_train, self.y_train)

        y_pred = model.predict(self.x_test)

        precision = precision_score(y_pred, self.y_test, average='weighted')

        recall = recall_score(y_pred, self.y_test, average='weighted')

        f1 = f1_score(y_pred, self.y_test, average='weighted')

        return precision, recall, f1

    def calc_KNN_Classifier(self):
        from sklearn.neighbors import KNeighborsClassifier
        model = KNeighborsClassifier()

        self.x_train = self.x_train.fillna(self.x_train.mean())

        model.fit(self.x_train, self.y_train)

        y_pred = model.predict(self.x_test)
+
        precision = precision_score(y_pred, self.y_test, average='weighted')

        recall = recall_score(y_pred, self.y_test, average='weighted')

        f1 = f1_score(y_pred, self.y_test, average='weighted')

        return precision, recall, f1

    def calc_DT_Classifier(self):
        from sklearn.tree import DecisionTreeClassifier
        model = DecisionTreeClassifier()

        self.x_train = self.x_train.fillna(self.x_train.mean())
        model.fit(self.x_train, self.y_train)

        y_pred = model.predict(self.x_test)

        precision = precision_score(y_pred, self.y_test, average='weighted')

        recall = recall_score(y_pred, self.y_test, average='weighted')

        f1 = f1_score(y_pred, self.y_test, average='weighted')

        return precision, recall, f1

    def test_userInput(self, data):
        from sklearn.linear_model import LogisticRegression
        model = LogisticRegression()
        self.x_train = self.x_train.fillna(self.x_train.mean())
        model.fit(self.x_train, self.y_train)
        results = model.predict([data])
        return results
