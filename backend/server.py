import numpy as np
import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler





credit_card_data = pd.read_csv('./Data/creditcard.csv')
credit_card_data.head()
credit_card_data.tail()
credit_card_data.info()
credit_card_data.isnull().sum()
credit_card_data['Class'].value_counts()
legit = credit_card_data[credit_card_data.Class == 0]
fraud = credit_card_data[credit_card_data.Class == 1]
print(legit.shape)
print(fraud.shape)
credit_card_data['Class'].value_counts()
legit.Amount.describe()
fraud.Amount.describe()
credit_card_data.groupby('Class').mean()
legit_sample = legit.sample(n=492)
new_dataset = pd.concat([legit_sample, fraud], axis=0)
new_dataset.head()
new_dataset.tail()
new_dataset['Class'].value_counts()
new_dataset.groupby('Class').mean()
X = new_dataset.drop(columns='Class', axis=1)
Y = new_dataset['Class']
print(X)
print(Y)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
print(X.shape, X_train.shape, X_test.shape)
#model = LogisticRegression()
#model.fit(X_train, Y_train)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = LogisticRegression(max_iter=100000, solver='saga', class_weight='balanced')
model.fit(X_train_scaled, Y_train)
model = LogisticRegression(max_iter=100000, solver='liblinear', class_weight='balanced')
model.fit(X_train_scaled, Y_train)

'''
# Correlation heatmap
corr_matrix = pd.DataFrame(X_train_scaled).corr()
sns.heatmap(corr_matrix, annot=False, cmap='coolwarm')
plt.show()
model = LogisticRegression(max_iter=100000, solver='saga', class_weight='balanced', C=0.1)
model.fit(X_train_scaled, Y_train)
'''




# Split the data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
# Scale the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Logistic Regression with modified parameters
model = LogisticRegression(max_iter=100000, solver='liblinear', class_weight='balanced', C=0.1)
model.fit(X_train_scaled, Y_train)

# Evaluate the model
accuracy = model.score(X_test_scaled, Y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")