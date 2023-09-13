from sklearn.linear_model import LinearRegression
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, ElasticNet
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error, mean_squared_error

'''
Función para calcular el índíce de calidad del aire (ICA)

Para ello primero calcula el indice de calidad del aire para cata contaminante atmosférico
- ICA_SO2 = (Concentración_SO2 / Valor_Límite_SO2) * 100, Valor límite = 125 μg/m3
- ICA_NO2 = (Concentración_NO2 / Valor_Límite_NO2) * 100, Valor límite = 40 μg/m3
- ICA_PM10 = (Concentración_PM10 / Valor_Límite_PM10) * 100, Valor límite = 50 μg/m3
- ICA_O3 = (Concentración_O3 / Valor_Límite_O3) * 100, Valor límite = 120 μg/m3

Luego promedia los valores de ICA de los cuatro contaminantes para obtener el índice de calidad del aire (ICA) general
- ICA = (ICA_SO2 + ICA_NO2 + ICA_PM10 + ICA_O3) / 4)
'''
def calcular_ICA(df):

    concentraciones = ['SO2', 'PM10', 'O3', 'NO2']
    valores_limites = [125, 50, 120, 40]  # Valores límite de los contaminantes
    
    ica_columnas = ['ICA_SO2', 'ICA_PM10', 'ICA_O3', 'ICA_NO2']
    
    for i, concentracion in enumerate(concentraciones):
        ica_contaminante = (df[concentracion] / valores_limites[i]) * 100
        df[ica_columnas[i]] = ica_contaminante.round(2)
    
    ica_promedio = df[ica_columnas].mean(axis=1)
    df['ICA'] = ica_promedio.round(2)
        
    return df

'''
Función que calcula el porcentaje de valores nulos en cada columna
'''
def calc_missing(df):

    missing_columns =[col for col in df.columns if df[col].isnull().sum() > 0]
    
    # Esta es otra opcion
    # for col in df.columns:
    #     if df[col].isnull().sum() > 0:
    #         missing_columns.append(col)
    
    for col in missing_columns:
        null_count = df[col].isnull().sum()
        total_count = df.shape[0]
        null_percent = (null_count / total_count) * 100
        print(f'{col} {null_count} / {total_count}= {null_percent:.2f} %')
        

'''
Función que devuelve las una lista con las columnas que tienen valores nulos
'''
def obtener_columnas_con_nulos(df):
    columnas_con_nulos = []

    for columna in df.columns:
        if df[columna].isnull().any():
            columnas_con_nulos.append(columna)
    
    return columnas_con_nulos

'''
Función que rellena los datos faltante con una predicción a partir de una regresión
'''
def rellenar_nulos_regresion(df, columns):
    imp_iter = IterativeImputer(random_state=42)
    
    for column in columns:
        df[column] = imp_iter.fit_transform(df[[column]])
    
    return df




def plot_residuos(y_train, y_predictions_train, y_test, y_predictions_test, model_name):
    resid_train = y_train - y_predictions_train
    resid_test = y_test - y_predictions_test

    sns.residplot(x=y_predictions_train, y=resid_train, color='b', lowess=True)
    plt.title(f'Residuos en entrenamiento - {model_name}')
    plt.xlabel('Predicciones')
    plt.ylabel('Residuos')
    plt.show()

    sns.residplot(x=y_predictions_test, y=resid_test, color='r', lowess=True)
    plt.title(f'Residuos en test - {model_name}')
    plt.xlabel('Predicciones')
    plt.ylabel('Residuos')
    plt.show()

def evaluate_model(model, X_train, X_test, y_train, y_test, model_name, df_results):
    model.fit(X_train, y_train)
    y_predictions_train = model.predict(X_train)
    mae_train = mean_absolute_error(y_train, y_predictions_train)
    rmse_train = mean_squared_error(y_train, y_predictions_train, squared=False)

    y_predictions_test = model.predict(X_test)
    mae_test = mean_absolute_error(y_test, y_predictions_test)
    rmse_test = mean_squared_error(y_test, y_predictions_test, squared=False)

    new_row = {
        'model_name': model_name,
        'mae_train': mae_train,
        'rmse_train': rmse_train,
        'mae_test': mae_test,
        'rmse_test': rmse_test
    }
    df_results.loc[df_results.shape[0]] = new_row
    plot_residuos(y_train, y_predictions_train, y_test, y_predictions_test, model_name)
    return df_results
