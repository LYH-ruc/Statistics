import torch.nn as nn
import torch.nn.functional as F

class MLP(nn.Module):
    def __init__(self, num_classes = 10):
        super().__init__()
        self.fc1 = nn.Linear(784,200)
        self.fc2 = nn.Linear(200,200)
        self.fc3 = nn.Linear(200,num_classes)

    def forward(self, x):
        x = x.view(x.size(0),-1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return self.fc3(x)
    
class CNN(nn.Module):
    def __init__(self, num_classes:int = 10):
        super().__init__()
        self.conv1 = nn.Conv2d(1,32,kernel_size=5,padding=2)
        self.conv2 = nn.Conv2d(32,64,kernel_size=5,padding=2)
        self.fc1 = nn.Linear(64*7*7,512)
        self.fc2 = nn.Linear(512,num_classes)
        
    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), 2)
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(x.size(0),-1)
        x = F.relu(self.fc1(x))
        return self.fc2(x)