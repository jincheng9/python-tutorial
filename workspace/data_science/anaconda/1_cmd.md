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

该命令用于创建新的环境。

* `conda create -n env_name`

  创建名为env_name的新环境，这个环境里没有python以及任何python的包。`-n`的`n`表示name。

* `conda create -n env_name python=3.x`  

  创建名为env_name的新环境，并且在这个新环境安装版本为3.x的python。

  **注意**：全新环境默认是没有装pandas等数据分析库的，只有ca-certificates到wincertstore等基本库，如下所示：

```bash
(test_pandas) C:\Users\jczha>conda create -n test_create python=3.9
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\jczha\Anaconda3\envs\test_create

  added / updated specs:
    - python=3.9


The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/win-64::ca-certificates-2022.4.26-haa95532_0
  certifi            pkgs/main/win-64::certifi-2021.10.8-py39haa95532_2
  openssl            pkgs/main/win-64::openssl-1.1.1o-h2bbff1b_0
  pip                pkgs/main/win-64::pip-21.2.4-py39haa95532_0
  python             pkgs/main/win-64::python-3.9.12-h6244533_0
  setuptools         pkgs/main/win-64::setuptools-61.2.0-py39haa95532_0
  sqlite             pkgs/main/win-64::sqlite-3.38.3-h2bbff1b_0
  tzdata             pkgs/main/noarch::tzdata-2022a-hda174b7_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  wheel              pkgs/main/noarch::wheel-0.37.1-pyhd3eb1b0_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py39haa95532_2
```

* `conda create --clone exist_env_name -n new_env_name`  

  克隆已有环境exist_env_name到新环境new_env_name，新环境new_env_name的python版本和python库与被clone的环境exist_env_name保持一致。

  

## conda activate

该命令用于切换到新环境。

` conda activate [-h] [--[no-]stack] [env_name_or_prefix]`

一般activate后面跟的是环境名称，示例如下：

```bash
(base) C:\Users\jczha>conda activate test_no_pandas

(test_no_pandas) C:\Users\jczha>conda activate test_pandas

(test_pandas) C:\Users\jczha>
```




## conda deactivate

该命令用于退出当前环境到上一级环境，和栈的逻辑一样。

比如我们按照base -> env1 -> env2的顺序切换环境，从base环境切换到env1环境，然后从env1环境切换到env2环境。

那在env2环境下执行`conda deactivate`会退出env2环境，进入env1环境。

接着在env1环境下执行`conda deactivate`会退出env1环境，进入base环境。

在base环境下执行`conda deactivate`会退出base环境，进入到cmd原始环境，

```bash
(base) C:\Users\jczha>conda deactivate

C:\Users\jczha>
```



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

该命令用于给指定环境安装包。

* `conda install -n myenv scipy`

  给指定环境myenv安装scipy包。


* `conda install scipy`

  在当前环境安装scipy。

* `conda install -c conda-forge pandas`

  -c 指定从哪个channel获取对应的python package。

  channel官方说明：https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html

  可以通过`conda install -h`来查看关于channel的参数说明。

## conda update

该命令用于给指定环境更新包到最新的兼容版本。

> Updates conda packages to the latest compatible version.
>
>     This command accepts a list of package names and updates them to the latest
>     versions that are compatible with all other packages in the environment.
>     
>     Conda attempts to install the newest versions of the requested packages. To
>     accomplish this, it may update some packages that are already installed, or
>     install additional packages. To prevent existing packages from updating,
>     use the --no-update-deps option. This may force conda to install older
>     versions of the requested packages, and it does not prevent additional
>     dependency packages from being installed.

* `conda update -n myenv scipy`

  更新指定环境myenv的scipy包到最新版本。

* `conda update scipy`

  更新当前环境的scipy包到最新版本。

## conda remove

该命令用于删除指定环境的指定包或者所有包，如果使用`--all`移除所有包，那这个环境也被删除了。

* `conda remove -n myenv scipy`

  移除myenv这个环境下的scipy包。

* `conda remove -n myenv --all`

  移除myenv环境。

* `conda env remove -n myenv`

  移除myenv环境。

  

## References

* conda开源地址：https://github.com/conda/conda
* https://www.jianshu.com/p/eaee1fadc1e9