# UGC to JSON Converter <img  src='https://xesque.rocketseat.dev/platform/tech/python.svg' width='24px' title='Python'/>

<div>
<img src='https://img.shields.io/github/last-commit/ruggeryiury/ugc2json-converter?color=%23DDD&style=for-the-badge' />
<img src='https://img.shields.io/github/repo-size/ruggeryiury/ugc2json-converter?style=for-the-badge' />
<img src='https://img.shields.io/github/issues/ruggeryiury/ugc2json-converter?style=for-the-badge' />
<img src='https://img.shields.io/badge/version-v1.2-red?style=for-the-badge' />
<img src='https://img.shields.io/github/license/ruggeryiury/ugc2json-converter?style=for-the-badge' />
</div>

<p align="center">
  <img src="https://github.com/ruggeryiury/ugc2json_converter/blob/master/header.webp?raw=true" alt="Create JSON files without needing to use explicit JSON structure"/>
</p>

UGC (User-Generated Content) files is a more practical way to create JSON files without needing to use explicit JSON structure. It can be used on any projetct that you may have to create JSON files by hand without the need to place brackers and quotation marks to indicates value keys.

# 💠 Table of Contents
- [How to use](#-how-to-use)
- [Declare Class Types](#%EF%B8%8F-declare-class-types)
    - [Root Type](#root-type)
    - [Minify](#minify)
- [Script Variables](#%EF%B8%8F-script-variables)
    - [Scan Subdirectories ON/OFF](#subdirs--read-subdirectories-onoff)
- [Value Types](#-value-types)
    - [Strings](#strings)
    - [Numbers](#numbers)
    - [Booleans](#booleans)
    - [Null Values](#null-values)
    - [Dicts](#dicts)
    - [Lists](#lists)
- [Comments](#-comments)
- [Changelog](https://github.com/ruggeryiury/ugc2json-converter/blob/master/CHANGELOG.md)

## ✅ How to use

- Create a `*.ugc` file with the UGC file structure (see below).
- Place the `ugc2json.py` file on the same directory of your `.ugc` files and execute it.
- JSON files will be generated.

## ⚙️ Declare Class Types
A few features of your generated JSON file can be manipulated by placing `#declare` classes at the very beginning of your UGC file. There's all possible declare options:

### Root Type
The generated JSON file can be both a dict or a list. By default, the script will generate the JSON root as a dict. But if you want the root as a list, you just need to place the following _declarative_ class at the first line of your UGC file:

    #declare list
    [...]

By declaring the root type as a list, the [rules to declare any value to a list](#lists "Lists") must be followed (no key names, only values).

### Minify
The generated JSON file will be generated minified by placing:
    
    #declare minify
    [...]
    
`NOTE` : All these declaring classes can be used together but you have to declare them individually.

    #declare list
    #declare minify
    [...]

## ⭕️ Script Variables
Certain features can be enabled/disabled changing variables on the script, here's all variables:

### `subdirs` : Scan Subdirectories ON/OFF
By default, the script scans for UGC files on the root subdirectories, you can restrict the scanning only for the root folder changing the `subdirs` variable inside the Python script to `False`.

## 📄 Value Types

### Strings

Strings are declared with quotation marks as default, but this rule can be broken if it is a string with a single word (lovely called a "code string").

    code_string_example ugc2json_converter
    normal_string "This is a normal string."

### Numbers

Int and float are declared just by putting the number after the key name.

    int_example 1
    float_example 1.2
    
### Booleans

Booleans are declared putting `TRUE` or `FALSE` (All uppercase) after the key name.

    boolean_example TRUE

### Null Values

Null values are declared putting `NONE` after the key name.

    null_value_example NONE
    
## Dicts

Dicts are declared by placing `#set` and the key name right after. To close it, just place an `#endset` alone.

    #set dict_example
        desc "This "desc" string will be placed inside "dict_example"."
    #endset
    
Inside a list, dicts are declared just by placing `#set`.

    #list list_with_dicts
        #set
            will_be_index 0
        #endset
        #set
            will_be_index 1
        #endset
    #list
    
## Lists

Like dicts, lists are declared by placing `#list` and the key name right after. To close it, just place an `#endlist` alone. By being a list, values are declared alone (without key names)

    #list list_example                                  | List opened
        "This string will be appended at index 0."      | String
        "This, at index 1."                             | String
        "And this at index 2."                          | String
        3                                               | Int
        index_4                                         | String (Code String)
        TRUE                                            | Boolean
    #endlist                                            | List closed

Inside another list, list are declared just by placing `#list`.

    #list list_with_lists
        #list
            "This string will be at index 0 inside a list, that is the index 0 inside the "list_with_lists" list."
        #endlist
        "This string will be at index 1 inside the "list_with_lists" list."
    #list

## ➕ Comments

By now, UGC to JSON Converter only supports __Inline Comments__ only.
To place an inline comment, just use `##` followed by a space and your comment.

    ## This is a comment and will be ignored.
