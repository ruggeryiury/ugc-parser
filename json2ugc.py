# JSON 2 UGC CONVERTER
# Version 1.0
#
# Created by Ruggery Iury Corrêa
# GitHub: https://github.com/ruggeryiury
#
# Get the latest version of this script through the
# UGC to JSON Converter GitHub Repository
# https://github.com/ruggeryiury/ugc2json_converter

from io import TextIOWrapper
import json
import os
from types import NoneType


# Change this 'subdirs' variable to False if you want
# UGC files from subdirectories to be converted
subdirs = True




def json_to_ugc(root: str, file_name: str) -> None:
    operators = 0
    json_file: dict = json.load( open(os.path.join(root, '{}.json'.format(file_name)), 'r', encoding='utf-8'))
    new_file = open(os.path.join( root, '{}.ugc'.format(file_name)), 'w', encoding='utf-8')
    root_list = False

    def write_key(new_file: TextIOWrapper, key: str, value: str | int | float | bool, type: str, operator: int) -> TextIOWrapper:
        for i in range(operator):
            new_file.write('\t')

        if type == 'code':
            try:
                if value[0] == "0":
                    new_file.write(f'{key} "{value}"')
                else:
                    new_file.write(f'{key} {value}')
            except IndexError:
                new_file.write(f'{key} ""')

        elif type == 'str':
            new_file.write(f'{key} "{value}"')

        elif type == 'number':
            new_file.write(f'{key} {value}')

        elif type == 'bool':
            if value:
                new_file.write(f'{key} TRUE')
            else:
                new_file.write(f'{key} FALSE')

        elif type == 'null':
            new_file.write(f'{key} NONE')


        new_file.write('\n')

        return new_file

    def write_key_for_list(new_file: TextIOWrapper, value: str | int | float | bool, type: str, operator: int) -> TextIOWrapper:
        for i in range(operator):
            new_file.write('\t')

        if type == 'code':
            try:
                if value[0] == "0":
                    new_file.write(f'"{value}"')
                else:
                    new_file.write(f'{value}')
            except IndexError:
                new_file.write(f'""')

        elif type == 'str':
            new_file.write(f'"{value}"')

        elif type == 'number':
            new_file.write(f'{value}')

        elif type == 'bool':
            if value:
                new_file.write(f'TRUE')
            else:
                new_file.write(f'FALSE')

        elif type == 'null':
            new_file.write(f'NONE')


        new_file.write('\n')

        return new_file
        
    def write_set(new_file: TextIOWrapper, key: str, value: dict, operator: int, for_list: bool = False) -> TextIOWrapper:
        if for_list:
            for i in range(operator):
                new_file.write('\t')
            new_file.write(f'#set\n')
        else:
            for i in range(operator):
                new_file.write('\t')
            new_file.write(f'#set {key}\n')

        operator += 1

        for post_key, post_value in value.items():
            if type(post_value) is str:
                if len(post_value.split()) == 1:
                    new_file = write_key(new_file, post_key, post_value, 'code', operator)
                elif len(post_value.split()) == 0:
                    new_file = write_key(new_file, post_key, "", 'code', operator)
                else:
                    new_file = write_key(new_file, post_key, post_value, 'str', operator)
            elif type(post_value) is int or type(post_value) is float:
                new_file = write_key(new_file, post_key, post_value, 'number', operator)
            elif type(post_value) is bool:
                new_file = write_key(new_file, post_key, post_value, 'bool', operator)
            elif type(post_value) is NoneType:
                new_file = write_key(new_file, post_key, post_value, 'null', operator)
            elif type(post_value) is dict:
                new_file = write_set(new_file, post_key, post_value, operator)
            elif type(post_value) is list:
                new_file = write_list(new_file, post_key, post_value, operator)

        operator -= 1
        for i in range(operator):
            new_file.write('\t')
        new_file.write(f'#endset\n')

        return new_file

    def write_list(new_file: TextIOWrapper, key: str, value: list, operator: int, for_list: bool = False) -> TextIOWrapper:
        if for_list:
            for i in range(operator):
                new_file.write('\t')
            new_file.write(f'#list\n')
        else:
            for i in range(operator):
                new_file.write('\t')
            new_file.write(f'#list {key}\n')

        operator += 1

        for i in value:
            if type(i) is str:
                if len(i.split()) == 1:
                    new_file = write_key_for_list(new_file, i, 'code', operator)
                elif len(i.split()) == 0:
                    new_file = write_key_for_list(new_file, "", 'code', operator)
                else:
                    new_file = write_key_for_list(new_file, i, 'str', operator)
            elif type(i) is int or type(i) is float:
                new_file = write_key_for_list(new_file, i, 'number', operator)
            elif type(i) is bool:
                new_file = write_key_for_list(new_file, i, 'bool', operator)
            elif type(i) is NoneType:
                new_file = write_key_for_list(new_file, i, 'null', operator)
            elif type(i) is dict:
                new_file = write_set(new_file, "", i, operator, True)
            elif type(i) is list:
                new_file = write_list(new_file, "", i, operator, True)

        operator -= 1
        for i in range(operator):
            new_file.write('\t')
        new_file.write(f'#endlist\n')

        return new_file

    if type(json_file) is list:
        new_file.write('#declare list\n\n')
        root_list = True
    else:
        pass

    if root_list:
        for i in json_file:
            if type(i) is str:
                if len(i.split()) == 1:
                    new_file = write_key_for_list(new_file, i, 'code', operators)
                elif len(i.split()) == 0:
                    new_file = write_key_for_list(new_file, "", 'code', operators)
                else:
                    new_file = write_key_for_list(new_file, i, 'str', operators)
            elif type(i) is int or type(i) is float:
                new_file = write_key_for_list(new_file, i, 'number', operators)
            elif type(i) is bool:
                new_file = write_key_for_list(new_file, i, 'bool', operators)
            elif type(i) is NoneType:
                new_file = write_key_for_list(new_file, i, 'null', operators)
            elif type(i) is dict:
                new_file = write_set(new_file, "", i, operators, True)
            elif type(i) is list:
                new_file = write_list(new_file, "", i, operators, True)
    else:
        for key, value in json_file.items():
            if type(value) is str:
                if len(value.split()) == 1:
                    new_file = write_key(
                        new_file, key, value, 'code', operators)
                elif len(value.split()) == 0:
                    new_file = write_key(
                        new_file, key, "", 'code', operators)
                else:
                    new_file = write_key(new_file, key, value, 'str', operators)
            elif type(value) is int or type(value) is float:
                new_file = write_key(new_file, key, value, 'number', operators)
            elif type(value) is bool:
                new_file = write_key(new_file, key, value, 'bool', operators)
            elif type(value) is NoneType:
                new_file = write_key(new_file, key, value, 'null', operators)
            elif type(value) is dict:
                new_file = write_set(new_file, key, value, operators)
            elif type(value) is list:
                new_file = write_list(new_file, key, value, operators)



script_path: str = os.path.dirname(__file__)
def init() -> None:
    """
    Main function: JSON to UGC Converter.
    """
    for root, dirs, files in os.walk(script_path):
        if subdirs:
            for file in files:
                if file.endswith(".json"):
                    file_name = file[:-5]
                    json_to_ugc(root, file_name)
        else:
            if root == script_path:
                for file in files:
                    if file.endswith(".json"):
                        file_name = file[:-5]
                        json_to_ugc(root, file_name)
            else:
                pass


init()
