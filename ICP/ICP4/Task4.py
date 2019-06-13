import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

X_train = pd.read_csv('./glass.csv')
train_df, test_df = train_test_split(X_train, test_size=0.4, random_state=0)
X_train = train_df.drop("Type",axis=1)
Y_train = train_df["Type"]
X_test = test_df.drop("Type",axis=1)
Y_test = test_df["Type"]

##SVM
svc = SVC(kernel='linear')
svc.fit(X_train, Y_train)
Y_pred = svc.predict(X_test)
acc_svc = round(svc.score(X_train, Y_train) * 100, 2)
print("svm Linear accuracy is:", acc_svc)
print("prediction",Y_pred)
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import  train_test_split

X_train = pd.read_csv('./glass.csv')
train_df, test_df = train_test_split(X_train, test_size=0.4, random_state=0)
X_train = train_df.drop("Type",axis=1)
Y_train = train_df["Type"]
X_test = test_df.drop("Type",axis=1)
Y_test = test_df["Type"]

##SVM
svc = SVC(kernel='rbf')
svc.fit(X_train, Y_train)
Y_pred = svc.predict(X_test)
acc_svc = round(svc.score(X_train, Y_train) * 100, 2)
print("svm  RBF accuracy is:", acc_svc)
print("prediction",Y_pred)