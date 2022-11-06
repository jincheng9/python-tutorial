# Lecture 2: Jupyter Lab指定Conda环境作为Kernel

## 问题

本地安装好Anaconda后，可以在Anaconda Prompt里执行如下命令启动Jupyter Lab

```bash
jupyter lab
```

我们在创建notebook的时候，可以选择kernel。

初始安装后，只有一个默认的kernel: Python 3，那我们怎么可以添加新的kernel呢？

方法是基于conda创建新的环境，然后把新的环境安装到Jupyter Lab的Kernel里，界面上就可以显示新的Kernel了。

## 操作步骤

* 第一步，创建你需要的conda环境，假设名字为quant-dev。

* 第二步，激活你的环境quant-dev。

  ```bash
  conda activate quant-dev
  ```

* 在这个conda环境里安装你需要的各种依赖包。

  使用conda  install或者pip install都可以，都会把package安装在当前所处的quant-dev环境。

  ```bash
  conda install package_xxx
  pip install package_xxx
  ```

* 第三步，安装ipykernel。如果你的环境已经有了ipykernel那就可以跳过。使用conda install或者pip install安装都可以。

  ```bash
  conda install ipykernel
  pip install ipykernel
  ```

* 第四步，把conda环境写入jupyterlab的kernel中，用于Jupyter Lab界面显示。

  ```bash
  python -m ipykernel install --name quant-dev --display-name quant-dev
  ```

  * --name后面的参数是kernel的名字，执行`jupyter kernelspec list`会显示这里的名字。

  * --display-name后面的参数是Jupyter  Lab界面显示的Kernel名字。

  * 如果在上述命令增加--user则只给当前用户安装，而不是给系统里所有用户都安装。

    ```bash
    python -m ipykernel install --user --name quant-dev --display-name quant-dev
    ```

* 第五步，刷新Jupyter Lab页面，就可以展示新加的Kernel了。



## 其它常用命令

* 查看有哪些Kernel

  ```bash
  jupyter kernelspec list
  ```

* python -m ipykernel install的参数含义

  ```bash
  (base) > python -m ipykernel install -h
  usage: ipython-kernel-install [-h] [--user] [--name NAME] [--display-name DISPLAY_NAME] [--profile PROFILE]
                                [--prefix PREFIX] [--sys-prefix] [--env ENV VALUE]
  
  Install the IPython kernel spec.
  
  optional arguments:
    -h, --help            show this help message and exit
    --user                Install for the current user instead of system-wide
    --name NAME           Specify a name for the kernelspec. This is needed to have multiple IPython kernels at the same
                          time.
    --display-name DISPLAY_NAME
                          Specify the display name for the kernelspec. This is helpful when you have multiple IPython
                          kernels.
    --profile PROFILE     Specify an IPython profile to load. This can be used to create custom versions of the kernel.
    --prefix PREFIX       Specify an install prefix for the kernelspec. This is needed to install into a non-default
                          location, such as a conda/virtual-env.
    --sys-prefix          Install to Python's sys.prefix. Shorthand for --prefix='C:\Users\jczha\Anaconda3'. For use in
                          conda/virtual-envs.
    --env ENV VALUE       Set environment variables for the kernel.
  ```

## References

* https://blog.csdn.net/Geoffrey_Zflyee/article/details/111586786



