# flatbuffers-demo
Programming language used:</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C++</br>
## Configuration of System used for developing 
<pre>
OS : 
  Windows 10
  
Softwares : 
  python==3.9.1,
  g++==11.2.0, (g++ used with MinGW)  
</pre>
  
## c++ : steps to execute

- Move to **cpp** folder
```
$ cd cpp
```

- Generate header file using flatbuffer compiler
```
$ ..\bin\flatc.exe -c -b ..\schema.fbs
```
Above cmd will generate **schema_generated.h** in cpp\ folder

- compile **fb_encoder.cpp** and **fb_decoder.cpp**
```
$ g++ -I ../ ../cpp/fb_encoder.cpp -o fb_encoder.exe
$ g++ -I ../ ../cpp/fb_decoder.cpp -o fb_decoder.exe
```

- run **encoder**
```
$ fb_encoder.exe 
```

- run **decoder**
```
$ fb_decoder.exe
```

## python : steps to execute

- Move to **cpp** folder
```
$ cd py
```

- Generate header file using flatbuffer compiler
```
$ ..\bin\flatc.exe -p -b ..\schema.fbs
```
Above cmd will generate **ORM classes** in py\ folder

- run **encoder**
```
$ python fb_encoder.py
```

- run **decoder**
```
$ python fb_decoder.py
```
