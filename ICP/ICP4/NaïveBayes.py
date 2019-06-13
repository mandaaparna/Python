import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)
train_test_split_1 = pd.read_csv('./glass.csv')
train_df, test_df = train_test_split(train_test_split_1, test_size=0.5, random_state=0)

X_train = train_df.drop("Type",axis=1)
Y_train = train_df["Type"]
model = GaussianNB()
model.fit(X_train, Y_train)
X_test = test_df.drop("Type",axis=1).copy()
Y_test = model.predict(X_test)
acc_svc = round(model.score(X_train, Y_train) * 100, 2)
print("NB accuracy is:", acc_svc)

plt.hist(Y_train,color='blue')
plt.xlabel('Type')
plt.ylabel('Count')
plt.title('BN Model')
plt.show()
plt.scatter(Y_test, test_df["Type"], alpha=.75,
            color='b') #alpha helps to show overlapping data
plt.xlabel('Predicted Price')
plt.ylabel('Actual Price')
plt.title('BN Model')
plt.show()