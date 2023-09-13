import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, ElasticNet
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error, mean_squared_error

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
    #plot_residuos(y_train, y_predictions_train, y_test, y_predictions_test, model_name)
    return df_results
