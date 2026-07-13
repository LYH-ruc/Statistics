import argparse
import copy
import numpy as np
import torch
import torch.nn as nn
from models import build_model
from data import (load_mnist, iid_partition, noniid_partition, make_client_loader,)

def client_update(model, loader, epochs: int, lr: float, device):
    model.train()
    optimizer = torch.optim.SGD(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()
    for _ in range(epochs):
        for x, y in loader:
            x, y = x.to(device), y.to(device)
            optimizer.zero_grad()
            loss = criterion(model(x), y)
            loss.backward()
            optimizer.step()
    return model.state_dict()

def average_weights(local_weights, local_sizes):
    total = float(sum(local_sizes))
    avg = copy.deepcopy(local_weights[0])
    for key in avg.keys():
        acc = torch.zeros_like(avg[key], dtype=torch.float32)
        for w, n in zip(local_weights, local_sizes):
            acc += w[key].float() * (n / total)
        avg[key] = acc.to(avg[key].dtype)
    return avg

@torch.no_grad()
def evaluate(model, loader, device):
    model.eval()
    correct, total = 0, 0
    for x, y in loader:
        x, y = x.to(device), y.to(device)
        pred = model(x).argmax(dim=1)
        correct += (pred == y).sum().item()
        total += y.size(0)
    return correct / total

def train(args):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    torch.manual_seed(args.seed)
    np.random.seed(args.seed)
 
    train_set, test_set = load_mnist(args.data_root)
    if args.iid:
        client_idxs = iid_partition(train_set, args.num_clients, args.seed)
    else:
        client_idxs = noniid_partition(train_set, args.num_clients, seed=args.seed)
    test_loader = torch.utils.data.DataLoader(test_set, batch_size=256, shuffle=False)

    global_model = build_model(args.model).to(device)
    global_weights = global_model.state_dict()
 
    m = max(int(args.frac * args.num_clients), 1) 
    print(f"设备={device} | 模型={args.model} | {'IID' if args.iid else 'Non-IID'} "
          f"| K={args.num_clients} C={args.frac} (每轮 {m} 个) E={args.epochs} B={args.batch_size}")
 
    rng = np.random.default_rng(args.seed)
 
    for rnd in range(1, args.rounds + 1):
        selected = rng.choice(args.num_clients, m, replace=False)
 
        local_weights, local_sizes = [], []
        for k in selected:
            idxs = client_idxs[k]
            loader = make_client_loader(train_set, idxs, args.batch_size)
 
            local_model = build_model(args.model).to(device)
            local_model.load_state_dict(global_weights)
            w = client_update(local_model, loader, args.epochs, args.lr, device)
 
            local_weights.append(w)
            local_sizes.append(len(idxs))
 
        global_weights = average_weights(local_weights, local_sizes)
        global_model.load_state_dict(global_weights)
 
        if rnd % args.eval_every == 0 or rnd == args.rounds:
            acc = evaluate(global_model, test_loader, device)
            print(f"[round {rnd:4d}] test accuracy = {acc*100:.2f}%")
 
    return global_model
 
 
def get_args():
    p = argparse.ArgumentParser(description="FedAvg (McMahan et al., 2017) on MNIST")
    p.add_argument("--model", default="cnn", choices=["mlp", "cnn"], help="2NN(mlp) 或 cnn")
    p.add_argument("--iid", action="store_true", help="加上则用 IID 划分, 默认 Non-IID")
    p.add_argument("--num_clients", type=int, default=100, help="客户端总数 K")
    p.add_argument("--frac", type=float, default=0.1, help="每轮参与比例 C")
    p.add_argument("--epochs", type=int, default=5, help="本地训练轮数 E")
    p.add_argument("--batch_size", type=int, default=10, help="本地 batch 大小 B (<=0 表示 B=∞)")
    p.add_argument("--lr", type=float, default=0.01, help="本地 SGD 学习率 η")
    p.add_argument("--rounds", type=int, default=100, help="通信总轮数 T")
    p.add_argument("--eval_every", type=int, default=1, help="每几轮在测试集上评估一次")
    p.add_argument("--data_root", default="./data")
    p.add_argument("--seed", type=int, default=42)
    return p.parse_args()
 
 
if __name__ == "__main__":
    train(get_args())