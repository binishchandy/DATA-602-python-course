'''
Assignment #7

1. Add / modify code ONLY between the marked areas (i.e. "Place code below")
2. Run the associated test harness for a basic check on completeness. A successful run of the test cases does not 
    guarantee accuracy or fulfillment of the requirements. Please do not submit your work if test cases fail.
3. To run unit tests simply use the below command after filling in all of the code:
    python 07_assignment.py
  
4. Unless explicitly stated, please do not import any additional libraries but feel free to use built-in Python packages
5. Submissions must be a Python file and not a notebook file (i.e *.ipynb)
6. Do not use global variables unless stated to do so
7. Make sure your work is committed to your master branch in Github


Packages required:

pip install cloudpickle==0.5.6 (this is an optional install to help remove a deprecation warning message from sklearn)
pip install sklearn

'''
# core
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ml
from sklearn import datasets as ds
from sklearn import linear_model as lm
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import train_test_split as tts

# infra
import unittest

# ------ Place code below here \/ \/ \/ ------
# import plotly library and enter credential info here
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tools
user_name = 'binishkurian'
api_key = 'TzQ6XHOUO3XY4riDAmsZ'


# ------ Place code above here /\ /\ /\ ------





# ------ Place code below here \/ \/ \/ ------
# Load datasets here once and assign to variables iris and boston

iris = ds.load_iris()
boston = ds.load_boston()

# ------ Place code above here /\ /\ /\ ------




# 10 points
def exercise01():
    '''
        Data set: Iris
        Return the first 5 rows of the data including the feature names as column headings in a DataFrame and a
        separate Python list containing target names
    '''

    # ------ Place code below here \/ \/ \/ ------
    df = pd.DataFrame(data=np.c_[iris['data']],
                      columns=iris['feature_names'])
    df_first_five_rows = df.head(5)
    target_names = iris.target_names
    # ------ Place code above here /\ /\ /\ ------


    return df_first_five_rows, target_names

# 15 points
def exercise02(new_observations):
    '''
        Data set: Iris
        Fit the Iris dataset into a kNN model with neighbors=5 and predict the category of observations passed in 
        argument new_observations. Return back the target names of each prediction (and not their encoded values,
        i.e. return setosa instead of 0).
    '''

    # ------ Place code below here \/ \/ \/ ------
    from sklearn import preprocessing
    X = iris.data
    y = iris.target
    df = pd.DataFrame(X, columns=iris.feature_names)

    X = df.values

    # Create a k-NN classifier with 5 neighbors: knn
    knn = KNN(n_neighbors=5)

    # Fit the classifier to the data
    knn.fit(X, y)

    # Predict and print the label for the new data point X_new
    X_new = new_observations
    new_prediction = knn.predict(X_new)

    le = preprocessing.LabelEncoder()
    le.fit(iris.target_names)
    iris_predictions = list(le.inverse_transform(new_prediction))

    # ------ Place code above here /\ /\ /\ ------


    return iris_predictions

# 15 points
def exercise03(neighbors,split):
    '''
        Data set: Iris
        Split the Iris dataset into a train / test model with the split ratio between the two established by 
        the function parameter split.
        Fit KNN with the training data with number of neighbors equal to the function parameter neighbors
        Generate and return back an accuracy score using the test data was split out

    '''
    random_state = 21

    

    # ------ Place code below here \/ \/ \/ ------
    X = iris.data
    y = iris.target
    df = pd.DataFrame(X, columns=iris.feature_names)

    X = df.values

    X_train, X_test, y_train, y_test = tts(X, y, test_size=split, random_state = random_state, stratify=y)

    knn = KNN(n_neighbors=neighbors)

    knn.fit(X_train, y_train)

    knn_score = knn.score(X_test, y_test)
    # ------ Place code above here /\ /\ /\ ------


    return knn_score

# 20 points
def exercise04():
    '''
        Data set: Iris
        Generate an overfitting / underfitting curve of kNN each of the testing and training accuracy performance scores series
        for a range of neighbor (k) values from 1 to 30 and plot the curves (number of neighbors is x-axis, performance score 
        is y-axis on the chart). Return back the plotly url.

    '''
    
    # ------ Place code below here \/ \/ \/ ------
    X = iris.data
    y = iris.target
    df = pd.DataFrame(X, columns=iris.feature_names)

    X = df.values

    X_train, X_test, y_train, y_test = tts(X, y, test_size=0.3, random_state=21, stratify=y)

    neighbors = np.arange(1, 30)
    train_accuracy = np.empty(len(neighbors))
    test_accuracy = np.empty(len(neighbors))

    # Loop over different values of k
    for i, k in enumerate(neighbors):
        # Setup a k-NN Classifier with k neighbors: knn
        knn = KNN(n_neighbors=k)

        # Fit the classifier to the training data
        knn.fit(X_train, y_train)

        # Compute accuracy on the training set
        train_accuracy[i] = knn.score(X_train, y_train)

        # Compute accuracy on the testing set
        test_accuracy[i] = knn.score(X_test, y_test)

    trace0 = go.Scatter(
        x=neighbors,
        y=test_accuracy,
        mode='lines',
        name='Testing Accuracy'
    )
    trace1 = go.Scatter(
        x=neighbors,
        y=train_accuracy,
        mode='lines',
        name='Training Accuracy'
    )
    data = [trace0, trace1]
    layout = dict(title='k-NN: Varying Number of Neighbors',
                  xaxis=dict(title='Number of Neighbors'),
                  yaxis=dict(title='Accuracy'),
                  )
    tools.set_credentials_file(username=user_name, api_key=api_key)
    fig = dict(data=data, layout=layout)
    plotly_overfit_underfit_curve_url = py.plot(fig, filename='k-NN-varyingNeighbors', layout=layout, auto_open=True)
    # ------ Place code above here /\ /\ /\ ------


    return plotly_overfit_underfit_curve_url

# 10 points
def exercise05():
    '''
        Data set: Boston
        Load sklearn's Boston data into a DataFrame (only the data and feature_name as column names)
        Load sklearn's Boston target values into a separate DataFrame
        Return back the average of AGE, average of the target (median value of homes or MEDV), and the target as NumPy values 
    '''

    # ------ Place code below here \/ \/ \/ ------
    X = boston.data
    y = boston.target
    df = pd.DataFrame(X, columns=boston.feature_names)
    average_age = df['AGE'].mean()
    df_target = pd.DataFrame(y)
    average_medv = df_target[0].mean()
    medv_as_numpy_values = df_target.values
    # ------ Place code above here /\ /\ /\ ------


    return average_age, average_medv, medv_as_numpy_values

# 10 points
def exercise06():
    '''
        Data set: Boston
        In the Boston dataset, the feature PTRATIO refers to pupil teacher ratio.
        Using a matplotlib scatter plot, plot MEDV median value of homes as y-axis and PTRATIO as x-axis
        Return back PTRATIO as a NumPy array
    '''

    # ------ Place code below here \/ \/ \/ ------
    X = boston.data
    y = boston.target
    X_axis = pd.DataFrame(X, columns=boston.feature_names)['PTRATIO'].values
    Y_axis = pd.DataFrame(y).values
    X_ptratio = X_axis

    plt.scatter(X_axis, Y_axis)
    plt.ylabel('Value of house /1000 ($)')
    plt.xlabel('Pupil teacher ratio')
    plt.show()
    # ------ Place code above here /\ /\ /\ ------


    return X_ptratio

# 20 points
def exercise07():
    '''
        Data set: Boston
        Create a regression model for MEDV / PTRATIO and display a chart showing the regression line using matplotlib
        with a backdrop of a scatter plot of MEDV and PTRATIO from exercise06
        Use np.linspace() to generate prediction X values from min to max PTRATIO
        Return back the regression prediction space and regression predicted values
        Make sure to labels axes appropriately
    '''

    # ------ Place code below here \/ \/ \/ ------

    reg = lm.LinearRegression()

    X = boston.data
    y = boston.target
    X_PTRATIO = pd.DataFrame(X, columns=boston.feature_names)['PTRATIO'].values
    # print(type(X_PTRATIO))
    y = pd.DataFrame(y).values

    X_PTRATIO = X_PTRATIO.reshape(-1, 1)
    y = y.reshape(-1, 1)
    reg.fit(X_PTRATIO, y)

    prediction_space = np.linspace(min(X_PTRATIO), max(X_PTRATIO)).reshape(-1, 1)
    reg_model = reg.predict(prediction_space)

    plt.scatter(X_PTRATIO, y, color='blue')
    plt.ylabel('Value of house /1000 ($)')
    plt.xlabel('Pupil teacher ratio')
    plt.plot(prediction_space, reg.predict(prediction_space), color='black', linewidth=3)
    plt.show()

    # ------ Place code above here /\ /\ /\ ------

    return reg_model, prediction_space


class TestAssignment7(unittest.TestCase):
    def test_exercise07(self):
        rm, ps = exercise07()
        self.assertEqual(len(rm),50)
        self.assertEqual(len(ps),50)

    def test_exercise06(self):
        ptr = exercise06()
        self.assertTrue(len(ptr),506)

    def test_exercise05(self):
        aa, am, mnpy = exercise05()
        self.assertAlmostEqual(aa,68.57,2)
        self.assertAlmostEqual(am,22.53,2)
        self.assertTrue(len(mnpy),506)
        
    def test_exercise04(self):
         print('Skipping EX4 tests')     

    def test_exercise03(self):
        score = exercise03(8,.25)
        self.assertAlmostEqual(exercise03(8,.3),.955,2)
        self.assertAlmostEqual(exercise03(8,.25),.947,2)
    def test_exercise02(self):
        pred = exercise02([[6.7,3.1,5.6,2.4],[6.4,1.8,5.6,.2],[5.1,3.8,1.5,.3]])
        self.assertTrue('setosa' in pred)
        self.assertTrue('virginica' in pred)
        self.assertTrue('versicolor' in pred)
        self.assertEqual(len(pred),3)
    def test_exercise01(self):
        df, tn = exercise01()
        self.assertEqual(df.shape,(5,4))
        self.assertEqual(df.iloc[0,1],3.5)
        self.assertEqual(df.iloc[2,3],.2)
        self.assertTrue('setosa' in tn)
        self.assertEqual(len(tn),3)
     

if __name__ == '__main__':
    unittest.main()

