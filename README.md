# Simple Compressed File Cracker

[![GitHub All Releases](https://img.shields.io/github/downloads/hanerx/rarCracker/total)](https://github.com/hanerx/rarCracker/releases/latest)  ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rarCracker) [![PyPI](https://img.shields.io/pypi/v/rarCracker)](https://pypi.org/project/rarCracker/) ![PyPI - Downloads](https://img.shields.io/pypi/dm/rarCracker) ![GitHub](https://img.shields.io/github/license/hanerx/rarCracker)

A python based compressed file cracker

- generate password from ASCII charset or custom charset using `charset` param

- multi-thread

## Install

### From git

- `git clone https://github.com/hanerx/rarCracker.git ` 

- run `pip install -r requriements.txt`

- make sure you have installed `winrar` or `unar` or `bsdstar` 

- run `python -m rarCracker`

## From release
- download file from [release](https://github.com/hanerx/rarCracker/releases/latest) 
- run `pip install rarCracker-0.0.1.tar.gz`
- run `python -m rarCracker`
## From pip
- run `pip install rarCracker`

## Usage

### Basic

```python
from rarCracker import RarCracker
if __name__ == '__main__':
    cracker = RarCracker('file_path', 3, 3, workers=2, charset='1234567890')
    cracker.crack()
```

### Use Local Dictionary

```python
from rarCracker import RarCracker, LocalProvider

if __name__ == '__main__':
    cracker = RarCracker('./test.rar', provider=LocalProvider('./dict.txt'), unrar_tool='unrar')
    print(cracker.crack())
```

### Use Network Dictionary

```python
from rarCracker import RarCracker, NetworkProvider

if __name__ == '__main__':
    cracker = RarCracker('./test.rar', provider=NetworkProvider('https://hanerx.top/rarCracker/dict.json',
                                                                method=NetworkProvider.GET))
    print(cracker.crack())

```

### Use Breakpoint

```python
from rarCracker import RarCracker, LocalProvider, LocalBreakPoint

if __name__ == '__main__':
    cracker = RarCracker('./test.rar', provider=LocalProvider('./dict.txt'), unrar_tool='unrar',
                         break_point=LocalBreakPoint(breakpoint_count=1))
    print(cracker.crack())
```





## API

### RarCracker

The main class for module

#### params

| name       | type     | desc                                                         | default                              | required |
| ---------- | -------- | ------------------------------------------------------------ | ------------------------------------ | -------- |
| file_path  | str      | the compressed file path, if file does not exist raise `FileNotFoundError` , if file is not `.rar` or `.zip` raise `TypeError` | None                                 | True     |
| start      | int      | the minimum password length                                  | 1                                    | False    |
| stop       | int      | the maximum password length                                  | 10                                   | False    |
| charset    | str      | the password charset                                         | digits + ascii_letters + punctuation | False    |
| output     | str      | the output folder                                            | './output'                           | False    |
| workers    | int      | the number of multi thread                                   | 8                                    | False    |
| level      | int      | the logging display level                                    | logging.INFO                         | False    |
| unrar_tool | str      | the decompressing tool, support `unrar` \ `unar` \ `bsdtar`  | 'unrar'                              | False    |
| provider   | Provider | the password provider, if provider is not `None` it will replace original password generator and `start` \ `stop` \ `charset` will not work | None                                 | False    |

#### Methods

##### crack()

- The method which start cracking, will block until all threads done or password found, if crack failed it will return `None`

- return `None` or `str`

##### generate_password()

- The method which will return an iterator for password

- return `iter`

### Provider
The abstract class for provider param
#### Methods
##### generate(file)
- The method which will return an iterator for password
- return `iter`

### DefaultProvider

The default password provider

#### Param

| name    | type | desc                        | default                              | required |
| ------- | ---- | --------------------------- | ------------------------------------ | -------- |
| start   | int  | the minimum password length | 1                                    | False    |
| stop    | int  | the maximum password length | 10                                   | False    |
| charset | str  | the password charset        | digits + ascii_letters + punctuation | False    |

#### Methods

##### generate(file)

- The method which will return an iterator for password
- return `iter`

### LocalProvider

The class allows to get password from local dictionary

#### Param

| name | type | desc                                                         | default | required |
| ---- | ---- | ------------------------------------------------------------ | ------- | -------- |
| path | str  | the dictionary file path, if file does not exist raise `FileNotFoundError` | None    | True     |

#### Methods

##### generate(file)

- The method which will return an iterator for password
- return `iter`

### NetworkProvider

The class allows to get password from network dictionary

#### Param

| name      | type   | desc                                                         | default                     | required |
| --------- | ------ | ------------------------------------------------------------ | --------------------------- | -------- |
| url       | str    | the url of the dictionary                                    | None                        | True     |
| method    | method | the method of request, support `GET` \  `POST` \ `PUT` \ `DELETE` \ `OPTION` \ `HEAD` | NetworkProvider.GET         | False    |
| on_decode | method | the decode method for response                               | self.default_decode(result) | False    |
| **kwargs  |        | support params for `requests` module                         | None                        | False    |

#### Methods

##### default_decode(result)

- The method which will decode the response by default
- accept json format array, for example `["123","124","125"]`
- return `list`

##### generate(file)

- The method which will return an iterator for password
- return `iter`

### BreakPoint

The abstract class for break_point param

#### Methods

##### generate(provider,file)

- The method which will return a iterator for password with breakpoint supported
- return `iter`

### DefaultBreakPoint

The default breakpoint when break_point param is None

#### Methods

##### generate(provider,file)

- The method which will return a iterator for password with breakpoint supported
- return `iter`

### LocalBreakPoint

The breakpoint will save cracking count number into local file and recover the progress from local file

#### Param

| name             | type | desc                                                         | default            | required |
| ---------------- | ---- | ------------------------------------------------------------ | ------------------ | -------- |
| breakpoint_path  | str  | the breakpoint file path, if file does not exist counter will start at 0 | './breakpoint.txt' | False    |
| breakpoint_count | int  | the interval between two breakpoint                          | 1000               | False    |