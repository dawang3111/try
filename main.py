import numpy as np
import torch
import torch.nn as nn
from tqdm import tqdm
import time

# b = torch.IntTensor(6, 3)
# print(b)
# print(list(range(0, b.shape[1])))
# c = b[:, :-1]
# print(c)
# print(list(range(c.shape[1])))
# text = ""
# pbar = tqdm(range(55156))
# for i in pbar:
#     # print(i)
#     a = 464443161*845113131
#     pbar.set_description("train loss: %.1f" %i)
# a = np.array([[2, 3, 4], [1, 2, 3]])
# print(a)
# b = torch.FloatTensor([[2, 3, 4], [1, 2, 3]])
# print(b)
c = []
a1 = torch.FloatTensor(9)
a2 = torch.FloatTensor(9)
a3 = torch.FloatTensor(1,9)
print(a1)
print(a2)
print(a3)
c.append(a1)
c.append(a2)
print(c)
b = torch.cat(c, dim=0).numpy()
print(b)
