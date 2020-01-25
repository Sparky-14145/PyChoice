# PyChoice
供中小学教师上课点名用的一个点名器。

## Usage
### 图形界面
#### 1. 获取可执行文件
##### 使用打包完成的可执行文件
在[Release页面](https://github.com/Sparky-14145/PyChoice/releases)下载可执行文件，然后在可执行文件所在的目录下建立一个`assets`文件夹。
##### 克隆本仓库
```shell
git clone https://github.com/Sparky-14145/PyChoice.git
```

##### 文本界面
暂未开发文本界面，详见 [TODO List](#TODO)。
#### 2. 配置
**以下文件均位于`assets`文件夹中。**  
##### `cfg.txt`
主控制文件。  
默认内容：
```
lang:zh_CN
database:assets/data.txt
```

- `lang`：软件界面语言。默认为`zh_CN`。值为`x`时表示界面文字使用文件`assets/x.txt`中的内容；
- `database`：数据存放位置。可使用相对（可执行文件的）路径或者绝对路径。默认为`assets/data.txt`；
##### `(Lang).txt`
多国语言文件，控制界面显示文字。  
默认内容：
```
hello:欢迎使用 PyChoice，请在下方文本框内输入人数后点击下方“抽样”按钮！
action:抽样！
mount_init:抽取人数
no_enough_students:错误——没有那么多学生！
not_a_num:请输入一个正整数！
```

- `hello`：初始时结果区显示的文字；
- `action`：按钮文字；
- `mount_init`：初始时人数区显示的文字；
- `no_enough_students`：（提示信息）人数区请求人数大于数据中实际人数；
- `not_a_num`：（提示信息）人数区输入的不是一个数字。
##### `data.txt`
默认的数据文件。  
此文件中存储学生姓名，每个名字一行。
## TODO
- [ ] 资瓷文本界面！
- [ ] 美化图形界面（考虑用 `pygame` 重写 :thinking: ）；
- [ ] 图形界面内修改配置文件:clipboard:。