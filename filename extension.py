Python 3.2.3 (default, Apr 11 2012, 07:15:24) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> fileName=input("Write the fileName")
Write the fileName abc.python
>>> file_extns= fileName.split(".")
>>> print("the extension is" + repr(file_extns[-1]))
the extension is'python'
>>> 
