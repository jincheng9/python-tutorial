# Lecture 1: Series数据结构

## Series定义

```python
class pandas.Series(data=None, index=None, dtype=None, name=None, copy=None, fastpath=_NoDefault.no_default)
	One-dimensional ndarray with axis labels (including time series).

  Labels need not be unique but must be a hashable type. The object supports both integer- and label-based indexing and provides a host of methods for performing operations involving the index. Statistical methods from ndarray have been overridden to automatically exclude missing data (currently represented as NaN).

  Operations between Series (+, -, /, *, **) align values based on their associated index values– they need not be the same length. The result index will be the sorted union of the two indexes.

  Parameters:
    data: array-like, Iterable, dict, or scalar value
      Contains data stored in Series. If data is a dict, argument order is maintained.

    index: array-like or Index (1d)
      Values must be hashable and have the same length as data. Non-unique index values are allowed. Will default to RangeIndex (0, 1, 2, …, n) if not provided. If data is dict-like and index is None, then the keys in the data are used as the index. If the index is not None, the resulting Series is reindexed with the index values.

    dtype: str, numpy.dtype, or ExtensionDtype, optional
      Data type for the output Series. If not specified, this will be inferred from data. See the user guide for more usages.

    name: Hashable, default None
    	The name to give to the Series.

    copy: bool, default False
    	Copy input data. Only affects Series or 1d ndarray input. See examples.
```

Series是Pandas里非常重要的数据结构，可以把Series理解为带有索引的一维数组。

## Series创建

Series创建有如下核心参数：

* 入参data：Series里的元素值。入参data可以是标量(scalar)，可以是类似数组的类型(比如Python里的list和tuple, NumPy的一维ndarray)，也可以是dict。
* 入参index：Series的索引。入参index可以是一个类似数组(array-like)的类型，比如list或者tuple，也可以不传。
* 入参dtype: Series的类型，可以是python里的数据类型，如int, str, bool等，也可以是numpy里的数据类型，如numpy.int8, numpy.int16等。
* 入参name: Series的名字。一个是增加数据的可读性，在处理大量Series变量时，有时候根据Series的名字就能快速知道Series的含义。另外在Series转换为DataFrame时，Series的name可以自动作为DataFrame的列名。
* 入参copy：
  * **`copy=True`**：创建原始数据的副本。这意味着，如果原始数据之后发生更改，这些更改不会反映到你创建的`Series`上，反之亦然。
  * **`copy=False`**（默认值）：如果可能，不创建原始数据的副本。这意味着新创建的`Series`可能只是原始数据的一个视图(view)。在这种情况下，改变`Series`中的数据可能会影响原始数据，而原始数据的更改也可能反映到`Series`中。




Series创建的时候根据data和index这2个入参的搭配，有不同的效果。

* data为None

  * index为None，这种情况下就是个空的Series。

    ```bash
    In [111]: s = pd.Series()
    
    In [112]: s.size
    Out[112]: 0
    
    In [113]: s
    Out[113]: Series([], dtype: object)
    ```

    

  * index有值，这种情况下虽然data为None，但是Series非空。

    ```bash
    In [108]: s3 = pd.Series(index=['a','b'])
    
    In [109]: s3
    Out[109]: 
    a   NaN
    b   NaN
    dtype: float64
    
    In [110]: s3.size
    Out[110]: 2
    ```

    

* data为scalar标量

  * index为None。这种情况下index是默认的整数索引，从0开始编号。

    ```bash
    In [114]: s = pd.Series(1)
    
    In [115]: s
    Out[115]: 
    0    1
    dtype: int64
    
    In [116]: s.size
    Out[116]: 1
    
    In [117]: s.iloc[0]
    Out[117]: 1

  * index有值。这种情况下可以通过索引来访问或者通过iloc来访问。

    ```bash
    In [118]: s = pd.Series(1, index=['a'])
    
    In [119]: s
    Out[119]: 
    a    1
    dtype: int64
    
    In [120]: s.size
    Out[120]: 1
    
    In [121]: s.iloc[0]
    Out[121]: 1
    
    In [272]: s = pd.Series(1, index=['20240915','20240916','20240917'])
    
    In [273]: s
    Out[273]: 
    20240915    1
    20240916    1
    20240917    1
    dtype: int64
    
    # (1)不是tuple，实际上就是1，是个scalar
    In [275]: s = pd.Series((1), index=['20240915','20240916','20240917'])
    
    In [276]: s
    Out[276]: 
    20240915    1
    20240916    1
    20240917    1
    dtype: int64
    ```
    
    

* data为array-like的类型

  * index为None。这种情况下index是默认的整数索引，从0开始编号。

    ```bash
    In [122]: s = pd.Series([1,2,3])
    
    In [123]: s
    Out[123]: 
    0    1
    1    2
    2    3
    dtype: int64
    
    In [124]: s.size
    Out[124]: 3

  * index有值。这种情况下index的长度必须和array-like的data的长度一致，否则会报错。

    ```bash
    In [125]: s = pd.Series([1,2,3], index=['a', 'b', 'c'])
    
    In [126]: s
    Out[126]: 
    a    1
    b    2
    c    3
    dtype: int64
    
    In [127]: s.size
    Out[127]: 3
    ```

    长度不一致的报错如下：

    ```bash
    In [128]: s = pd.Series([1,2,3], index=['a', 'b'])
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    Cell In[128], line 1
    ----> 1 s = pd.Series([1,2,3], index=['a', 'b'])
    
    File /opt/anaconda3/lib/python3.12/site-packages/pandas/core/series.py:575, in Series.__init__(self, data, index, dtype, name, copy, fastpath)
        573     index = default_index(len(data))
        574 elif is_list_like(data):
    --> 575     com.require_length_match(data, index)
        577 # create/copy the manager
        578 if isinstance(data, (SingleBlockManager, SingleArrayManager)):
    
    File /opt/anaconda3/lib/python3.12/site-packages/pandas/core/common.py:573, in require_length_match(data, index)
        569 """
        570 Check the length of data matches the length of the index.
        571 """
        572 if len(data) != len(index):
    --> 573     raise ValueError(
        574         "Length of values "
        575         f"({len(data)}) "
        576         "does not match length of index "
        577         f"({len(index)})"
        578     )
    
    ValueError: Length of values (3) does not match length of index (2)
    ```

    

* data为dict

  * index为None。这种情况下dict的key是Series的index。

    ```bash
    In [129]: s = pd.Series({'a':1, 'b':2, 'c': 3})
    
    In [130]: s
    Out[130]: 
    a    1
    b    2
    c    3
    dtype: int64
    ```

    

  * index有值。这种情况下会根据index的值匹配生成对应的Series。

    ```bash
    In [131]: s = pd.Series({'a':1, 'b':2, 'c': 3}, index=['a', 'd'])
    
    In [132]: s
    Out[132]: 
    a    1.0
    d    NaN
    dtype: float64
    
    In [133]: s = pd.Series({'a':1, 'b':2, 'c': 3}, index=['d'])
    
    In [134]: s
    Out[134]: 
    d   NaN
    dtype: float64
    
    In [135]: s.size
    Out[135]: 1
    ```

  * dict里的key顺序也是最后Series里的元素顺序。

    ```bash
    In [148]: s = pd.Series({'d':4, 'b':1, 'a':2, 'c': 3})
    
    In [149]: s
    Out[149]: 
    d    4
    b    1
    a    2
    c    3
    dtype: int64
    ```

    

## Series访问

Series访问有访问一个元素和多个元素。

### 访问其中一个元素

* 根据索引访问：s[index]，这是推荐用法

  ```bash
  In [150]: s = pd.Series({'d':4, 'b':1, 'a':2, 'c': 3})
  
  In [151]: s['a']
  Out[151]: 2
  ```

* 根据索引访问：s.loc[index]，和上面的效果一样

  ```bash
  In [248]: s = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
  
  In [249]: s.loc['d']
  Out[249]: 4
  
  In [251]: s['d']
  Out[251]: 4
  ```

* 根据位置访问：s.iloc[position]

  ```bash
  In [150]: s = pd.Series({'d':4, 'b':1, 'a':2, 'c': 3})
  
  In [153]: s.iloc[1] # Series第二个元素
  Out[153]: 1
  
  In [160]: s.iloc[-1] # Series最后一个元素
  Out[160]: 3
  
  In [152]: s[1] # 这种方式要被废弃
  <ipython-input-152-f8bb2b116405>:1: FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
    s[1]
  Out[152]: 1
  ```

  

### 访问其中多个元素

* 根据索引访问：

  ```bash
  In [257]: s = pd.Series({'d':4, 'b':1, 'a':2, 'c': 3})
  ## :切片访问，返回的是2个索引之间的所有元素组成的Series，左右都是闭区间。
  In [154]: s['d':'a']
  Out[154]: 
  d    4
  b    1
  a    2
  dtype: int64
  ## 返回的是索引为'a'和'd'的元素组成的Series
  In [256]: s[['a','d']]
  Out[256]: 
  a    2
  d    4
  dtype: int64

* 根据索引访问：使用loc属性来访问，同上面

  ```bash
  In [252]: s = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
  
  ## 返回的是索引为'a'和'd'的元素组成的Series
  In [253]: s.loc[['a', 'd']]
  Out[253]: 
  a    1
  d    4
  dtype: int64
  
  ## :切片访问，返回的是2个索引之间的所有元素组成的Series，左右都是闭区间。
  In [255]: s.loc['b':'d']
  Out[255]: 
  b    2
  c    3
  d    4
  dtype: int64
  ```

  

* 根据位置访问：左开右闭

  ```bash
  In [257]: s = pd.Series({'d':4, 'b':1, 'a':2, 'c': 3})
  In [156]: s[0:3]
  Out[156]: 
  d    4
  b    1
  a    2
  dtype: int64
  
  In [158]: s[:3]
  Out[158]: 
  d    4
  b    1
  a    2
  dtype: int64
  ```

* 根据位置访问：使用iloc来访问，同上面

  ```bash
  In [259]: s = pd.Series({'d':4, 'b':1, 'a':2, 'c': 3})
  
  In [260]: s.iloc[0:3]
  Out[260]: 
  d    4
  b    1
  a    2
  dtype: int64
  
  In [261]: s.iloc[:3]
  Out[261]: 
  d    4
  b    1
  a    2
  dtype: int64
  
  In [262]: s.iloc[[1,2]] # 获取位置为1和2的元素
  Out[262]: 
  b    1
  a    2
  dtype: int64
  ```

  

### 遍历Series

```bash
In [161]: for i in s:
     ...:     print(i)
     ...: 
4
1
2
3

In [162]: for k, v in s.items():
     ...:     print(k, v)
     ...: 
d 4
b 1
a 2
c 3
```

### 获取Series的索引和值

```bash
In [187]: s = pd.Series({'d':4, 'b':1, 'a':2, 'c': 3})

In [188]: s.index
Out[188]: Index(['d', 'b', 'a', 'c'], dtype='object')

In [189]: s.values
Out[189]: array([4, 1, 2, 3])

In [190]: for i in s.index:
     ...:     print(i)
     ...: 
d
b
a
c
```



## Series修改

### 增加元素

* 通过新的索引增加元素

```bash
In [175]: s = pd.Series({'d':4, 'b':1, 'a':2, 'c': 3})

In [176]: s['e'] = 5
```

* 通过concat函数增加元素

  ```bash
  In [216]: s = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
  
  In [217]: s2 = pd.Series([5,6], index=['e', 'f'])
  
  In [218]: s3 = pd.concat([s, s2])
  
  In [219]: s3
  Out[219]: 
  a    1
  b    2
  c    3
  d    4
  e    5
  f    6
  dtype: int64
  
  In [220]: s3 = pd.concat([s, s2]).reset_index(drop=True)
  
  In [221]: s3
  Out[221]: 
  0    1
  1    2
  2    3
  3    4
  4    5
  5    6
  dtype: int64
  ```

  使用`reset_index(drop=True)`是为了重建一个简单的整数索引。

* 可以把Series转换为list后，通过list增加元素，然后再转化回Series。

  ```bash
  In [225]: s = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
  
  In [226]: s
  Out[226]: 
  a    1
  b    2
  c    3
  d    4
  dtype: int64
  
  In [227]: s_list = s.tolist()
  
  In [228]: s_list
  Out[228]: [1, 2, 3, 4]
  
  In [229]: s_list.append(5)
  
  In [230]: s_list
  Out[230]: [1, 2, 3, 4, 5]
  
  In [231]: s_new = pd.Series(s_list)
  
  In [232]: s_new
  Out[232]: 
  0    1
  1    2
  2    3
  3    4
  4    5
  dtype: int64
  ```

  

* **注意**: Series的append函数在pandas 2.0版本里被删除了。

### 删除元素

* 删除`Series`中的元素通常使用`.drop()`方法。这个方法能够根据索引标签删除`Series`中的一个或多个项，并返回一个新的`Series`对象，而不会就地修改原始的`Series`。

  ```bash
  In [233]: s
  Out[233]: 
  a    1
  b    2
  c    3
  d    4
  dtype: int64
  
  In [234]: s_new = s.drop(['a', 'c'])
  
  In [235]: s_new
  Out[235]: 
  b    2
  d    4
  dtype: int64
  
  In [236]: s
  Out[236]: 
  a    1
  b    2
  c    3
  d    4
  dtype: int64
  ```

  - 在调用`.drop()`方法时，如果传递的索引在`Series`中不存在，它会抛出`KeyError`。如果你不确定索引是否存在，或者你希望在索引不存在时简单地忽略这个操作，可以使用参数`errors='ignore'`。

  ```bash
  # 安全删除，忽略不存在的索引
  s_new = s.drop('z', errors='ignore')
  print(s_new)
  ```

* 使用del删除Series里的元素，会修改原始的Series。

```bash
In [181]: s
Out[181]: 
d    4
b    1
a    2
c    3
dtype: int64

In [241]: del s['a']

In [242]: s
Out[242]: 
b    2
c    3
d    4
dtype: int64
```

### 修改元素

```bash
In [615]: s = pd.Series([1,2], index=['r1', 'r2'])

In [616]: s
Out[616]: 
r1    1
r2    2
dtype: int64

In [617]: s['r1'] = 10

In [618]: s
Out[618]: 
r1    10
r2     2
dtype: int64

In [619]: s.loc['r1'] = 20

In [620]: s
Out[620]: 
r1    20
r2     2
dtype: int64

In [621]: s.iloc[0] = 30

In [622]: s
Out[622]: 
r1    30
r2     2
dtype: int64
```



## Series索引

* Series有自己的索引，可以通过索引来访问Series里的元素。

* Series的索引可以重复，比如下面的代码示例：

  ```bash
  In [193]: s = pd.Series([1,2,3,4], index=['a','a','b','c'])
  
  In [194]: s
  Out[194]: 
  a    1
  a    2
  b    3
  c    4
  dtype: int64
  
  In [195]: s['a']
  Out[195]: 
  a    1
  a    2
  dtype: int64
  ```


**注：**iloc的i代表 "integer"，意味着 "integer-location based"。这表示`iloc`用于基于整数位置（从 0 开始的索引）的索引，让你可以通过整数的位置来访问Series或DataFrame中的数据。这种索引方式与Python及其使用整数作为索引的数据结构（例如列表）保持一致，对数据进行位置上的直接选择。

## References

* https://pandas.pydata.org/docs/reference/api/pandas.Series.html