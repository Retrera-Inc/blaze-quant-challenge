import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from io import StringIO

# Load the data
data = """
Date,Price,Open,High,Low,Vol.,Change,Yesterday Price,Tomorrow Price,30 Day Average,7 Day Average,10-day SMA,20-day SMA,50-day SMA,12-day EMA,26-day EMA,50-day EMA
2023-02-19,1681.52,1691.62,1722.28,1670.97,427.00,-0.6,1691.62,1703.27,1611.8296666666668,1634.9271428571428,1601.209,1616.138,1523.8570000000002,1630.0222643068137,1596.1823406530568,1526.7915607617883
2023-02-20,1703.27,1681.49,1719.10,1651.54,478.59,1.29,1681.52,1659.41,1614.421,1663.1314285714286,1620.154,1622.038,1533.9119999999998,1641.29114672115,1604.1147598639413,1533.7122838691691
2023-02-21,1659.41,1703.29,1716.35,1637.16,554.52,-2.58,1703.27,1643.39,1615.5003333333334,1677.9814285714285,1632.261,1622.9035,1542.8216,1644.078662610204,1608.2107035777235,1538.6416060703782
2023-02-22,1643.39,1659.41,1666.39,1600.79,560.40,-0.97,1659.41,1650.52,1616.062333333333,1673.4042857142856,1645.056,1622.9875000000002,1551.398,1643.9727145163265,1610.8165773867809,1542.7493862244812
2023-02-23,1650.52,1643.39,1678.20,1630.94,529.75,0.43,1643.39,1608.24,1619.208,1674.812857142857,1659.524,1622.324,1559.27,1644.9799892061224,1613.7575716544266,1546.9756848039133
2023-02-24,1608.24,1650.52,1663.82,1579.68,548.07,-2.56,1650.52,1594.66,1619.1093333333333,1662.567142857143,1664.8020000000001,1619.391,1566.4158000000002,1639.327683174411,1613.3488626429876,1549.3782069684657
2023-02-25,1594.66,1608.24,1608.62,1562.10,309.29,-0.84,1608.24,1641.60,1618.8463333333336,1648.7157142857143,1656.725,1617.652,1572.9261999999999,1632.4557319168093,1611.9645024472106,1551.1539635579377
2023-02-26,1641.60,1594.66,1648.77,1588.65,326.58,2.94,1594.66,1633.66,1620.3129999999999,1643.0128571428572,1656.819,1619.0459999999998,1580.4802000000002,1633.8625423911462,1614.159724488158,1554.7008669478223
2023-02-27,1633.66,1641.59,1664.98,1609.82,458.53,-0.48,1641.60,1604.69,1622.3326666666665,1633.0685714285714,1650.789,1617.159,1587.3858000000002,1633.8313820232777,1615.604189340887,1557.7973035381037
2023-02-28,1604.69,1633.66,1646.33,1598.67,411.49,-1.77,1633.66,1666.09,1620.9566666666665,1625.2514285714285,1642.096,1614.844,1593.0693999999996,1629.3480924812347,1614.7957308711916,1559.6362328111193
2023-03-01,1666.09,1604.69,1668.55,1595.40,497.12,3.83,1604.69,1647.38,1624.276333333333,1628.4942857142855,1640.5529999999999,1620.8809999999999,1599.6886000000002,1635.0006936379677,1618.5953063622144,1563.810890347938
"""

# Load data into a pandas DataFrame
df = pd.read_csv(StringIO(data))

# Extract relevant columns
data = df[['Price', 'Open', 'High', 'Low', 'Vol.', 'Change', 'Yesterday Price', '30 Day Average', '7 Day Average', '10-day SMA', '20-day SMA', '50-day SMA', '12-day EMA', '26-day EMA', '50-day EMA']]

# Normalize the data
scaler = MinMaxScaler()
data_normalized = scaler.fit_transform(data)

# Convert data to PyTorch tensors
sequences = torch.tensor(data_normalized[:-1], dtype=torch.float32)
target = torch.tensor(data_normalized[1:, 0], dtype=torch.float32)

# Reshape data for LSTM input
sequences = sequences.view(-1, 1, sequences.size(1))

# Define the LSTM model
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.fc(out[:, -1, :])
        return out

# Initialize the model
input_size = data.shape[1]
hidden_size = 50
output_size = 1
model = LSTMModel(input_size, hidden_size, output_size)

# Define loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training the model
epochs = 50
for epoch in range(epochs):
    outputs = model(sequences)
    loss = criterion(outputs.squeeze(), target)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

# Predictions for the next 7 days
with torch.no_grad():
    last_sequence = sequences[-1].view(1, 1, -1)
    predictions = []

    for _ in range(7):
        next_day = model(last_sequence)
        predictions.append(next_day.item())
        last_sequence = torch.cat((last_sequence[:, :, 1:], next_day.view(1, 1, -1)), dim=2)

# Inverse transform the predictions to get the actual prices
predictions = np.array(predictions).reshape(1, 7)  # Reshape to (1, 7)
predictions = scaler.inverse_transform(predictions)

# Display the predictions
print("Predictions for the next 7 days:")
for i, pred in enumerate(predictions[0]):
    print(f"Day {i+1}: {pred:.2f}")

