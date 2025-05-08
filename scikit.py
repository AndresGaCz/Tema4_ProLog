
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score 

iris = load_iris() 

X = iris.data    # variables predictoras (features) 
y = iris.target  # variable objetivo (label) 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, 
random_state=42) 

model = LogisticRegression(max_iter=200) 

model.fit(X_train, y_train) 

y_pred = model.predict(X_test) 


print("Precision:", accuracy_score(y_test, y_pred))