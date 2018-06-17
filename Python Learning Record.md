<h1>Python Learning Record</h1>

#### 前言
Python Learning Record即是Python学习记录，装装逼用用英文，仅此。

写这篇Markdown的目的，是为了记录Python学习中的林林总总。学习Python的目的是为了以后的人工智能时代做准备，即便未来不做人工智能，Python在数据处理，数据抓取上也有很强的优势，是个强大的数据工具。

代码块部分，有一部分是伪代码，但大部分都是可执行代码，注意甄别。

> 开发环境：Python版本3.6.5，代码编辑器：Sublime Text/Python IDLE，编译器：Shell/Windows PowerShell-Python

[comment]: <> (This is a comment, it will not be included)
[comment]: <> (in  the output file unless you use it in)
[comment]: <> (a reference style link.)
[//]: <> (This is also a comment.)
[//]: # (This may be the most platform independent comment)
[^_^]:(参考链接编写格式： [[text]]（web）PS：此处应为半角括号，因为Markdown注释显示的原因，才用了全角) 
#### 参考：
[[Sublime Text 快捷键]](http://www.cnblogs.com/fan-fan/p/4526817.html) [[Python官网]](https://www.python.org/) [[Python官方文档]](https://docs.python.org/3/)

<h2>名词解释</h2>

<h3>什么是“交互式python解释器”？</h3>
- 它其实是一种让源代码程序运行起来的解释翻译工具，解释器将读取程序，并按照程序中的一些命令语句来执行程序，最终按要求显示结果。
- 当你看到“>>>”符号，就意味着你进入交互式python解释器，又称作“提示符”。
- 注意：python不同于其他的计算机语言，每行以分号结束；python的一行就是一行，不管多少。
- 在python中如果每行结束时加了分号会怎样呢？ 加上分号不影响程序，但也不会有任何作用。

<h3>什么是变量？</h3>
概念：变量可以指在计算机存储器里存在值的被命名的存储空间。变量可以指在计算机存储器里存在值的被命名的存储空间。[Wiki-变量](https://zh.wikipedia.org/wiki/%E8%AE%8A%E6%95%B8)
> Python有五种标准数据类型：数字、字符串、列表、元组、字典  
> Python在定义变量时不需要表示类型，而C#需要  
> Python的变量属于弱类型变量  
> 强制转换需要声明变量类型

- 变量：可变的量
- 组成：名称+所代表的数据
- 例子：李雷的成绩 = 98、班级平均成绩 = 班级成绩总和/班级人数
- 利用等于号（=）为变量赋值
- 格式：变量名 = 要存储的内容
- 同时给多个变量赋值：a = b = c = 100（赋相同值）width,height = 640,480（赋不同值）
- 规范：等号两边加空格（高可读性）[More](http://www.cnblogs.com/Maker-Liu/p/5528213.html)
```
#代码示例

#新建两个变量并赋值
lilei = 95
hanmeimei = 98
print(lilei+hanmeimei) #计算期中成绩
#变量重新赋值
lilei = 90
hanmeimei = 100
print(lilei+hanmeimei) #计算期末成绩
```

<h3>什么是函数？</h3>
概念：函数（Function）是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。函数能提高应用的模块性，和代码的重复利用率。[Wiki-(数学意义的)函数](https://zh.wikipedia.org/wiki/%E5%87%BD%E6%95%B0)
> 你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。  
> **def**是define的缩写，表示定义一个函数。  
> 你可以将++函数++理解为一种++方法++。

<h4>定义一个函数</h4>
你可以定义一个由自己想要功能的函数，以下是简单的规则：
- 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
- 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
- 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
- 函数内容以冒号起始，并且缩进。
- return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
- 注意！函数中间**不要**有空格，想要空格的地方可以用下划线代替。

<h5>语法</h5>
默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的。  
值得一提的是，Python中相同的代码块要用相同的缩进，C#中相同的代码块用的是花括号。
```
def functionname( parameters ):
   "函数_文档字符串"
   function_suite
   return [expression]
```

<h5>函数调用</h5>
- 定义一个函数只给了函数一个名称，指定了函数里包含的参数，和代码块结构。
- 这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从Python提示符执行。

如下实例调用了printme()函数：
```
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 定义函数
# 请注意，这不是Python3的写法
def printme( str ):
   "打印任何传入的字符串"
   print str;
   return;
 
# 调用函数
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");
```

四种类型的函数：
```
# 无参数，无返回值
def say_hi_0():
    print('Hi!')
say_hi_0()

# 有参数，无返回值
def say_hi_1(name):
    print('Hi!')
    print("I'm "+name)
say_hi_1('Felix')

# 有参数，有返回值
def add(a,b):
    sum_number = a + b
    return sum_number
value_0 = add(12,13)
print(value_0)

# 无参数，有返回值
def getNum():
    return 2333
num = getNum()
print(num)
```

<h3>数据的类型？</h3>

<h4>数字：整数和浮点数</h4>
PS：在编程中，整数和浮点数是有区别的，如果你用的是浮点数，那么程序就会用浮点数的计算方法，即便12与12.0在数学上是相等的，这是一个要注意的点。
```
grade = 100
number = 12

grade = 98.5
number = 12.0
```

<h4>字符串：</h4>
在Python当中，单引号和双引号都可以表示数据类型是字符串。
```
name = 'Felix'
university = "Tsinghua University"
print(name+' '+university)
# 输出：Felix Tsinghua University
```

<h4>列表：</h4>
在Python当中，列表要用中括号括起来。列表类似C#的数组和List泛型集合。
```
names = ["Felix","Jinfeng","Xiaoming"]
universities = ["Tsinghua","Peking","MIT"]
grades = [90,100,95]
```

<h4>字典：</h4>
Python的字典跟列表有点像，字典存储的也是一组数据。区别就是字典里的每个关键字会对应一个值，而列表只能存储数据而且也没有关键字。字典用的是花括号。
```
grades = {"Felix":"100","Xiaoming":"60"}
Phone_numbers = {"Felix":"189","Xiaoming":"153"}
```

<h4>元组：</h4>
元组用圆括号括起来，元组里的数据只能访问，不能修改。一般用得比较少。
```
t = (10,20,30,"Felix")
```

<h4>集合：</h4>
集合是无序的，和数学上的集合一样可以做集合的运算。
```
a = {10,20,30,40,50,60}
b = {20,40,60}

Print(a-b)
# 输出：{10,30,50}
```

<h3>什么是字符串？</h3>

<h4>字符串的创建</h4>
> Python当中用引号引起来的（大概）都是字符串

```
name = 'Felix'
number = '2018'
paragraph = '''Hello,Felix!
Hello,World!'''

print(name)
print(number)
print(paragraph)
```

<h4>字符串的引号</h4>
注意引号的用法
```
# 双引号括单引号
sentence01 = "I'm Felix."
# 单引号括双引号
sentence02 = 'Maker "Felix".'
# 三个单引号换行
sentence03 = '''Hello!
I'm Felix.'''
```

<h4>字符串中字符的获取</h4>
```
name = 'hanmeimei'
print(name[0])
# 输出：h

# 从第0个开始获取的话**冒号**前面的数字可以省略
print(name[3:6])
# 输出：mei
```

<h4>字符串的添加</h4>
```
s1 = 'hello'
s2 = 'world'

print(s1+s2)
print(s1,s2)
# 两个print的结果都是helloworld
```

<h4>字符串的长度</h4>
len()输出的结果是一个int类型值
```
s1 = 'hello world'
s2 = 'makerworld'

print(len(s1))
# 输出：11
print(len(s2))
# 输出：10
print(len(s1)+len(s2))
# 输出：21
```

<h4>字符串的转义</h4>
在计算机科学与远程通信中，转义字符是这样一个字符，标志着在一个字符序列中出现在它之后的后续几个字符采取一种替代解释。[wiki-转义字符](https://zh.wikipedia.org/wiki/%E8%BD%AC%E4%B9%89%E5%AD%97%E7%AC%A6)

Python也有原始字符串的机制，在字符串前加上“r”即可：  
参见：[wiki-倾斜牙签综合症](https://zh.wikipedia.org/wiki/%E5%80%BE%E6%96%9C%E7%89%99%E7%AD%BE%E7%BB%BC%E5%90%88%E7%97%87)

```
filePath = r"C:\Foo\Bar.txt"
```

**常用转义符：**
转义符|含义|转义符|含义
---|---|---|---
\n | 换行       |\b  |退格
\' | 单引号     |\v  |横向制表符
\" | 双引号     |\r  |回车
\t | 纵向制表符 |\\\ |反斜杠符号

```
s1 = 'hello\nworld'
s2 = 'I\'m a maker'
```

<h4>读取用户输入</h4>
input()这个函数的作用是读取用户输入，类似C#的Console.ReadLine()；
```
user_input = input()
print(user_input)

# input()括号内可填入提示性文字
user_input = input('Type>')
print('You typed:'+user_input)

# 判断用户输入是否是数字
user_input = input('Type a number>>>')
if user_input.isdigit():
	print('true')
	num = int(user_input)
	print('number + 233 = ',num+233)
else :
	print('false')
```

<h4>程序化生成简历</h4>
这里是一段程(ran)序(bing)化(luan)生成简历的Python代码
> 代码里面用了format的两种格式：%s 以及 .format  
> 格式化：[string — Common string operations](https://docs.python.org/3/library/string.html)  
> 不同的代码块之间可以**空出一行**以便代码有更高的可读性  
> 注意区分段落*3！

```
# 生成程序化简历
name = input('Type your name>')
age = input('Type your age>')
gender = input('Type your gender>')
school = input('Type your school>')
print('正在生成您的简历···')
import time
print ("Start : %s" % time.ctime())
time.sleep(5)
print ("End : %s" % time.ctime())
print('*'*21)
print('\t简历')
import datetime
print('姓名：{0}\n年龄：{1}\n性别：{2}\n学校：{3}\n{4}\n{5[0]}\n{5[1]}\n{i}\n{time}'.format(name,age,gender,school,'*'*21,['Have fun!','See you next time!'],i='Made in MS(Matrix Studio)',time = datetime.datetime.now()))
```

<h4>另一段格式化代码</h4>
> 以下代码描述了两种格式化的基本写法
```
class Person:
	def __init__(self,name,age):
		self.name,self.age = name,age
	# def __str__(self):
	# 	return 'This guy is {self.name},is {self.age} old'.format(self=self)
	def __repr__(self):
		return 'This guy is {self.name},is {self.age} old'.format(self=self)
# str(Person('Lee',18)) # 这段代码需要到交互式解释器实现
felix = Person('Felix',18)
print(felix)
# 在object中，__str__和__repr__都是返回对object的描述，前一个简短，后一个复杂
from datetime import datetime as dt
print(dt.today().__str__())
print(dt.today().__repr__())
```