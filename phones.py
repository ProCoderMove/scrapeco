import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder


def objectify(ram,storage,yor,age, scrd,chrgav,keywork, batth):
    d = {
       'RAM (GB)': ram,
       'Storage (GB)': storage,
       'Year of Release': yor,
       'Age (Years)': age,
       'Screen Damage': scrd,  # 0 for No
       'Charger Availability': chrgav,  # 1 for Yes
       'Keyword Working': keywork,  # 1 for Yes
       'Battery Health (%)': batth
    }
    return d
    
def predict(ram,storage,yor,age, scrd,chrgav,keywork, batth):
    df = pd.read_csv("D:/ewaste_price_detection/Ewaste_price_prediction/used_device_data.csv")
    df_drop_rows = df.dropna()
    df = df.fillna(0)
    # Drop columns with any missing values
    df_drop_rows = df.dropna(axis=1)
    # Drop rows only if all columns have missing values
    df_drop_rows_all = df.dropna(how='all')
    df2 = df.copy()
    # Label Encoding for categorical variables
    label_encoder = LabelEncoder()
    df2['device_brand'] = label_encoder.fit_transform(df2['device_brand'])
    df2['os'] = label_encoder.fit_transform(df2['os'])
    df2['screen_size'] = label_encoder.fit_transform(df2['screen_size'])

    # Convert 'Storage (GB)' column to numeric by extracting numerical part

    # Define features and target variable
    features = ['RAM (GB)', 'Storage (GB)', 'Year of Release', 'Age (Years)', 'Screen Damage',
                'Charger Availability', 'Keyword Working', 'Battery Health (%)']

    target = 'Old Phone Selling Price (Rs)'

    X = df2[features]
    y = df2[target]

    # Train the linear regression model with the entire dataset
    model = LinearRegression()
    model.fit(X, y)

    # Take user input
    user_input = objectify(ram,storage,yor,age, scrd,chrgav,keywork, batth)

    # Predict the selling price for the user input
    user_input_df = pd.DataFrame([user_input])
    user_pred = model.predict(user_input_df[features])

    predicted_price = user_pred[0]*0.7
    if(predicted_price<=100):
        predicted_price=100
    

    return(int(predicted_price))

