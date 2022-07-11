# UGC to JSON Converter
UGC (User-Generated Content) files is a more practical way to create JSON files without needing to use explicit JSON structure. It can be used on any projetct that you may have to create JSON files by hand without the need to place brackers and quotation marks to indicates value keys.

## ✅ How to use

- Create a `*.ugc` file with the UGC file structure (see below).
- Place the `ugc2json.py` file on the same directory of your `.ugc` files and execute it.
- JSON files will be generated.

## ⚙️ UGC File Structure

to be added.

## 📄 Types

### Strings

Strings are declared with quotation marks as default, but this rule can be broken if it is a string with a single word (lovely called a "code string").

    code_string_example ugc_parser
    normal_string "This is a normal string."

### Numbers

Int and float are declared just by putting the number after the key name.

    int_example 1
    float_example 1.2
    
### Booleans

Booleans are declared putting `TRUE` or `FALSE` (All uppercase) after the key name.

    boolean_example TRUE
    
## Dicts

Dicts are declared by placing `#set` and the key name right after. To close it, just place an `#endset` alone.

    #set dict_example
        desc "This "desc" string will be placed inside "dict_example"."
    #endset
    
## Lists

Like dicts, lists are declared by placing `#list` and the key name right after. To close it, just place an `#endlist` alone.

    #list list_example
        "This string will be appended at index 0."
        "This, at index 1."
        "And this at index 2."
    #endlist

