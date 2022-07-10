# UGC Parser
UGC (User-generated content) files is a more practical way to create JSON files without needing to use explicit JSON structure. It can be used on any projetct that you may have to create JSON files by hand without the need to place brackers and quotation marks to indicates value keys.

## 📄 File Structure

### Basic Values: String / Numbers (Integrer/Float) / Booleans

    .
    ├── ...
    ├── META
    │   └── content
    │       └── songs
    |           ├── songname
    |               ├── gen
    |                   └── songname_keep.png_wii            # The ARTWORK file
    |               └── songname_prev.bik                    # The PREVIEW file
    |           └── songs.dta
    |
    ├── SONG
    │   └── content
    │       └── songs
    |           ├── songname
    |               ├── gen
    |                   └── songname.milo_wii                # The MILO file
    |               └── songname.bik                         # The MULTITRACK BIK file
    |               └── songname.mid                         # The MIDI file
    └── ...
