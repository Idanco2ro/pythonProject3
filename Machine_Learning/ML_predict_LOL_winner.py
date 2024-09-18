# Imports
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Reading the data
df = pd.read_csv("games.csv")
champ_data = json.load(open("champion_info.json"))

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

# Training the model
clf = RandomForestClassifier(n_jobs=-1)
clf.fit(x_train, y_train)

# Evaluating the model
score = clf.score(x_test, y_test)
print(f"Accuracy percentage: {score * 100:.2f}%")

# Feature importance analysis
importances = dict(zip(clf.feature_names_in_, clf.feature_importances_))
sorted_importances = sorted(importances.items(), key=lambda x: x[1], reverse=True)

# Champion analysis
champ_name = 'Tristana'
wins1 = len(df[(df[f't1_{champ_name}'] == 1) & (df['winner'] == 1)])
wins2 = len(df[(df[f't2_{champ_name}'] == 1) & (df['winner'] == 2)])
losses1 = len(df[(df[f't1_{champ_name}'] == 1) & (df['winner'] == 2)])
losses2 = len(df[(df[f't2_{champ_name}'] == 1) & (df['winner'] == 1)])

# Printing the win ratio for the champion
print((wins1 + wins2) / (wins1 + wins2 + losses1 + losses2))
