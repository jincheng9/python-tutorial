# 安装或卸载Anaconda后Windows自带的cmd窗口会闪退

## 问题现象

Anaconda初次安装或者重装后，如果打开Windows系统自带的cmd命令窗口，会马上闪退。

Win + R，输入`cmd`就闪退。

Win + R，输入`cmd /d`可以正常打开。



## 解决方案

网上很多给出的解决方案是：

按Win + R，输入regedit打开注册表编辑器，顶部输入：

```
计算机\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Command Processor
```

修改界面里AutoRun的值为空或者删除AutoRun，按确定即可。

但是在我这里不生效，界面里就没有AutoRun。



解决方法是：以管理员权限打开PowerShell，然后输入

`C:\Windows\System32\reg.exe DELETE "HKCU\Software\Microsoft\Command Processor" /v AutoRun /f`

之后就可以正常打开cmd了。



## 开源地址

文章和示例代码开源在GitHub: [Python语言初级、中级和高级教程](https://github.com/jincheng9/python-tutorial)。

公众号：coding进阶。关注公众号可以获取最新Python数据科学、Python量化交易技术栈。

个人网站：[Jincheng's Blog](https://jincheng9.github.io/)。

知乎：[无忌](https://www.zhihu.com/people/thucuhkwuji)。



## 福利

我为大家整理了一份后端开发学习资料礼包，包含编程语言入门到进阶知识(Go、C++、Python)、后端开发技术栈、面试题等。

关注公众号「coding进阶」，发送消息 **backend** 领取资料礼包，这份资料会不定期更新，加入我觉得有价值的资料。

发送消息「**进群**」，和同行一起交流学习，答疑解惑。

