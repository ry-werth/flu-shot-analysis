# flu-shot-analysis
This notebook explores different Classifiers for predicting whether or not someone will get a Flu vaccine.

The final can be seen in use this [app](https://flu-analysis.herokuapp.com/) that I put together using flask and d3. 

## Data
The data is taken originally from the [U.S. National 2009 H1N1 Flu Survey (NHFS).](https://webarchive.loc.gov/all/20140511031000/http://www.cdc.gov/nchs/nis/about_nis.htm#h1n1). It was compiled and organized by [DataDriven](https://www.drivendata.org/competitions/66/flu-shot-learning/data/) which is where I downloaded it from. The data consists of information the survey respondants shared about their lives, opinions, and behaviors, as well as whether they got the Seasonal and H1N1 Flu vaccines.


## Project Goal
The ultimate goal is to create a prediction model that will identify people who are least likely to get a vaccine for the seasonal flu or a more novel infectious disease. This model will give us an understanding of how certain characteristics have been associated with personal vaccination patterns. This will help provide guidance for future public health efforts.

## Classifiers Explored
This project was meant to explore all sorts of different classification methods.
These are what I looked at with my data: 
- KNN (Nearest Neighbors)
- Decision Trees and Random Forests
- Logistic Regression
- Naive Bayes (Gaussian, Complement,  Categorical)
- Support Vector Classification
- XGBoost


## Main Files

- [cleaning.ipynb](work_analysis/cleaning.ipynb)\
  notebook containing the data processing and cleaning 
  
- [Initial_analysis.ipynb](work_analysis/Initial_analysis.ipynb) \
  The intial analysis and data exploration process
  
- [Final_Workbook.ipynb](work_analysis/Final_Workbook.ipynb) \
  This is the heart of the project. This is where all the modelling and model comparison lies. 
  

## Biggest Challenge

The survey contained a lot of null values, I had to explore each feature and decide what the best way to handle the null values were. I learned that a small difference in two data cleaning processes can have vast consequences on the end model. For some categories I ended up keeping the Null values as almost a "value" in and of itself. I.E. For health insurance we basically have "Yes they have it", "No they don't have it", and "We Don't Know". This was my first time treating null values this way, but I felt they held a certain signifigance.
  

## Big picture takeaways
- People listen to their doctors. Unsurprisingly, a large factor as to whether or not someone got a vaccine was whether or not it was recommened to them by thier doctors.

- Peoples opinions guide their actions more than any other factors. Across race, socio-economic or education levels a person's opinion on virus severity, or vaccine effectivity played the largest role as to whether they would get a vaccine. This is not a case of "I don't think it will help, but I'll get it anyways because it is easy". If a person wasn't afraid of the flu they likely weren't going to get vaccinated.

- If you don't have health insurance you probably aren't getting a flu vaccine. Health Insurance seems to be a large "barrier" to vaccination. All else being equal, if a person is not insured they are far less likely to get a vaccine.
  
## Final Model In Action
[Here](https://flu-analysis.herokuapp.com/) you can play with the final model in action.


## Technologies/Programs used
- Python
- Pandas/NumPy
- Matplotlib/Seaborn
- SQL/Postgres/psycopg2
- Flask
- Javascript/D3
- Heroku

