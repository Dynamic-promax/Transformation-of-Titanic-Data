
# Titanic Dataset Cleaning and Analysis

## Project Overview
This project focuses on data cleaning and basic exploratory analysis of the Titanic dataset using Python and pandas. It demonstrates how to handle missing data, encode categorical variables, and analyze survival rates by gender and age groups.

## Prerequisites
- Python 3.x
- pandas library (`pip install pandas`)

## Dataset
You can download the Titanic dataset from:  
[Kaggle Titanic Dataset](https://www.kaggle.com/competitions/titanic/data)

## How to Run
1. Ensure the Titanic CSV file is in the path specified in the script or update the path accordingly.
2. Install required packages:
   ```bash
   pip install pandas
   ```
3. Run the script:
   ```bash
   python Cleaning_Titanic_dataset.py
   ```

## Key Steps in the Script
1. Load the Titanic dataset from CSV.
2. View basic info and check for missing values.
3. Remove rows with null values.
4. Encode 'Sex' as numerical (male = 1, female = 0).
5. One-hot encode the 'Embarked' column.
6. Group by gender and age group to analyze survival rates.

## Results Summary
- Displays the cleaned data.
- Shows survival rates by gender.
- Shows survival rates by age group categories: Child, Young Adult, Adult, and Senior.

## Author
**John Benedict Bello**  
[LinkedIn Profile](https://www.linkedin.com/in/bello-john-493b15155)

## License
This project is open source and available under the MIT License.
