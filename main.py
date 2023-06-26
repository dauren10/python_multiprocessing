from multiprocessing import Pool
from time import sleep

def f(x):
    sleep(20)
    return x * x


if __name__ == '__main__':
    with Pool(20) as p:
        print(p.map(f,[1,2,3]))
