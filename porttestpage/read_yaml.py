# _*_ coding: utf-8 _*_
# @Time     : 2022/4/25 20:24
# @Author   : Mr_Li
# @FileName :
import yaml


def Read_Yaml(yaml_path):
    with open(yaml_path, 'r', encoding='UTF-8') as yml:
        yaml_data = yaml.load(yml, yaml.FullLoader)
    return yaml_data
