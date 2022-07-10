# UGC Parser
UGC (User-generated content) files is a more practical way to create JSON files without needing to use explicit JSON structure. It can be used on any projetct that you may have to create JSON files by hand without the need to place brackers and quotation marks to indicates value keys.

## How to use

- Create a `*.ugc` file with the UGC file structure (see below).
- Place the `ugc.py` file on the same directory of your `.ugc` files and execute it
- JSON files will be generated! Yay!

## 📄 File Structure

### Strings

Strings are declared with quotation marks as default, but this rule can be broken if it is a string with a single word (lovely called a "code string").

    code_string value_with_no_space
    normal_string "This is a normal string"

### Integrers/Float

Integrers and float numbers are declared just by putting the number after the key, the parser will check if the given number is really a number and declare if it is.

    integrer 1
    float 1.2
    
### Booleans

Booleans are declared putting `TRUE` or `FALSE` (All uppercase) after the key.

    boolean TRUE
    
### Dictionaries

Dicts are declared by placing `#set` and the key of the dict right after. All followed keys/values will be placed on this dict until you close it an `#endset` line.

    #set dict_example
        desc "This \"desc\" string will be placed on the \"disc_example\" dict.
    #endset
    
## Lists

Like dictionaries, lists are declared by placing `#list` and the key of the list right after. All followed values will be appended on this list until you close it with an `#endlist` line.

    #list list_example
        "This string will be appended at index 0"
        "This, at index 1"
        "And this at index 2"
        "Hope you got it right lol"
    #endlist
    
## ❗️ Known imitations/To-do List

- [ ] You can't declare dicts inside a list, this is a feature that may be added later.
