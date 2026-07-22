import torch
import torch.nn as nn
import torch.optim as optim

# Example dataset
X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])

# Linear regression model: y = wx + b
model = nn.Linear(in_features=1, out_features=1)

criterion = nn.MSELoss()          # Mean Squared Error
optimizer = optim.SGD(model.parameters(), lr=0.01)

for epoch in range(1000):
    # Forward pass
    y_pred = model(X)
    loss = criterion(y_pred, y)

    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print("Final parameters:", list(model.parameters()))

X_test = torch.tensor([[5.0]])
y_test = model(X_test)
print("Prediction for x=5:", y_test.item())
