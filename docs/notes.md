# CRATE-STASH NOTES©

# Learning Lessons

## Glossary
* **Refactor** - improve code structure without changing behavior
* 

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
    * Tends to easily break JSON structure because a JSON fil is supposed to contain one valid JSON structure 
      (a single dictionary/object)
  * `"x"` - Create (fails if file exists)
* `with open` automatically closes JSON file by calling `close()` so that data is not lost


### *`json.dump` vs. `json.dumps`*
* Next, writing to a .json file, the data needs to be **serialized** into a JSON-formatted string so it can be stored
  * To do this, it is best practice to use the `json.dumps` method
* `json.dump()` directly saves data to a local file without storing the entire formatted string in a system's RAM, 
  therefore, being more memory-efficient for large data sets. It already includes `file.write()`!
* `json.dumps`, the "s" stands for __string__ and converts your data into a JSON-formatted string in memory. This method
  requires `file.write()` if you eventually want to save it to disk
* Why bother using `json.dumps()`?!:
  * Because it is essential when you need the JSON data as a string in memory rather than a physical file on your 
    hard-drive

### *`json.load` vs `json.loads`*
* The `json.load()` function accepts a **file object** (the pointer created by `open`) and parses the JSON content 
  directly into a native Python object, such as a dictionary or a list
  * Use `json.load` if the object you need Python to read the content directly from a file on your disk
* The `json.loads()` (load string) is used when the JSON data is already loaded into your code's memory as text
  * Use if the data is already a string inside quotes ("..."), like data that comes from a network request

### *Expression Evaluation & Discarding*
* In programming, any line of code that produces a result is an **expression**
  * When you call `json.load(file)`, Python runs the function and computes a result
  * BUT, if you do not assign that result to a variable or pass it to another function, the term for what happens is
    **discarding the return value**. The data is momentarily generated in memory, but because there is no reference to
    it, Python instantly discards it

### *Garbage Collection*
* Core memory management system