#importing required libraries
from random import randint 
from sklearn.linear_model import LinearRegression

#Create a range limit for random numbers in the training set, and a count of the number of rows in the training set
TRAIN_SET_LIMIT = 1000 
TRAIN_SET_COUNT = 100

#Create an empty list of the input training set 'X' and create an empty list of the output for each training set 'X'
TRAIN_INPUT = list() 
TRAIN_OUTPUT= list()

#Create and append a randomly generated data set to the input and output 
for i in range(TRAIN_SET_COUNT): 
    a = randint(0, TRAIN_SET_LIMIT) 
    b = randint(0, TRAIN_SET_LIMIT) 
    c = randint(0, TRAIN_SET_LIMIT)
    d = randint(0, TRAIN_SET_LIMIT)

#Create a linear function for the output dataset 'X' 
    op = (7*a) + (3*b) + (4*c) + (9*d) 
    TRAIN_INPUT.append([a,b,c,d]) 
    TRAIN_OUTPUT.append(op)
    
#Create a linear regression object NOTE n_jobs = the number of jobs to use for computation, -1 means use all processors
predictor = LinearRegression(n_jobs = -1)

#fit the linear model (approximate a target function)
predictor.fit(X = TRAIN_INPUT, y = TRAIN_OUTPUT) 

#Create our testing data set, the ouput should be 7*10+3*20+4*30+9*40=610.
X_TEST = [[10,20,30,40]]

# Predict the ouput of the test data using the linear model
outcome = predictor.predict(X = X_TEST) 

#The estimated coefficients for the linear regression problem. be[7. 3. 4. 9.]
coefficients = predictor.coef_

print('Outcome: {} \n Coefficients: {}'.format(outcome, coefficients))
