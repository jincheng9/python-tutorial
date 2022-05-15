# conda命令使用手册

打开`Anaconda Prompt`或`Anaconda Powershell Prompt`后，即可在命令行窗口里使用`conda`命令，默认会进入到`base`环境。

`conda`命令可以用来管理和部署应用(applications)、环境(environments)和包(packages)。

> conda is a tool for managing and deploying applications, environments and packages.

conda常用命令如下：

## conda -h

该命令是conda命令帮助手册，通过`conda -h`我们可以知晓conda所支持的子命令。

```bash
(base) C:\Users\jczha>conda -h
```

conda常用的子命令有env, create, list, install, remove, update, activate, deactivate等。

如果想了解每个子命令怎么使用，可以使用如下命令(以create子命令为例)

```bash
(base) C:\Users\jczha>conda create -h
```

## conda env list

该命令用于展示当前已有的环境。命令执行结果里，第一列是环境名称，第二列是环境所在的路径。

```bash
(base) C:\Users\jczha>conda env list
# conda environments:
#
base                  *  C:\Users\jczha\Anaconda3
test_no_pandas           C:\Users\jczha\Anaconda3\envs\test_no_pandas
test_pandas              C:\Users\jczha\Anaconda3\envs\test_pandas
```

每次打开Anaconda Prompt的时候，默认会进入到base环境。

`(base) C:\Users\jczha>conda env list`最前面的`(base)`就表示当前处于base环境。

## conda create 



## conda activate/deactivate



## conda list

## conda install

## conda update

## conda remove

