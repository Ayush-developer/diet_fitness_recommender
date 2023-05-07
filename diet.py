import warnings
warnings.filterwarnings('ignore')
import math
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split

def model(weight,height,age):
    bmi = 10000*(int(weight))/(int(height)**2)
    print(bmi)

    fit_arr= [age,height,weight,bmi]
    print(fit_arr)
    data = pd.read_excel('GYMDATA.xlsx')

    df = data.copy()
    del df['Class']

    X = df.iloc[:,:-1]
    y = df['Prediction']

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)

    model_GYM = RandomForestClassifier(n_estimators=100)

    model_GYM.fit(X_train, y_train)

    print(model_GYM)


    expected = y_test
    predicted = model_GYM.predict(X_test)

    metrics.classification_report(expected, predicted)
    metrics.confusion_matrix(expected, predicted)
    return model_GYM.predict([fit_arr])
  


# model(weight,height,age)

















