# Numpy Starting


```python
import numpy as np
print(np.__version__)
```

    1.25.2
    


```python
a=np.arange(10)
print(a)
print(type(a))
```

    [0 1 2 3 4 5 6 7 8 9]
    <class 'numpy.ndarray'>
    

### Numpy array is much faster than list


```python
l=list(range(1000))
%timeit [i*2 for i in l]
```

    50.5 µs ± 1.49 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
    


```python
t=np.arange(1000)
%timeit np.array(i*2 for i in t)
```

    3.17 µs ± 119 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
    


```python
arr=np.array([1,2,3])
print(arr)
print(type(arr))#type
print(arr.ndim)#Dimesions
print(arr.shape)#Shape
print(len(arr))
```

    [1 2 3]
    <class 'numpy.ndarray'>
    1
    (3,)
    3
    


```python
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print(type(arr))#type
print(arr.ndim)#Dimesions
print(arr.shape)#Shape
print(len(arr))
```

    [[1 2 3]
     [4 5 6]]
    <class 'numpy.ndarray'>
    2
    (2, 3)
    2
    

## Day 2 (28/8/23)

### Linspace Function


```python
d=np.linspace(0,1,9)
print(d)
```

    [0.    0.125 0.25  0.375 0.5   0.625 0.75  0.875 1.   ]
    

#### How to generate identity matrix | D-Type function


```python
a=np.ones((3,3))
print(a)
print(a.dtype)
```

    [[1. 1. 1.]
     [1. 1. 1.]
     [1. 1. 1.]]
    float64
    


```python
a=np.zeros((3,3))
print(a)
print(a.dtype)
```

    [[0. 0. 0.]
     [0. 0. 0.]
     [0. 0. 0.]]
    float64
    


```python
f=np.eye(3)
print(f)
g=np.eye((2,3))#It will show an error
print(g)
```

    [[1. 0. 0.]
     [0. 1. 0.]
     [0. 0. 1.]]
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[4], line 3
          1 f=np.eye(3)
          2 print(f)
    ----> 3 g=np.eye((2,3))#It will show an error
          4 print(g)
    

    File D:\Installation\Python\Lib\site-packages\numpy\lib\twodim_base.py:211, in eye(N, M, k, dtype, order, like)
        209 if M is None:
        210     M = N
    --> 211 m = zeros((N, M), dtype=dtype, order=order)
        212 if k >= M:
        213     return m
    

    TypeError: 'tuple' object cannot be interpreted as an integer



```python
g=np.diag([1,2,3,4])
print(g)
```

    [[1 0 0 0]
     [0 2 0 0]
     [0 0 3 0]
     [0 0 0 4]]
    


```python
j=np.arange(10,dtype='float')
print(j)
print(j.dtype)

```

    [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
    float64
    

### Slicing and indexing in numpy array


```python
a=np.arange(10)
b=a[::2]
print(b)
print(a)
print(id(a),id(b))
b[0]=55
print(a,b)
print(np.shares_memory(a,b))
```

    [0 2 4 6 8]
    [0 1 2 3 4 5 6 7 8 9]
    2223318107312 2223318107024
    [55  1  2  3  4  5  6  7  8  9] [55  2  4  6  8]
    True
    


```python
a=np.arange(10)
b=a[::2].copy()
print(b)
print(a)
print(id(a),id(b))
b[0]=55
print(a,b)
print(np.shares_memory(a,b))
```

    [0 2 4 6 8]
    [0 1 2 3 4 5 6 7 8 9]
    2223317860144 2223318117776
    [0 1 2 3 4 5 6 7 8 9] [55  2  4  6  8]
    False
    

#### Random Function


```python
a=np.random.randint(0,100,10)
print(a)
```

    [68 10 78  2 10 19 39 56  3 99]
    

### Masking


```python
a=np.random.randint(0,100,10)
print(a)
mask=(a%2==0)
print(mask)
print(a[mask])
a[mask]=-1
print(a[mask])


```

    [ 9 24 74 44 88 29  7 64 57 11]
    [False  True  True  True  True False False  True False False]
    [24 74 44 88 64]
    [-1 -1 -1 -1 -1]
    


```python
a=np.random.randint(0,100,10)
a[[0,1,2,3]]=111
print(a)
a[[i for i in range(7)]]=555
print(a)
```

    [111 111 111 111  55  73  41  57  60  77]
    [555 555 555 555 555 555 555  57  60  77]
    

### Arthmetic Operation on numpy array

Element wise scaler addition, multiplication, power, division


```python
a=np.random.randint(0,10,6)
print(a)
print(a+1)
print(a*2)
print(a**2)
print(a/2)
```

    [3 9 5 8 4 1]
    [ 4 10  6  9  5  2]
    [ 6 18 10 16  8  2]
    [ 9 81 25 64 16  1]
    [1.5 4.5 2.5 4.  2.  0.5]
    


```python
a=np.linspace(0,1,5)
print(a)
print(a+1)
print(a*2)
print(a**2)
print(a/2)
```

    [0.   0.25 0.5  0.75 1.  ]
    [1.   1.25 1.5  1.75 2.  ]
    [0.  0.5 1.  1.5 2. ]
    [0.     0.0625 0.25   0.5625 1.    ]
    [0.    0.125 0.25  0.375 0.5  ]
    


```python
a=np.ones((3,3),dtype='int')*3
print(a)
```

    [[3 3 3]
     [3 3 3]
     [3 3 3]]
    


```python
b=np.diag([1,2,3])
print(a+b)
```

    [[4 3 3]
     [3 5 3]
     [3 3 6]]
    

#### Element wise multiplication of arrays


```python
a=np.ones((3,3),dtype='int')*3
# print(a)
b=np.diag([1,2,3])
# print(a+b)
print(a*b)

```

    [[3 0 0]
     [0 6 0]
     [0 0 9]]
    


```python
import matplotlib.pyplot as plt
import numpy as np
a=np.arange(100)
b=np.sin(a)
plt.plot(b)
plt.show()
```


    
![png](output_33_0.png)
    


>axis 0 means column and 1 means row

#### Standard Deviation, Mean and Median


```python
x=np.array([[1,2],[3,4]])
print(x.sum())
print(x.sum(axis=0))
print(x.std())#standard Deviation
print(np.median(x))#median
print(x.mean())#mean

```

    10
    [4 6]
    1.118033988749895
    2.5
    2.5
    

### Text File in loading in numpy and manipulating

#### Transpose of matrix


```python
data=np.loadtxt('population.txt')
print(data)
year,hares,lynx,carrot=data.T#Transpose the matrix
print(year)
```

    [[ 1900. 30000.  4000. 48300.]
     [ 1901. 47200.  6100. 48200.]
     [ 1902. 70200.  9800. 41500.]
     [ 1903. 77400. 35200. 38200.]
     [ 1904. 36300. 59400. 40600.]
     [ 1905. 20600. 41700. 39800.]
     [ 1906. 18100. 19000. 38600.]
     [ 1907. 21400. 13000. 42300.]
     [ 1908. 22000.  8300. 44500.]
     [ 1909. 25400.  9100. 42100.]
     [ 1910. 27100.  7400. 46000.]
     [ 1911. 40300.  8000. 46800.]
     [ 1912. 57000. 12300. 43800.]
     [ 1913. 76600. 19500. 40900.]
     [ 1914. 52300. 45700. 39400.]
     [ 1915. 19500. 51100. 39000.]
     [ 1916. 11200. 29700. 36700.]
     [ 1917.  7600. 15800. 41800.]
     [ 1918. 14600.  9700. 43300.]
     [ 1919. 16200. 10100. 41300.]
     [ 1920. 24700.  8600. 47300.]]
    [1900. 1901. 1902. 1903. 1904. 1905. 1906. 1907. 1908. 1909. 1910. 1911.
     1912. 1913. 1914. 1915. 1916. 1917. 1918. 1919. 1920.]
    
```
