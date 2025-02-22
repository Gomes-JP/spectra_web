# tools_web.py
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class WebMathModels:
    @staticmethod
    def select_features(df, target):
        # Modified version without matplotlib
        corr_matrix = df.corr()
        upper_tri = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
        selected_features = [col for col in upper_tri.columns if any(abs(upper_tri[col]) >= 0.75]

        if target in selected_features:
            selected_features.remove(target)

        # Feature importance plot using Plotly
        X = df[selected_features]
        y = df[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        model = RandomForestRegressor()
        model.fit(X_train, y_train)

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=model.feature_importances_,
            y=selected_features,
            orientation='h'
        ))
        fig.update_layout(title='Feature Importance', xaxis_title='Importance', yaxis_title='Features')

        return {
            'features': selected_features,
            'plot': fig.to_json()
        }

class WebFilterValues:
    @staticmethod
    def filter_results(x, y, yerr):
        # Same logic without Tkinter dependencies
        df = pd.DataFrame({'x': x, 'y': y, 'yerr': yerr})
        df = df.dropna()
        return df['x'].values, df['y'].values, df['yerr'].values