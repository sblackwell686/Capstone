import json
import pickle
import pandas as pd
import numpy as np

__data_columns = None
__model = None

def load_saved_artifacts():
   print("loading saved artifacts...start")
   global __data_columns, __model

   with open("./artifacts/columnsPhilly.json", 'r') as f:
       __data_columns = json.load(f)['data_columns']

   with open("./artifacts/Philadelphia_home_prices_model.pickle", 'rb') as f:
       __model = pickle.load(f)
   print("loading saved artifacts...done")

def price_predict(bed, bath, acre_lot, house_size):
   # Create a DataFrame with the input data
   input_data = pd.DataFrame({
       'bed': [bed],
       'bath': [bath],
       'acre_lot': [acre_lot],
       'house_size': [house_size],
       'city': ['Philadelphia']  # Hardcode the city value
   })

   # Generate dummy variables for the 'city' column
   dummiesP = pd.get_dummies(input_data['city'], dtype='int')

   # Drop the original 'city' column and join with the dummies
   input_data = input_data.drop('city', axis=1).join(dummiesP)

   # Ensure that the 'Philadelphia' column is present
   if 'Philadelphia' not in input_data.columns:
       input_data['Philadelphia'] = 0

   # Reorder the columns to match the training data
   feature_order = ['bed', 'bath', 'acre_lot', 'house_size', 'Philadelphia']
   X = input_data[feature_order]

   # Use the trained model to predict the price
   predicted_price = __model.predict(X)[0]

   # Round the predicted price to 2 decimal places
   rounded_price = round(predicted_price, 2)

   return rounded_price

if __name__ == '__main__':
   load_saved_artifacts()
   print("Booting main")


