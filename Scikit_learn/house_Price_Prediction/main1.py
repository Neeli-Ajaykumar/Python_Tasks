#Importing required libraries
import numpy as np
import pandas as pd

# Loading dataset
dataset = pd.read_csv("kc_house_data.csv")
print(dataset.head())

def categorize_price(price):
    if price < 300000:
        return 0
    elif price < 600000:
        return 1
    else:
        return 2
dataset['price_category'] = dataset['price'].apply(categorize_price)

# Selecting features (X) and target (y)
X = dataset[['bedrooms','bathrooms','sqft_living','sqft_lot',
             'floors','condition','grade','sqft_basement','yr_built','yr_renovated']].values
y = dataset['price_category'].values

# Display shape of data
print('-'*80)
print(f'Shape of X is {X.shape}\nShape of y is {y.shape}')

# Splitting dataset into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

print('-'*80)
print(f"Length of X_train: {len(X_train)}\nLength of X_test: {len(X_test)}")
print(f"Length of y_train: {len(y_train)}\nLength of y_test: {len(y_test)}")

# -----------------------------
# Feature Scaling
# -----------------------------

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)

# Transform test data (important: do NOT fit again)
X_test = sc.transform(X_test)

# ============================================================
# 1. Support Vector Machine (SVM)
# ============================================================

from sklearn.svm import SVC
classifier = SVC()

# Train model
classifier.fit(X_train, y_train)

# Predict test data
y_pred = classifier.predict(X_test)

# Evaluate accuracy
from sklearn.metrics import accuracy_score

print('\n'+'-'*20+'Accuracy Score on the Test set'+'-'*20)
print(classifier)

print("SVC Accuracy:", accuracy_score(y_test, y_pred))
print("{:.0%}".format(accuracy_score(y_test, y_pred)))


# ============================================================
# 2. Logistic Regression
# ============================================================

from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import accuracy_score

print('\n'+'-'*20+'Accuracy Score on the Test set'+'-'*20)
print(classifier)

print("LogisticRegression Accuracy:", accuracy_score(y_test, y_pred))
print("{:.0%}".format(accuracy_score(y_test, y_pred)))

# ============================================================
# 3. Naive Bayes
# ============================================================

from sklearn.naive_bayes import GaussianNB

classifier = GaussianNB()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import accuracy_score

print('\n'+'-'*20+'Accuracy Score on the Test set'+'-'*20)
print(classifier)

print("GaussianNB Accuracy:", accuracy_score(y_test, y_pred))
print("{:.0%}".format(accuracy_score(y_test, y_pred)))

# ============================================================
# 4. Decision Tree Classifier
# ============================================================

from sklearn.tree import DecisionTreeClassifier

classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import accuracy_score

print('\n'+'-'*20+'Accuracy Score on the Test set'+'-'*20)
print(classifier)

print("Decision Tree Classifier Accuracy:", accuracy_score(y_test, y_pred))
print("{:.0%}".format(accuracy_score(y_test, y_pred)))

# ============================================================
# 5. Random Forest Classifier
# ============================================================

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import accuracy_score

print('\n'+'-'*20+'Accuracy Score on the Test set'+'-'*20)
print(classifier)

print("Random Forest Classifier Accuracy:", accuracy_score(y_test, y_pred))
print("{:.0%}".format(accuracy_score(y_test, y_pred)))

# ============================================================
# 6. Ridge Classifier
# ============================================================

from sklearn.linear_model import RidgeClassifier

classifier = RidgeClassifier()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import accuracy_score

print('\n'+'-'*20+'Accuracy Score on the Test set'+'-'*20)
print(classifier)

print("Ridge Classifier Accuracy:", accuracy_score(y_test, y_pred))
print("{:.0%}".format(accuracy_score(y_test, y_pred)))

# ============================================================
# 7. K-Nearest Neighbors (KNN)
# ============================================================

from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import accuracy_score

print('\n'+'-'*20+'Accuracy Score on the Test set'+'-'*20)
print(classifier)

print("KNN Accuracy:", accuracy_score(y_test, y_pred))
print("{:.0%}".format(accuracy_score(y_test, y_pred)))

