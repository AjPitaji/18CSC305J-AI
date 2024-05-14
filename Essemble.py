# Importing necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score

# Load your dataset
# Assuming you have a dataset with features and target variable
# Replace this with your dataset loading code
# For demonstration, let's create a dummy dataset
X, y = np.random.rand(100, 10), np.random.randint(0, 2, 100)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define individual models
decision_tree = DecisionTreeClassifier()
random_forest = RandomForestClassifier()
gradient_boosting = GradientBoostingClassifier()

# Train individual models
decision_tree.fit(X_train, y_train)
random_forest.fit(X_train, y_train)
gradient_boosting.fit(X_train, y_train)

# Make predictions
predictions_dt = decision_tree.predict(X_test)
predictions_rf = random_forest.predict(X_test)
predictions_gb = gradient_boosting.predict(X_test)

# Ensemble predictions
ensemble_predictions = np.round((predictions_dt + predictions_rf + predictions_gb) / 3)

# Evaluate the ensemble model
ensemble_accuracy = accuracy_score(y_test, ensemble_predictions)
print("Ensemble Model Accuracy:", ensemble_accuracy)
