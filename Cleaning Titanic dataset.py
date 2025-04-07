import pandas as pd
df = pd.read_csv(r"C:\\Users\\DELL\\Desktop\\Data Sets\\CSV\\titanic.csv")

#View the data
print(df.head())

#Remove Null values
print(df.isnull().sum())

#Remove rows with null values
df_cleaned = df.dropna()

#Confirm missing values are removed
print(df_cleaned.isnull().sum())

#Convert sex column from categorical to numerical data (male=1, female=0)

df_cleaned['Sex'] = df_cleaned['Sex'].map({'male': 1, 'female': 0})

#Convert 'embark_town' into dummy variables
df_cleaned = pd.get_dummies(df_cleaned, columns=['Embarked'], drop_first=True)
print(df_cleaned.head())

#Group by gender and calculate survival rate
survival_gender = df_cleaned.groupby('Sex')['Survived'].mean()
print("survival rate by gender: \n", survival_gender)

#Group by age groups and calculate survival rate
df_cleaned['age_group'] = pd.cut(df_cleaned['Age'], bins=[0, 18, 35, 60, 100], labels=['Child', 'Young Adult', 'Adult', 'Senior'])
survival_age = df_cleaned.groupby('age_group', observed=False)['Survived'].mean()
print("survival rate by age group;\n, survival_age")


