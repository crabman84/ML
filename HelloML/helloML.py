### Tutorial from: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
## Author: Luke Gavin
## Date: 23/08/2019
import loadedLibraries;
from loadedLibraries import *;
# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv";
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'];
dataset = pandas.read_csv(url, names=names);

#Dimensions of datasheets

print(dataset.shape);

# Always to a good idea to eyeball your data to see Class Distribution
# Print first 20 rows of dataset
print(dataset.head(20));

# Lets look at the summary of each attribute(or the descriptions)

print(dataset.describe());


# Data visualisation
