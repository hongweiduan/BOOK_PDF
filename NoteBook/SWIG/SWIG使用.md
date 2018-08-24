# SWIG 使用

# 安装

- brew install swig

# C++ to Python
- 添加C 代码
```c
/* File : example.c */

 #include <time.h>
 double My_variable = 3.0;

 int fact(int n) {
     if (n <= 1) return 1;
     else return n*fact(n-1);
 }

 int my_mod(int x, int y) {
     return (x%y);
 }
 	
 char *get_time()
 {
     time_t ltime;
     time(&ltime);
     return ctime(&ltime);
 }

```

- 添加接口文件
```c
/* example.i */
 %module example
 %{
 /* Put header files here or function declarations like below */
 extern double My_variable;
 extern int fact(int n);
 extern int my_mod(int x, int y);
 extern char *get_time();
 %}
 
 extern double My_variable;
 extern int fact(int n);
 extern int my_mod(int x, int y);
 extern char *get_time();
```

- 运行shell指令 Python 接口

```sh
swig -python example.i
cc -c `python-config --cflags` example.c example_wrap.c
cc -bundle `python-config --ldflags` example.o example_wrap.o -o _example.so
```
生成的文件保存_example.so和example.py, python中就可以使用对应的模块了。

- Lua接口

```sh
swig -lua example.i
cc -c example.c example_wrap.c -I/Users/mac/Desktop/SWIG/lua-5.1.4/src
cc -bundle -undefined dynamic_lookup example.o example_wrap.o -o example.so
```

其中**/Users/mac/Desktop/SWIG/lua-5.1.4/src**  为Lua 源代码中 lua.c 的路径。

保存生成的example.so文件。

- 参考网页及博客：

  https://github.com/swig/swig/wiki/FAQ#shared-libraries

  http://www.swig.org/translations/chinese/index.html

  https://blog.csdn.net/themagickeyjianan/article/details/78493913

  

