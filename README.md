# python_project
爬虫
==========
## 说明<br>
----------------
>最近看了爬虫的这些代码，感觉挺有趣的。于是在网上参考了一些案例。做了一个爬取微信好友简单信息实现，见文件夹（爬取微信好友简单信息）。<br>
## 爬取微信好友简单信息功能说明<br>
>（1）可以打印出自己的好友性别比例<br>
>  Sex，男性值为1，女性为2，其他是不明性别的（就是没有填的）为0<br>
>（2）得到微信好友的城市分布，数据存到csv文件<br>
>  里面还包含了好友昵称、省份、城市、个人简介等<br>
>（3）微信好友个性签名的自定义词云图<br>
>  分析一下朋友个性签名时使用的高频词语是什么，做出词云图<br>
> (4) 头像下载和拼接<br><br>
## 配置过程<br>
--------------------------
### 本项目是基于python3.6+window10环境的。<br>
>模块:<br>
>itchat：提供了一个微信api接口<br>
>pandas:提供了一个value_counts()方法，可以更方便统计各项出现的次数<br>
>jieba :分词分析语料库<br>
>numpy:提供了矩阵运算的功能<br>
>wordcloud:生成的词云图<br>
re,matplotlib,PIL,os,math等<br>
使用pip 安装完成后导入包，环境配置完成。<br>
## 运行过程<br>
----------------------------
### 首先运行getinfo.py<br>
### 1.性别是存放在一个字典里面的，key是”Sex“，男性值为1，女性为2，其他是不明性别的为0。可以写个循环获取想要的性别数据，得到自己微信好友的性别比例。<br>
>![AAA](https://github.com/zhoujingwhy/python_project/raw/master/说明/QQ截图20180612171017.png)<br><br>
### 2.定义一个函数把好友昵称、省份、城市、个人简介等等的数据都爬下来，存到数据框里，再进行分析好友城市分布。<br>
>![AAA](https://github.com/zhoujingwhy/python_project/raw/master/说明/QQ截图20180612171200.png)<br><br>
### 3.把原先爬下来的个性签名打印出来，发现有很多本来是表情的，变成了emoji、span、class等等这些无关紧要的词，需要先替换掉，另外，还有类似<>/= 之类的符号，也需要写个简单的正则替换掉，再把所有拼起来，得到text字串。<br>
>![AAA](https://github.com/zhoujingwhy/python_project/raw/master/说明/QQ截图20180612171245.png)<br><br>
### 4.把jieba这个包搞进来分词<br>
>![AAA](https://github.com/zhoujingwhy/python_project/raw/master/说明/QQ截图20180612171320.png)<br><br>
### 5.进入画图阶段。可以根据自己想要的图片、形状、颜色画出相似的图形。
>![AAA](https://github.com/zhoujingwhy/python_project/raw/master/说明/QQ截图20180612171416.png)<br><br>
### 再运行head.py<br>
### 6.首先我们需要把好友的头像下载下来，然后进行拼接<br>
     把好友的头像下载下来,放入一个文件夹中<br>
>![AAA](https://github.com/zhoujingwhy/python_project/raw/master/说明/QQ截图20180620211248.png)<br><br>
     然后把好友的头像进行拼接，生成一个拼图。<br>
>![AAA](https://github.com/zhoujingwhy/python_project/raw/master/说明/QQ截图20180620211318.png)<br><br>
     
## 运行结果<br>
-------------------------------------------------------------
### 显示微信好友的性别比例<br>
>![AAA](https://github.com/zhoujingwhy/python_project/raw/master/说明/QQ截图20180612123421.png)<br><br>
### 微信好友的个人签名词云图<br>
>![AAA](https://github.com/zhoujingwhy/python_project/raw/master/说明/Figure_1.png)<br><br>
### 生成一个dtat.csv，在爬取微信好友简单信息文件夹中。如下图<br>
>![AAA](https://github.com/zhoujingwhy/python_project/raw/master/说明/QQ截图20180612184533.png)<br><br>
## 总结<br>
### 如果微信好友有几千个，可以得到几千条数据，还是挺有意思的。
