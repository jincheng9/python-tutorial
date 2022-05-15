# conda命令使用手册

打开`Anaconda Prompt`或`Anaconda Powershell Prompt`后，即可在命令行窗口里使用`conda`命令，默认会进入到`base`环境。

`conda`命令可以用来管理和部署应用(applications)、环境(environments)和包(packages)。

> conda is a tool for managing and deploying applications, environments and packages.

conda常用命令如下：

## conda env list

展示当前已有的环境，第一列是环境名称，第二列是环境所在的路径。

```bash
(base) C:\Users\jczha>conda env list
# conda environments:
#
base                  *  C:\Users\jczha\Anaconda3
test_no_pandas           C:\Users\jczha\Anaconda3\envs\test_no_pandas
test_pandas              C:\Users\jczha\Anaconda3\envs\test_pandas
```

