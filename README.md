# PalServerTools
## 幻兽帕鲁服务器管理工具

#### 自动备份脚本-linux

    将 “自动备份脚本 / linux / auto-backup.sh” 脚本文件放置在幻兽帕鲁服务器同级目录下

    运行即可

    ```Shell
    chmod +x ./auto-backup.sh
    ./auto-backup.sh
    ```

    运行之后它会在当前目录下创建目录“./auto-backup/时间格式的目录”并阻塞终端并打印日志。

    每30分钟进行备份，如果要更改自动备份的间隔时间只需要更改“sleep 30m”的 30m。例如：

    1d 12h 30m 30s   表示  1天、12小时、30分钟、30秒

    

#### 自动备份脚本-windows

    还没写，等啥时候用windows再看怎么写

#### 生成设置文件

    运行之前需要python环境

    需要对“生成设置文件/main.py”中的参数按照注释根据自己的玩法进行更改

    之后用python运行它，会在它的当前目录生成“PalWorldSettings.ini”文件。

    将该文件替换至 → ~PalServer/Pal/Saved/Config/LinuxServer/PalWorldSettings.ini

    或者替换至 → ~PalServer/Pal/Saved/Config/WindowsServer/PalWorldSettings.ini

    取决于你的系统


