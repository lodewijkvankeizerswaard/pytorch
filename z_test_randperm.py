# import torch
# import torch._dynamo

# @torch.compile(backend="eager", fullgraph=True)
# def fn(x):
#     return torch.functional.split(x, 0)

# fn(torch.empty((0,)))

import torch

my_tensor = torch.tensor([complex('nan'), complex('inf-infj'), complex('-inf+infj'), 4.+0.j])
                                    # ↓       # ↓       # ↓
print("1" + '#'*30)
res = torch.nan_to_num(input=my_tensor, nan=1, posinf=2, neginf=3)
# tensor([1.+0.j, 2.+3.j, 3.+2.j, 4.+0.j])
print(f"result = {res}")
print("2" + '#'*30)
                                    # ↓↓       # ↓↓       # ↓↓
res = torch.nan_to_num(input=my_tensor, nan=1., posinf=2., neginf=3.)
# tensor([1.+0.j, 2.+3.j, 3.+2.j, 4.+0.j])
print(f"result = {res}")
print("3" + '#'*30)
                                    # ↓↓↓↓       # ↓↓↓↓↓       # ↓↓↓↓
res = torch.nan_to_num(input=my_tensor, nan=True, posinf=False, neginf=True)
# tensor([1.+0.j, 0.+1.j, 1.+0.j, 4.+0.j])
print(f"result = {res}")
print("4" + '#'*30)
                                    # ↓↓↓↓↓↓       # ↓↓↓↓↓↓       # ↓↓↓↓↓↓
res = torch.nan_to_num(input=my_tensor, nan=1.+0.j, posinf=2.+0.j, neginf=3.+0.j)
# tensor([1.+0.j, 2.+0.j, 3.+0.j, 4.+0.j])
print(f"result = {res}")