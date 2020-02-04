import pandas as pd 

# read csv data set 'https://www.kaggle.com/kaggle/sf-salaries'
sal = pd.read_csv('Salaries.csv')

# finding head
sal.head()

# Use the .info() method to find out how many entries there are.
sal.info()

# findig average base pay
sal['BasePay'].mean()

# highest overtime pay
sal['OvertimePay'].max()

# ** Finding the job title of JOSEPH DRISCOLL ? 
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']

# How much does JOSEPH DRISCOLL make (including benefits)?
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']

# employee with highest total pay with benefits
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]

# employee with lowest total pay with benefits
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]

# What was the average (mean) BasePay of all employees per year? (2011-2014) ? *
sal.groupby('Year').mean()['BasePay']

# How many unique job titles are there?
sal['JobTitle'].nunique()

# What are the top 5 most common jobs?
sal['JobTitle'].value_counts().head(5)

# How many Job Titles were represented by only one person in 2013?
sum(sal[sal['Year']==2013]['JobTitle'].value_counts()==1)