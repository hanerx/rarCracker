# Simple Compressed File Cracker

A python based compressed file cracker

- generate password from ASCII charset or custom charset using `charset` param

- multi-thread

## Install

- download file

- run `pip install -r requriement.txt`

- make sure you have installed `winrar` or `unar` or `bsdstar` 

- run `python ./main.py` for example

## Usage

```python
if __name__ == '__main__':
    cracker = RarCracker('file_path', 3, 3, workers=2, charset='1234567890')
    cracker.crack()
```



## Param

| name       | type | desc                                                         | default                              | required |
| ---------- | ---- | ------------------------------------------------------------ | ------------------------------------ | -------- |
| file_path  | str  | the compressed file path, if file does not exist raise `FileNotFoundError` , if file is not `.rar` or `.zip` raise `TypeError` | None                                 | True     |
| start      | int  | the minimum password length                                  | 1                                    | False    |
| stop       | int  | the maximum password length                                  | 10                                   | False    |
| charset    | str  | the password charset                                         | digits + ascii_letters + punctuation | False    |
| output     | str  | the output folder                                            | './output'                           | False    |
| workers    | int  | the number of multi thread                                   | 8                                    | False    |
| level      | int  | the logging display level                                    | logging.INFO                         | False    |
| unrar_tool | str  | the decompressing tool, support `unrar` \ `unar` \ `bsdtar`  | 'unrar'                              | False    |

