import pandas as pd
from imblearn.over_sampling import RandomOverSampler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import VotingClassifier
from datetime import datetime
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV

# Load your cricket dataset
data = pd.read_csv('ipl_dataset.csv')

# Data preprocessing

# Handling missing values
data.fillna(0, inplace=True)  # You might use different strategies for missing data

# Convert the 'margin' column to a numerical format
data['margin'] = data['margin'].str.extract('(\d+)').astype(float)

# Fill missing values in the 'margin' column (if any)
data['margin'].fillna(0, inplace=True)

# Convert all data in relevant columns to strings
string_columns = ['team1', 'team2', 'toss_winner', 'toss_choice', 'winner', 'man_of_the_match']
data[string_columns] = data[string_columns].astype(str)

# Encoding categorical variables
encoder = LabelEncoder()
for column in string_columns:
    data[column] = encoder.fit_transform(data[column])

# Feature Engineering
# Depending on your dataset and objectives, you might want to engineer features such as 'team1_score', 'team2_score', etc.

# Splitting the data
X = data[['team1', 'team2', 'toss_winner', 'toss_choice', 'margin', 'man_of_the_match']]
y = data['winner']

# Oversampling to address class imbalance
oversampler = RandomOverSampler(random_state=42)
X_resampled, y_resampled = oversampler.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Standardize the features using StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define a dictionary of classifiers
classifiers = {
    'Logistic Regression': LogisticRegression(),
    'Decision Tree': DecisionTreeClassifier(),
    'SVM': SVC(probability=True),
    'KNN': KNeighborsClassifier(),
    'Naive Bayes': GaussianNB(),
    'XGBoost': XGBClassifier()
}

# Hyperparameter tuning for RandomForestClassifier
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

rf_classifier = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(rf_classifier, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)
best_rf_classifier = grid_search.best_estimator_

# Create a VotingClassifier with 'hard' voting
voting_clf = VotingClassifier(estimators=list(classifiers.items()) + [('Random Forest', best_rf_classifier)], voting='hard')
voting_clf.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred = voting_clf.predict(X_test)

# Print model evaluation results
print("Model Evaluation Results:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))


