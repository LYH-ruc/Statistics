import numpy as np
import torch
from torchvision import datasets, transforms

def load_mnist(root: str = "./data"):
    transform = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.1307,), (0.3081,)),])
    train = datasets.MNIST(root,train = True, download = True, transform=transform)
    test = datasets.MNIST(root, train=False, download=True, transform=transform)
    return train, test

def iid_partition(dataset, num_clients: int, seed: int = 0):
    rng = np.random.default_rng(seed)
    idxs = rng.permutation(len(dataset))
    shards = np.array_split(idxs, num_clients)
    return {i: shards[i].tolist() for i in range(num_clients)}

def noniid_partition(dataset, num_clients: int, shards_per_client: int = 2, seed: int = 0):
    rng = np.random.default_rng(seed)
    labels = np.array(dataset.targets)
    idxs = np.argsort(labels) 
    num_shards = num_clients * shards_per_client
    shard_size = len(dataset) // num_shards
    shards = [idxs[i * shard_size:(i + 1) * shard_size] for i in range(num_shards)]
    shard_ids = rng.permutation(num_shards)
    client_idxs = {}
    for c in range(num_clients):
        chosen = shard_ids[c * shards_per_client:(c + 1) * shards_per_client]
        client_idxs[c] = np.concatenate([shards[s] for s in chosen]).tolist()
    return client_idxs

def make_client_loader(dataset, idxs, batch_size: int):
    subset = torch.utils.data.Subset(dataset, idxs)
    if batch_size is None or batch_size <= 0:
        batch_size = len(idxs)
    return torch.utils.data.DataLoader(subset, batch_size=batch_size, shuffle=True)