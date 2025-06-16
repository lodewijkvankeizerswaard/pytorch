# Local development

## Recompiling the project
```bash
export CMAKE_PREFIX_PATH=${CONDA_PREFIX:-"$(dirname $(which conda))/../"}
python setup.py develop 
python setup.py install  # i do not know the difference between develop and install
``` 



## Installation
To be able to contribute to the pytorch project, we need to [install pytorch from source](https://github.com/pytorch/pytorch#from-source). 
	
## Discovery
We are looking to adapt the `randperm` function. Searching for randperm, we find the file `aten/src/ATen/native/native_function.yaml`, which contains:
```yaml
...

- func: randperm(SymInt n, *, ScalarType? dtype=long, Layout? layout=None, Device? device=None, bool? pin_memory=None) -> Tensor
  tags: [core, nondeterministic_seeded]
  dispatch:
    CompositeExplicitAutograd: randperm

- func: randperm.generator(SymInt n, *, Generator? generator, ScalarType? dtype=long, Layout? layout=None, Device? device=None, bool? pin_memory=None) -> Tensor
  tags: nondeterministic_seeded
  dispatch:
    CompositeExplicitAutograd: randperm

- func: randperm.out(SymInt n, *, Tensor(a!) out) -> Tensor(a!)
  tags: nondeterministic_seeded
  dispatch:
    CompositeExplicitAutograd: randperm_out

- func: randperm.generator_out(SymInt n, *, Generator? generator, Tensor(a!) out) -> Tensor(a!)
  tags: nondeterministic_seeded
  dispatch:
    CPU: randperm_out_cpu
    CUDA: randperm_out_cuda
    MPS: randperm_out_mps

...
```


## Interesting files
- `aten/src/ATen/native/cuda/Randperm.cu`
- 