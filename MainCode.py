
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# data =  datadets

X = data[['high_heart_beat', 'high_pressure', 'fast_body_movement', 'high_altitude_brain_wavelength']]
y = data['seizure']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


model = LogisticRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print(classification_report(y_test, y_pred))


def predict_seizure(features):
    features_scaled = scaler.transform([features])
    prediction = model.predict(features_scaled)
    if prediction[0] == 1:
        return "Seizure Detected"
    else:
        return "No Seizure Detected"