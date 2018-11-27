import torch
import torch.nn as nn
torch.set_default_tensor_type(torch.DoubleTensor)

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()

    def create_input_layer(self, input_formatter):
        self.layers = nn.ModuleList()
        self.layers.append(nn.Linear(input_formatter.get_input_state_dimension(), 64))

    def create_hidden_layers(self):
        self.layers.append(nn.Linear(64, 64))
        self.layers.append(nn.Linear(64, 64))
        self.layers.append(nn.Linear(64, 64))

    def create_output_layer(self, output_formatter):
        self.layers.append(nn.Linear(64, output_formatter.get_model_output_dimension()))

    def finalize_model(self, lr=0.1):
        self.optimizer=torch.optim.Adam(self.parameters(), lr=lr)
        self.loss=nn.MSELoss()

    def predict(self, arr):
        for layer in self.layers[:-1]:
            arr=nn.functional.softplus(layer(arr))

        arr=nn.functional.softmax(self.layers[-1](arr))
        return arr

    def fit(self, x, target, epochs=1):
        for _ in range(epochs):
            for i in range(len(x)):
                self.optimizer.zero_grad()
                action=self.predict(x[i])
                loss=self.loss(action, target[i])
                loss.backward()
                self.optimizer.step()
        return loss

    def save(self, filepath):
        pass
    def load(self, filepath):
        pass
