#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/3/16 23:23
# @FileName : test.py
# @Author : RicahrdYang
import torch

if __name__ == "__main__":
    print(torch.__version__)
    print(torch.cuda.is_available())