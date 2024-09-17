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
* 入参index：`index`用于为DataFrame指定行标签（索引）。
* 入参columns： `columns`参数用于为DataFrame指定列标签。
* 入参dtype：`dtype`参数用于指定DataFrame中数据的类型，如果不指定会自动推导数据类型。
* 入参copy：copy参数是布尔类型或None，默认是None。如果data是dict类型，那默认值None的行为相当于copy=True，拷贝一份原始数据。如果data是DataFrame或者2d ndarray，那默认值None的行为相当于copy=False，不拷贝原始数据，是原始数据的一个副本。

DataFrame创建的时候根据data、index和columns这3个入参的搭配，有不同的效果。

* data是None
* data是scalar
* data是2d ndarray
* data是list
* data是dict
* data是Series
* data是DataFrame

## DataFrame访问



## DataFrame修改



## DataFrame删除



## DataFrame索引



## References

* https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame
* https://www.runoob.com/pandas/pandas-dataframe.html
