from numba import jit,cuda
import numpy as np
from timeit import default_timer as timer


def func_cpu(a):
    for i in range(10_000_000):
        a[i]+=1

@jit(target_backend='cuda')
def func_gpu(a):
    for i in range(10_000_000):
        a[i]+=1

if __name__ == '__main__':
    n = 10_000_000
    a = np.ones(n,dtype=np.float64)

    start = timer()
    func_cpu(a)
    print(f"funkcja uruchomiona na CPU: {timer()-start} s")

    start = timer()
    func_gpu(a)
    print(f"funkcja uruchomiona na GPU: {timer() - start} s")
