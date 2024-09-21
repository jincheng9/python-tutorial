# Lecture 2: DataFrame数据结构

## DataFrame定义

```python
class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)
    Two-dimensional, size-mutable, potentially heterogeneous tabular data.

    Data structure also contains labeled axes (rows and columns). Arithmetic operations align on both row and column labels. Can be thought of as a dict-like container for Series objects. The primary pandas data structure.

    Parameters:
      data: ndarray (structured or homogeneous), Iterable, dict, or DataFrame
        Dict can contain Series, arrays, constants, dataclass or list-like objects. If data is a dict, column order follows insertion-order. If a dict contains Series which have an index defined, it is aligned by its index. This alignment also occurs if data is a Series or a DataFrame itself. Alignment is done on Series/DataFrame inputs.

      	If data is a list of dicts, column order follows insertion-order.

			index: Index or array-like
        Index to use for resulting frame. Will default to RangeIndex if no indexing information part of input data and no index provided.

			columns: Index or array-like
        Column labels to use for resulting frame when data does not have them, defaulting to RangeIndex(0, 1, 2, …, n). If data contains column labels, will perform column selection instead.

			dtype: dtype, default None
				Data type to force. Only a single dtype is allowed. If None, infer.

			copy: bool or None, default None
        Copy data from inputs. For dict data, the default of None behaves like copy=True. For DataFrame or 2d ndarray input, the default of None behaves like copy=False. If data is a dict containing one or more Series (possibly of different dtypes), copy=False will ensure that these inputs are not copied.
```

DataFrame是Pandas里最重要的数据结构，可以理解为一个带有行索引和列索引的二维表格。

DataFrame的每一列都是一个Series，不同列的数据类型都可以不一样，同一列的数据类型也可以不一样。

## DataFrame创建

DataFrame创建有如下核心参数：

* 入参data：`data`可以是numpy的ndarray，list，dict，Series, scalar，也可以是一个dataframe。
* 入参index：`index`用于为DataFrame指定行标签（索引），是一个array-like的类型，比如python里的list和tuple，通常用list的类型作为传参，例如`index=['row1', 'row2']`。
* 入参columns： `columns`参数用于为DataFrame指定列标签，是一个array-like的类型，比如python里的list和tuple，通常用list的类型作为传参，例如`columns=['col1', 'col2']`。
* 入参dtype：`dtype`参数用于指定DataFrame中数据的类型，如果不指定会自动推导数据类型，如果指定的话，那整个DataFrame的每一个值都是相同的数据类型（如果不能转换为相同的数据类型就会创建失败）。
* 入参copy：copy参数是布尔类型或None，默认是None。如果data是dict类型，那默认值None的行为相当于copy=True，拷贝一份原始数据。如果data是DataFrame或者2d ndarray，那默认值None的行为相当于copy=False，不拷贝原始数据，是原始数据的一个副本。

DataFrame创建的时候根据data、index和columns这3个入参的搭配，有不同的效果。

* data是None

  ```bash
  In [387]: df = pd.DataFrame()
  
  In [388]: df
  Out[388]: 
  Empty DataFrame
  Columns: []
  Index: []
  
  ## 只传index时，DataFrame是empty
  In [389]: df = pd.DataFrame(index=['r1'])
  
  In [390]: df
  Out[390]: 
  Empty DataFrame
  Columns: []
  Index: [r1]
  
  ## 只传columns时，DataFrame是empty
  In [391]: df = pd.DataFrame(columns=['c1'])
  
  In [392]: df
  Out[392]: 
  Empty DataFrame
  Columns: [c1]
  Index: []
  
  ## 当index和columns都传值时，虽然data是None，但是DataFrame不再是empty
  In [393]: df = pd.DataFrame(index=['r1'], columns=['c1'])
  
  In [394]: df
  Out[394]: 
       c1
  r1  NaN
  ```

  

* data是scalar。这种情况下index和columns都必须传参，否则会报错提示`ValueError: DataFrame constructor not properly called!`

  ```bash
  In [395]: df = pd.DataFrame(6)
  ---------------------------------------------------------------------------
  ValueError                                Traceback (most recent call last)
  <ipython-input-395-a217a9a40569> in ?()
  ----> 1 df = pd.DataFrame(6)
  
  /opt/anaconda3/lib/python3.12/site-packages/pandas/core/frame.py in ?(self, data, index, columns, dtype, copy)
      882                 )
      883         # For data is scalar
      884         else:
      885             if index is None or columns is None:
  --> 886                 raise ValueError("DataFrame constructor not properly called!")
      887 
      888             index = ensure_index(index)
      889             columns = ensure_index(columns)
  
  ValueError: DataFrame constructor not properly called!
  
  In [396]: df = pd.DataFrame(6, index=['r1'])
  ---------------------------------------------------------------------------
  ValueError                                Traceback (most recent call last)
  <ipython-input-396-ef67b9911446> in ?()
  ----> 1 df = pd.DataFrame(6, index=['r1'])
  
  /opt/anaconda3/lib/python3.12/site-packages/pandas/core/frame.py in ?(self, data, index, columns, dtype, copy)
      882                 )
      883         # For data is scalar
      884         else:
      885             if index is None or columns is None:
  --> 886                 raise ValueError("DataFrame constructor not properly called!")
      887 
      888             index = ensure_index(index)
      889             columns = ensure_index(columns)
  
  ValueError: DataFrame constructor not properly called!
  
  In [397]: df = pd.DataFrame(6, index=['r1'], columns=['c1'])
  ```

  注意上面的报错代码，就可以看到如果data是scalar，那index和columns都必须非None。

  ```python
  # For data is scalar
      884         else:
      885             if index is None or columns is None:
  --> 886                 raise ValueError("DataFrame constructor not properly called!")
  ```

  data是scalar也可以创建多行多列的DataFrame

  ```bash
  In [399]: df = pd.DataFrame(6, index=['r1'], columns=['c1', 'c2'])
  
  In [400]: df
  Out[400]: 
      c1  c2
  r1   6   6
  
  In [401]: df = pd.DataFrame(6, index=['r1', 'r2'], columns=['c1', 'c2'])
  
  In [402]: df
  Out[402]: 
      c1  c2
  r1   6   6
  r2   6   6
  ```

  

* data是2d ndarray

  ```bash
  ## 不指定index和column，那index和column都是默认从0开始编号
  In [412]: array = np.array([[1,2,3], [4,5,6]])
  
  In [413]: df = pd.DataFrame(array)
  
  In [414]: df
  Out[414]: 
     0  1  2
  0  1  2  3
  1  4  5  6
  
  ## 指定index
  In [415]: df = pd.DataFrame(array, index=['r1', 'r2'])
  
  In [416]: df
  Out[416]: 
      0  1  2
  r1  1  2  3
  r2  4  5  6
  
  ## 指定index和column
  In [417]: df = pd.DataFrame(array, index=['r1', 'r2'], columns=['c1', 'c2', 'c3'])
  
  In [418]: df
  Out[418]: 
      c1  c2  c3
  r1   1   2   3
  r2   4   5   6
  ```

  

* data是list。

  ```bash
  ## 类似2d ndarray，可以按需指定index和column
  In [419]: l = [[1, 2, 3], [4, 5, 6]]
  
  In [420]: df = pd.DataFrame(l, index=['r1', 'r2'], columns=['c1', 'c2', 'c3'])
  
  In [421]: df
  Out[421]: 
      c1  c2  c3
  r1   1   2   3
  r2   4   5   6
  ```

  如果list里每个元素是dict，那dict里的每个key就是DataFrame的column。

  ```bash
  In [422]: l = [{'c1':1, 'c2':2, 'c3':3}, {'c1':4, 'c2':5, 'c3':6}]
  
  In [423]: df = pd.DataFrame(l, index=['r1', 'r2'])
  
  In [424]: df
  Out[424]: 
      c1  c2  c3
  r1   1   2   3
  r2   4   5   6
  
  ## 如果columns有传参，那只有匹配了dict的key的列才会被保留下来
  ## 如果column的列匹配不到dict的key，那该列的值就是NaN
  In [437]: df = pd.DataFrame(l, index=['r1', 'r2'], columns=['d'])
  
  In [438]: df
  Out[438]: 
       d
  r1 NaN
  r2 NaN
  
  ## 如果list里的每个dict元素不是都有完全一样的key
  In [444]: l = [{'c1':1, 'c2':2, 'c3':3}, {'c1':4, 'c2':5}]
  
  In [445]: df = pd.DataFrame(l, index=['r1', 'r2'])
  
  In [446]: df
  Out[446]: 
      c1  c2   c3
  r1   1   2  3.0
  r2   4   5  NaN
  
  ## 只有columns里的列才会出现在DataFrame里
  ## 如果columns里的列名匹配不到dict里的key，那DataFrame里该列的值是NaN
  In [447]: df = pd.DataFrame(l, index=['r1', 'r2'], columns=['d'])
  
  In [448]: df
  Out[448]: 
       d
  r1 NaN
  r2 NaN
  
  In [449]: l = [{'c1':1, 'c2':2, 'c3':3}, {'c1':4, 'c2':5, 'c4':6}]
  
  In [450]: df = pd.DataFrame(l, index=['r1', 'r2'])
  
  In [451]: df
  Out[451]: 
      c1  c2   c3   c4
  r1   1   2  3.0  NaN
  r2   4   5  NaN  6.0
  ```

  

* data是dict

  ```bash
  In [453]: df = pd.DataFrame({'col1':[1, 2], 'col2': [3, 4]}, index=['r1', 'r2'])
  
  In [454]: df
  Out[454]: 
      col1  col2
  r1     1     3
  r2     2     4
  
  ## 如果指定了columns参数，会从dict里选出匹配columns参数的列，其它列不会出现在
  ## DataFrame里
  
  In [455]: df = pd.DataFrame({'col1':[1, 2], 'col2': [3, 4]}, index=['r1', 'r2'], columns=['col1'])
  
  In [456]: df
  Out[456]: 
      col1
  r1     1
  r2     2
  
  ## 如果columns里的某个列名匹配不到dict里的key，那DataFrame里该列的值都是NaN
  In [457]: df = pd.DataFrame({'col1':[1, 2], 'col2': [3, 4]}, index=['r1', 'r2'], columns=['col1', 'col3'])
  
  In [458]: df
  Out[458]: 
      col1 col3
  r1     1  NaN
  r2     2  NaN
  ```

  

* data是Series。

  ```bash
  ## Series直接作为data传参，生成的DataFrame就只有Series这一列
  In [462]: s = pd.Series([1,2])
  
  In [463]: df = pd.DataFrame(s)
  
  In [464]: df
  Out[464]: 
     0
  0  1
  1  2
  
  ## Series指定了index
  In [465]: s = pd.Series([1,2], index=['r1', 'r2'])
  
  In [466]: df = pd.DataFrame(s)
  
  In [467]: df
  Out[467]: 
      0
  r1  1
  r2  2
  
  ## 指定列名
  In [468]: df = pd.DataFrame(s, columns=['col'])
  
  In [469]: df
  Out[469]: 
      col
  r1    1
  r2    2
  
  ## 如果Series里的index和pd.DataFrame传参的index不匹配
  ## 生成的DataFrame会以pd.DataFrame传参的index作为DataFrame的index
  ## 根据pd.DataFrame的index参数去找Series里对应index的值，找不到的话值就是NaN
  In [474]: df = pd.DataFrame(s, index=['a', 'b'], columns=['col'])
  
  In [475]: df
  Out[475]: 
     col
  a  NaN
  b  NaN
  
  In [481]: s = pd.Series([1,2], index=['r1', 'r2'])
  
  In [482]: df = pd.DataFrame(s, index=['r1', 'r3'], columns=['col'])
  
  In [483]: df
  Out[483]: 
      col
  r1  1.0
  r3  NaN
  ```

  

* data是DataFrame

  ```bash
  In [485]: df = pd.DataFrame({'A':[1,2], 'B': [3, 4]}, index=['r1', 'r2'])
  
  In [486]: df
  Out[486]: 
      A  B
  r1  1  3
  r2  2  4
  
  In [487]: df1 = pd.DataFrame(df)
  
  In [488]: df1
  Out[488]: 
      A  B
  r1  1  3
  r2  2  4
  ```

  

## DataFrame访问



## DataFrame修改



## DataFrame删除



## DataFrame索引



## References

* https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame
* https://www.runoob.com/pandas/pandas-dataframe.html
