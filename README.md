## Python 跨模块全局变量的简单实现方法

文章同步在：https://uinote.com/index.php?c=index&a=show&id=133

Python 中 global 关键字可以定义一个变量为全局变量，但是这个仅限于在当前模块（py文件）中调用全局变量，在其他py文件 再次使用 global x 也是无法访问到的，因为在这个py模块中并没有一个叫做x的变量，于是就会报错 `未定义`。

我们知道Python使用变量的时候是可以直接使用的

```python
a = {}
b = 111
c = "333"
```

而不需要预先声明类型

```javascript
var a
var b = 2
var c = '222'
```

这样的话，在函数内部就无法操作外部的变量了，因为它总会认为你是在定义一个新变量并且赋值，不过 global 就可以解决这个问题。
**global 的基础用法**

```python
x = 6
def func():
    global x # 定义全局变量外部的x
    x = 1
func()
print(x)
# 输出1
```

这个时候，在定义本全局变量的模块内可以随意使用变量x

但是别的模块(py文件)再次使用 global x 却是无法访问到的，因为在这个py模块中并没有一个叫做x的变量。

既然只能在本模块可以使用，那么我们就专门为全局变量定义一个`全局变量管理模块`，然后在别的模块中导入全局变量管理模块，我们以Key-Value的形式存储和获取变量，这样就可以简单的实现全局变量啦。

**全局变量管理模块 global_variable.py**

```python
#!/usr/bin/env python3
# -*- coding:utf-8-*-
# 全局变量管理模块

def _init():
    """在主模块初始化"""
    global GLOBALS_DICT
    GLOBALS_DICT = {}

def set(name, value):
    """设置"""
    try:
        GLOBALS_DICT[name] = value
        return True
    except KeyError:
        return False

def get(name):
    """取值"""
    try:
        return GLOBALS_DICT[name]
    except KeyError:
        return "Not Found"
```

**配置文件, 设置全局变量  config.py**

```python
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 在本模块中定义全局变量

import global_variable as glv

glv._init()

glv._set("APP_NAME", "全局变量测试")
glv._set("author", "doudoudzj")
```

**主程序, 获取全局变量 main.py**

```python
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 主程序

import config  # 加载配置
import global_variable as glv

print(glv._get("APP_NAME"))
print("----")
print(glv._get("author"))
```

**然后运行主程序文件**

```shell
python3 main.py
# 输出内容如下
全局变量测试
----
doudoudzj
```

 