#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""
 @Time : 2020/4/4 20:39 
 @Author : ZHANG 
 @File : prepare_data.py 
 @Description:
"""

import json
from shutil import copyfile

input = "/dlwsdata3/yiyifrisky/bdd/bdd100k/images/100k/bdd100k_labels_images_train.json"
str = "/dlwsdata3/yiyifrisky/bdd/bdd100k/images/100k/train/"
dst_day = "/dlwsdata3/yiyifrisky/bdd/bdd100k/images/100k/daytime100/"
dst_night = "/dlwsdata3/yiyifrisky/bdd/bdd100k/images/100k/night100/"
dst_dusk = "/dlwsdata3/yiyifrisky/bdd/bdd100k/images/100k/dusk/"

f = open(input)
f_data = json.load(f)
i, j = 0, 0
for img in f_data:
    name = img['name']
    att = img['attributes']
    if att['timeofday'] == 'daytime':
        i += 1
        if i > 5000 and i <= 5100:
            copyfile(str + name, dst_day + name)
    elif att['timeofday'] == 'night':
        j += 1
        if j > 5000 and j <= 5100:
            copyfile(str + name, dst_night + name)
print(i, j)