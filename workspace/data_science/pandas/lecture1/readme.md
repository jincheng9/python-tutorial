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
* 入参index：Series的索引。入参index

## Series访问



## Series修改



## Series索引



## Series总结

* Series里的每个元素可以是不同的数据类型
* Series

## References

* https://pandas.pydata.org/docs/reference/api/pandas.Series.html