import pylab as pl
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split,StratifiedKFold,cross_val_score
from sklearn.decomposition import PCA
from sklearn.feature_selection import RFECV
from sklearn.svm import SVC
import sklearn.preprocessing as pp

working_directory =r"./"

train_init = np.genfromtxt(open(working_directory + 'train.csv','rb'), delimiter=',')
target_init = np.genfromtxt(open(working_directory + 'trainLabels.csv','rb'), delimiter=',')
test_init = np.genfromtxt(open(working_directory + 'test.csv','rb'), delimiter=',')


"""
Split data into train and test
"""
def dsplit(train_init,target_init):
    train,test,train_target,test_target = train_test_split(train_init,target_init,test_size=0.1,random_state=42)
    return train,test,train_target,test_target


"""
Support vector Machines
"""
def svmclassifier(train,test,train_target,test_target):
    clf = SVC(kernel='rbf', C=1.35, gamma = 0.3)
    print clf
    clf.fit(train,train_target)
    res = clf.predict(train)
    print classification_report(train_target,res)
    
    res1 = clf.predict(test)
    print classification_report(test_target,res1)
    return clf




"""
perform pca
"""
def dopca(train,train_target,test,test_init):
    pca = PCA(n_components=12,whiten=True)
    train = pca.fit_transform(train,train_target)
    test = pca.transform(test)
    test_init =pca.transform(test_init)
    return train,test,test_init
    


train,test,train_target,test_target = dsplit(train_init,target_init)

train,test,test_init = dopca(train,train_target,test,test_init)


#est = knnclassifier(train,test,train_target,test_target)
est = svmclassifier(train,test,train_target,test_target)

res = est.predict(test_init)
idcol = np.arange(start=1,stop=9001)
res2 = np.column_stack((idcol,res))

np.savetxt(working_directory + 'prediction.csv',res2,fmt='%d',delimiter=",")



