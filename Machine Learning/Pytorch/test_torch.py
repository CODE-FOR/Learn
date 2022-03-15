import torch
import numpy as np

print(torch.cuda.is_available())

x = torch.tensor([1, 2])
print(x)

y = torch.rand_like(x, dtype=torch.double)
y = y.to('cuda')
print(y.device)