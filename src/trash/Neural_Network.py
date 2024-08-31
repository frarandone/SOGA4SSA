import torch
from torch import nn

class NeuralNetwork(nn.Module):
    def __init__(self, num_component_input=2, num_component_output=2):
        super(NeuralNetwork, self).__init__()
        self.num_component_input = num_component_input
        self.num_component_output = num_component_output
        self.flatten = nn.Flatten()
        self.network = nn.Sequential(
            nn.Linear(6, 24),
            nn.ReLU(),
            nn.Linear(24, 48),
            nn.ReLU(),
            nn.Linear(48,6)
        )

    def forward(self, x):
        output = self.network(x)
        pi = output[:, 0:self.num_component_output]
        mu = output[:, self.num_component_output:2*self.num_component_output]
        sigma = output[:, 2*self.num_component_output:3*self.num_component_output]

        pi = torch.softmax(pi, dim=1)
        sigma = torch.exp(sigma)
        mu = torch.exp(mu)

        return mu, pi, sigma

