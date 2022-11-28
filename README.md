## python自动化程序填写问卷星

### 1.配置环境
#### 1.1安装selenium依赖
```python
#使用默认源安装
pip install selenium

#如果速度过慢可以选着换源进行安装
pip install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```
#### 1.2安装浏览器驱动(这里默认使用Chrome浏览器进行演示)
使用Chrome浏览器打开链接查看自己浏览器的版本 chrome://settings/help

然后前往这个链接下载对应版本的浏览器驱动(若无对应版本选着高版本即可) http://npm.taobao.org/mirrors/chromedriver/

将下载好的chromedriver.exe放到 C:\Program Files\Google\Chrome\Application 目录下

### 2.开始运行
#### 2.获取项目
手动下载压缩包后解压或使用git拉取本项目

进入main.py目录下输入
```python
python main.py
```
会生成一个config.json文件
#### 2.1编写配置文件
```jsom

{
    "option_nums":[2, 5, 4, 4, 4, 5, 2], 
    "注释1": "每个问题选项的数量(-1表示该题为简答题)",
    "multiple_choice":[0,0,0,0,0,1,0],
    "注释2": " 0表单选 1表多选 简答题随意",
    "max_workers" : 4, 
    "注释3": "//线程数量",
    "run_num" : 200 , 
    "注释4": "//填写问卷次数",
    "url" : "https://www.wjx.cn/vm/exnm04A.aspx",
    "注释5" : "调查问卷链接"
}
```


