# Objective
To predict the stock prices for the next 30 days from the current date.

# Data Collection
The first step involves collecting stock data. In this project, Apple's stock prices from 2015 to the present a specific date are collected. The pandas_datareader library is used to fetch stock data from the Tiingo API. The necessary data is retrieved and stored in a DataFrame (DF). The data is then saved as a CSV file for future use.

# Data Preprocessing
After collecting the data, preprocessing is necessary to prepare it for training. This involves selecting a specific feature (e.g., closing price) for prediction, scaling the data using Min-Max scaling to bring it within a range of 0 to 1, and converting the DataFrame into an array.

# Train-Test Split
The data is split into training and testing sets. It's crucial to maintain the temporal order of the data when dealing with time series data. In this project, 65% of the data is used for training, and the remaining 35% is used for testing.

# Data Preprocessing for Modeling
After splitting the data, further preprocessing is done to prepare it for modeling. This involves creating sequences of input-output pairs based on a specified number of time steps. For example, if the time step is set to 3, the model will use data from the previous three days to predict the next day's price.

# Model Creation:
The LSTM (Long Short-Term Memory) model architecture is established.
The LSTM layers are stacked sequentially with a 4 number of hidden units.
The model is compiled with mean squared error as the loss function and Adam optimizer.

# Model Training:
The training data is reshaped to fit the LSTM model's input requirements.
The model is trained using the training data and evaluated using validation data.
The training process involves 100 epochs, with the goal of minimizing loss.

# Model Evaluation:
Performance metrics such as Root Mean Squared Error (RMSE) are calculated for both training and test data predictions.
The model's predictions are visualized against the actual data to assess accuracy. RSME on Train data is 140.99 while on test data is 235.71 

# Future Prediction:
The trained model is used to predict future values for a 10 number days.
Previous data is used as input to predict future values, and the process is iterated for the desired number of days.
Predictions are visualized alongside actual data to observe trends and accuracy.

# Model Improvement:
Suggestions are provided for improving model accuracy, such as adjusting the sequence length or exploring alternative model architectures like bidirectional LSTM.
