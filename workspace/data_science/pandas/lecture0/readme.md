# Lecture0: Pandas介绍

Pandas 在数据分析处理中应用非常广泛，各行各业需要做数据处理和分析的基本都会用到Pandas。

Pandas的作者是[Wes McKinney](https://wesmckinney.com/)。

Pandas最早是Wes Mckinney在 [AQR Capital Management](https://www.aqr.com/)工作期间研发的，2008年开始研发，2009年底正式开源，目前已经是数据分析领域的首选Python库。

Pandas主要引入了2种新的数据结构：Series和DataFrame。

## Series

Series可以理解为带有索引的一维数组，类似于表格里的某一列。

一个Series可以存储不同的数据类型的元素。

```python
import pandas as pd
s = pd.Series([1, 'str', True])
```

每个Series都有索引，可以在创建Series的时候显示指定索引。

## DataFrame

DataFrame可以理解为带有行索引和列索引的二维数组，类似于二维表格。

DataFrame的每一列就是一个Series，DataFrame的每一列可以是不同的数据类型，DataFrame的同一列里的每个元素也可以是不同的数据类型。

```python
import pandas as pd
df = pd.DataFrame({'a':[1,'s', True], 'b': [2, 3, 4]})
```



## References

* https://pandas.pydata.org/about/index.html
* https://wesmckinney.com/

