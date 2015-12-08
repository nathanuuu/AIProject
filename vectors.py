import urllib
import numpy as np

# # Download the data from URL 
# url = "https://data.wprdc.org/datastore/dump/c0fcc09a-7ddc-4f79-a4c1-9542301ef9dd"
# fileobj = urllib.urlopen(url)
# inputString = fileobj.read()
# # fileobj.read() is a string, and we split by '\r\n' to extract each row
# dataArray = inputString.split('\r\n')

# Use dummyInput.txt
f = open('dummyInput.txt', 'r')
inputString = f.read()
# fileobj.read() is a string, and we split by '\n' to extract each row
dataArray = inputString.split('\n')

arrest_description = []
arrest_time = []
arrest_neighborhood = []
arrest_zone = []
arrest_age = []
arrest_gender = []
offense_description = []
offense_time = []
offense_neighborhood = []
offense_zone = []

for entry in dataArray[1:-1]:
    values = entry.split(',')
    index = int(values[0])
    if (values[1] == 'ARREST'):
        if (values[4].find("Burglar") == -1): arrest_description.append(0)
        else: arrest_description.append(1)
        arrest_time.append(int(values[5][11]+values[5][12])/6) # take 11&12 digit for the hour
        #arrest_neighborhood.append(values[7])
        arrest_zone.append(int(values[8]))
        arrest_age.append(int(values[9]))
        arrest_gender.append(values[10])
    elif (values[1] == 'OFFENSE 2.0'):
        if (values[4].find("Burglar") == -1): offense_description.append(0)
        else: offense_description.append(1)
        offense_time.append(int(values[5][11]+values[5][12])/6) # take 11&12 digit for the hour
        #offense_neighborhood.append(values[7])
        offense_zone.append(int(values[8]))

offense_time_zone = []
for i in range(len(offense_time)):
    feature = []
    for j in range(10):
        feature.append(0)
    offense_time_zone.append(feature)

for i in range(len(offense_time)):
    offense_time_zone[i][offense_time[i]] = 1
    if (offense_zone[i] != 1): offense_time_zone[i][2+offense_zone[i]] = 0.5
    elif (offense_zone[i] == 1): offense_time_zone[i][9] = 0.5
    offense_time_zone[i][3+offense_zone[i]] = 1
    if (offense_zone[i] != 6): offense_time_zone[i][4+offense_zone[i]] = 0.5
    elif (offense_zone[i] == 6): offense_time_zone[i][4] = 0.5

y = offense_description
X = offense_time_zone

def loss_logistic(X,y,theta):
    l = sum((np.log(1+np.exp(-y*np.dot(X,theta)))))/len(y)
    g = sum(np.dot(np.diag(1/(1+np.exp(y*np.dot(X,theta)))),(-np.dot(np.diag(y),X))))/len(y)
    return (l,g)

def loss_svm(X,y,theta):
    l = sum(np.maximum(np.zeros(len(y)),(1-y*np.dot(X,theta))))/len(y)
    g = sum(np.dot(np.diag(((y*np.dot(X,theta))<1)),(-np.dot(np.diag(y),X))))/len(y)
    return (l,g)

def grad_descent(X, y, lam, loss, T, alpha):
    theta = []
    for i in range(len(X[0])):
        theta.append(0)
    theta = np.array(theta)
    for j in range(T):
        theta = theta-alpha*(loss(X,y,theta)[1]+lam*theta)
    return theta
        
def stochastic_grad_descent(X, y, lam, loss, T, alpha):
    theta = []
    for i in range(len(X[0])):
        theta.append(0)
    theta = np.array(theta)
    for j in range(T):
        for m in range(len(y)):
            theta = theta-alpha*(loss(np.array([X[m]]),np.array([y[m]]),theta)[1]+lam*theta)
    return theta

print grad_descent(X, y, 1e-3, loss_svm, 10, 5.0)
print stochastic_grad_descent(X, y, 1e-3, loss_svm, 10, 0.001)