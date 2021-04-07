# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:21:15 2021

@author: Desktop
"""
#LEER EL DATSET
import pandas as pd
import numpy as np
#from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
clasificador=tree.DecisionTreeClassifier()
#leer los datos
datos=pd.read_csv("GlobalLandTemperaturesByState.csv")
print(datos[:5])
datos0=datos['dt']
datos3=datos['State']
datos4=datos['Country']
datos33=pd.get_dummies(datos3,columns=['State'])
datos00=pd.get_dummies(datos0,columns=['dt'])
print(datos00[:5])
print(datos33[:5])
#MIRAMOS QUE NUMERO DE PACIENTES USA CAD FARMACO
pais=datos['Country'].value_counts()
print("los paises son \n",pais)

#creamos nuestro vector de paises independientes
X=datos[['dt','AverageTemperature','AverageTemperatureUncertainty','State']].values
print(X[:5])


y=datos['Country']
print(y[:5])

datos=pd.concat([datos,datos00],axis=1)
datos=pd.concat([datos,datos33],axis=1)
datossolo=datos.drop(['dt','State','Country'],axis=1)
#entrenamiento
print(datossolo[:5])
from sklearn import model_selection
from sklearn.metrics import confusion_matrix
print("PRIMERO")
X_train, X_test, y_train, y_test = model_selection.train_test_split( X, y, test_size=0.2)
print(len(X_train))
print(len(X_test))
print(X_train[:5])
print(X_test[:5])
print("SEGUNDO")
X_train, X_test, y_train, y_test = model_selection.train_test_split( X, y, test_size=0.3)
print(len(X_train))
print(len(X_test))
print(X_train[:5])
print(X_test[:5])
print("TERCERO")
X_train, X_test, y_train, y_test = model_selection.train_test_split( X, y, test_size=0.1)
print(len(X_train))
print(len(X_test))
print(X_train[:5])
print(X_test[:5])
print("CUARTO")
X_train, X_test, y_train, y_test = model_selection.train_test_split( X, y, test_size=0.6)
print(len(X_train))
print(len(X_test))
print(X_train[:5])
print(X_test[:5])
print("QUINTO")
X_train, X_test, y_train, y_test = model_selection.train_test_split( X, y, test_size=0.3)
print(len(X_train))
print(len(X_test))
print(X_train[:5])
print(X_test[:5])
print("SEXTO")
X_train, X_test, y_train, y_test = model_selection.train_test_split( X, y, test_size=0.2)
print(len(X_train))
print(len(X_test))
print(X_train[:5])
print(X_test[:5])
print("SEPTIMO")
X_train, X_test, y_train, y_test = model_selection.train_test_split( X, y, test_size=0.5)
print(len(X_train))
print(len(X_test))
print(X_train[:5])
print(X_test[:5])
print("OCTAVO")
X_train, X_test, y_train, y_test = model_selection.train_test_split( X, y, test_size=0.2)
print(len(X_train))
print(len(X_test))
print(X_train[:5])
print(X_test[:5])
print("NOVENO")
X_train, X_test, y_train, y_test = model_selection.train_test_split( X, y, test_size=0.3)
print(len(X_train))
print(len(X_test))
print(X_train[:5])
print(X_test[:5])
print("DECIMO")
X_train, X_test, y_train, y_test = model_selection.train_test_split( X, y, test_size=0.4)
print(len(X_train))
print(len(X_test))
print(X_train[:5])
print(X_test[:5])

