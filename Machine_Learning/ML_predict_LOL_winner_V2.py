# Imports
import json
from sys import implementation

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Reading the data with exception handling
try:
    df = pd.read_csv("games.csv")
except FileNotFoundError:
    print("Fișierul games.csv nu a fost găsit.")
    exit()

try:
    champ_data = json.load(open("champion_info.json"))
except FileNotFoundError:
    print("Fișierul champion_info.json nu a fost găsit.")
    exit()

# Mapping champion IDs to their names
for i in range(1, 6):
    df[f"t1_champ{i}"] = df[f"t1_champ{i}id"].apply(lambda x: champ_data["data"][str(x)]["name"])
    df[f"t2_champ{i}"] = df[f"t2_champ{i}id"].apply(lambda x: champ_data["data"][str(x)]["name"])

# Filtering necessary columns
df = df[["t1_champ1", "t1_champ2", "t1_champ3", "t1_champ4", "t1_champ5",
          "t2_champ1", "t2_champ2", "t2_champ3", "t2_champ4", "t2_champ5",
          "firstBlood", "firstDragon", "firstTower", "firstBaron", "winner"]]

# Creating dummy variables for champions
encodings1 = [pd.get_dummies(df[col], prefix='t1') for col in ["t1_champ1", "t1_champ2", "t1_champ3", "t1_champ4", "t1_champ5"]]
combine_df1 = sum(encodings1)
encodings2 = [pd.get_dummies(df[col], prefix='t2') for col in ["t2_champ1", "t2_champ2", "t2_champ3", "t2_champ4", "t2_champ5"]]
combine_df2 = sum(encodings2)

# Combining the data
df = df.join(combine_df1).join(combine_df2)
df = df.drop(["t1_champ1", "t1_champ2", "t1_champ3", "t1_champ4", "t1_champ5",
               "t2_champ1", "t2_champ2", "t2_champ3", "t2_champ4", "t2_champ5"], axis=1)

# Preparing data for the model
x, y = df.drop('winner', axis=1), df['winner']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Normalizing the data
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Hyperparameter tuning with GridSearchCV
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10, 20],
}
grid_search = GridSearchCV(RandomForestClassifier(n_jobs=-1), param_grid, cv=5)
grid_search.fit(x_train, y_train)

# Training the model with the best parameters
clf = grid_search.best_estimator_
clf.fit(x_train, y_train)

# Evaluating the model
score = clf.score(x_test, y_test)
print(f"Accuracy percentage: {score * 100:.2f}%")

# Feature importance analysis
importances = dict(zip(x.columns, clf.feature_importances_))
sorted_importances = sorted(importances.items(), key=lambda x: x[1], reverse=True)

# Limit to the top 20 features
top_n = 20
top_features = sorted_importances[:top_n]

# Visualizing feature importance
features = [feature for feature, _ in top_features]
importance_values = [importance for _, importance in top_features]

plt.figure(figsize=(12, 8))  # Mărim figura pentru a oferi mai mult spațiu
plt.barh(features, importance_values)
plt.xlabel('Feature Importance')
plt.title('Top 20 Feature Importance')

# Rotirea etichetelor pe axa y pentru a evita suprapunerea
plt.yticks(rotation=45)

# Ajustarea layout-ului pentru a preveni suprapunerile
plt.tight_layout()

plt.show()


# Champion analysis
champ_name = 'Tristana'
wins1 = len(df[(df[f't1_{champ_name}'] == 1) & (df['winner'] == 1)])
wins2 = len(df[(df[f't2_{champ_name}'] == 1) & (df['winner'] == 2)])
losses1 = len(df[(df[f't1_{champ_name}'] == 1) & (df['winner'] == 2)])
losses2 = len(df[(df[f't2_{champ_name}'] == 1) & (df['winner'] == 1)])

# Calculating and printing the win ratio for the champion
total_games = wins1 + wins2 + losses1 + losses2
win_ratio = (wins1 + wins2) / total_games if total_games > 0 else 0
print(f"Win ratio for {champ_name}: {win_ratio:.2f}")

