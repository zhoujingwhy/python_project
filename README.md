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
>  分析一下朋友个性签名时使用的高频词语是什么，做出词云图<br><br>
## 配置过程<br>
--------------------------
本项目是基于python3.6+window10环境的。<br>
>模块:<br>
>itchat：提供了一个微信api接口<br>
>pandas:提供了一个value_counts()方法，可以更方便统计各项出现的次数<br>
>jieba :分词分析语料库<br>
>numpy:提供了矩阵运算的功能<br>
>wordcloud:生成的词云图<br>
re,matplotlib等<br>
使用pip 安装完成后导入包，环境配置完成。<br>
