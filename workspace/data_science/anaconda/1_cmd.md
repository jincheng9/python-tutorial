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



## conda -V

该命令用于获取conda的版本号，等同于`conda --version`。

```bash
(base) C:\Users\jczha>conda -V
conda 4.12.0
(base) C:\Users\jczha>conda --version
conda 4.12.0
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



## conda activate

该命令用于切换到新环境。




## conda deactivate

该命令用于退出当前环境。



## conda list

该命令用于展示当前环境下的包(packages)，有时候想要查看当前环境是否有安装某个包时，可以使用该命令。

```bash
(test_no_pandas) C:\Users\jczha>conda list
# packages in environment at C:\Users\jczha\Anaconda3\envs\test_no_pandas:
#
# Name                    Version                   Build  Channel
bzip2                     1.0.8                he774522_0
ca-certificates           2022.4.26            haa95532_0
certifi                   2020.6.20          pyhd3eb1b0_3
libffi                    3.4.2                h604cdb4_1
openssl                   1.1.1o               h2bbff1b_0
pip                       21.2.4          py310haa95532_0
python                    3.10.4               hbb2ffb3_0
setuptools                61.2.0          py310haa95532_0
sqlite                    3.38.3               h2bbff1b_0
tk                        8.6.11               h2bbff1b_1
tzdata                    2022a                hda174b7_0
vc                        14.2                 h21ff451_1
vs2015_runtime            14.27.29016          h5e58377_2
wheel                     0.37.1             pyhd3eb1b0_0
wincertstore              0.2             py310haa95532_2
xz                        5.2.5                h8cc25b3_1
zlib                      1.2.12               h8cc25b3_2
```



## conda install

## conda update

## conda remove

