# CRATE-STASH NOTES©

# Learning

## Parsing
* There are 3 different methods to parse data (json) in Python:
  1. `Path.exists()`
  2. `os.path.isfile()`
  3. `try/except`

### `with open`*(Context Manager)* 
* Before writing to a .json file, instead of checking first to see if the file already exists, the Pythonic way is to
  **try** to open it and handle the error if it's missing by using **except**
  * AKA - _Easier to Ask for Forgiveness than Permission_ (**EAFP**)
* Common **modes** and their meanings when using the `with open` context manager:
  * `"r"` - Read (default)
  * `"w"` - Write (overwrites file)
  * `"a"` - Append (adds to file)
  * `"x"` - Create (fails if file exists)
* `with open` automatically closes JSON file by calling `close()` so that data is not lost


### `json.dumps method`
* Next, writing to a .json file, the data needs to be **serialized** into a JSON-formatted string so it can be stored
  * To do this, it is best practice to use the `json.dumps` method
### **