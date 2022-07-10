# UGC Parser
UGC (User-generated content) files is a more practical way to create JSON files without needing to use explicit JSON structure. It can be used on any projetct that you may have to create JSON files by hand without the need to place brackers and quotation marks to indicates value keys.

## 📄 File Structure

### String

Strings are declared with quotation marks as default, but this rule can be broken if it is a string with a single word (lovely called a "code string")

    code_string value_with_no_space
    normal_string "This is a normal string"
