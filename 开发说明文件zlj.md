# 6-4 5:51
## 本次版本开发说明：
！！warning！！请千万不要做出会对数据库进行修改的举动！！求您了！！
请只使用我配置好的数据库求求了

说明：大幅度更改了SchoolIndex页的内容。到course页的链接还没做好，但是现在SchoolIndex页已经可以成功与后端交互，从后端加载所有School数据。

==注意：返回SchoolIndex页之后需要刷新页面才能重新获取院系列表，具体为什么我也不太清楚==

想要搜索也很简单，在这个页面你只需要ctrl-F 然后搜索就行了，so easy

去掉了关注功能，具体原因见models和views，因为现在想要实现这个功能需要对用户模型进行比较大的修改而且可能会非常麻烦，引入别的bug，时间比较紧我就不搞了。

## 在本次开发中学到的东西：
在element plus的表项中加入跳转连接的方法（具体见SchoolIndex页，scope；还有就是element ui里面表格的设计）

# dynamic route matching
