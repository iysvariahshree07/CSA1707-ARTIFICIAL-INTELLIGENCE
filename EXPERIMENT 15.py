from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names

# Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create Decision Tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predict on test set
y_pred = clf.predict(X_test)

# Accuracy
accuracy = clf.score(X_test, y_test)

# Print decision tree rules
tree_rules = export_text(clf, feature_names=feature_names)

print(f"Accuracy on test set: {accuracy:.2f}\n")
print("Decision Tree rules:")
print(tree_rules)

print("Predictions on test set:")
for i, pred in enumerate(y_pred):
    print(f"Sample {i+1}: Predicted class = {iris.target_names[pred]}, Actual class = {iris.target_names[y_test[i]]}")
