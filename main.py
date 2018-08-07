#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 主程序


import config  # 加载配置
import global_variable as glv

print(glv._get("APP_NAME"))
print("----")
print(glv._get("author"))
