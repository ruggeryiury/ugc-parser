# Changelog

## December 18th, 2022
### Changes
  - `JSON 2 UGC` -- Added `null` value entries feature
    - You can now place `null` values placing `NONE` after the key code.

## July 30th, 2022
### Changes
  - `JSON 2 UGC` -- Initial release.
    - Now you can generate UGC files from JSON files!

## July 14th, 2022
### Changes
- `UGC 2 JSON` -- Added new Declaring feature: _Minify_
  - Now you can declare to minify generated JSON file by placing `#declare minify`.

- `UGC 2 JSON` -- Added new script variable: _Read Subdirectories_
  - By default, the script reads all UGC files of the root folder (where the script file was placed) and its subdirectories. Changing the `subdirs` variable on `ugc2json.py` to `False` will restrict the convertion for UGC files found on the root folder.

## July 12th, 2022
### Changes
- `UGC 2 JSON` -- Added new Declaring feature: _Declaring Root Type_
  - Now you can declare if the type of the generated JSON file is a dict or a list. By default, the type of the generated JSON file is a dict, but you can change to a list placing `#declare list` on the first line of your UGC file.

- `UGC 2 JSON` -- Added _Inline Comments_ feature
  - Now you can create inline comments on your UGC files using `## [...]`.

## July 11th, 2022
- `UGC 2 JSON` -- Initial release.
