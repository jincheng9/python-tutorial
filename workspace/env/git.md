# git安装和ssh配置

1. 下载和安装Git

   https://git-scm.com/downloads

2. 生成ssh公钥和私钥

   * 打开Git Bash，输入命令，一路回车

     ```bash
     ssh-keygen -t rsa -C "comment"
     ```

     -t 表示创建的key的类型(type)，比较常用的是rsa和ed25519，上面示例用的是rsa类型

     -C 表示Comment，给公钥末尾加上一些便于记忆的描述

     https://docs.github.com/cn/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

   * 生成的公钥和私钥在`~/.ssh`目录下。

3. 公钥复制到GitHub/GitLab的个人设置里(假设使用的ssh key类型是rsa)

   * 直接拷贝`~/.ssh/id_rsa.pub`里的公钥到GitHub/GitLab个人账户Settings下的`SSH and GPG keys`里。
   * 拷贝命令参考：Windows用`clip < ~/.ssh/id_rsa.pub`，Mac用`pbcopy < ~/.ssh/id_rsa.pub`，Linux用`xclip`命令。

4. 测试连接

   * 执行以下命令：

     ```bash
     ssh -T git@github.com
     ```

     出现`Are you sure you want to continue connecting (yes/no/[fingerprint])?`时，要输入yes，不能直接回车，否则就不会在`.ssh`目录下生成`known_hosts`文件，后面clone代码会出错。

   * 当看到如下结果就表示大功告成了。

     ```bash
     Hi xxx! You've successfully authenticated, but GitHub does not provide shell access.
     ```

5. 下载代码

   * 上面的1-4操作完成后，就可以`git clone`代码了。