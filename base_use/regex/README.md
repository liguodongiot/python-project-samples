

## 语法
<img width="800" alt="regex" src="./image/regex.jpg">


验证工具, [链接](http://regexr.com/)

正则表达式进阶练习，[链接](https://alf.nu/RegexGolf)

**re 模块**

Python 通过 re 模块提供对正则表达式的支持。

使用 re 的一般步骤是
* 1.将正则表达式的字符串形式编译为Pattern实例
* 2.使用Pattern实例处理文本并获得匹配结果（一个Match实例）
* 3.使用Match实例获得信息，进行其他的操作。


`re.compile(strPattern[, flag])`:
这个方法是Pattern类的工厂方法，用于将字符串形式的正则表达式编译为Pattern对象。

第二个参数flag是匹配模式，取值可以使用按位或运算符'|'表示同时生效，比如`re.I | re.M`。

当然，你也可以在regex字符串中指定模式，比如`re.compile('pattern', re.I | re.M)`等价于`re.compile('(?im)pattern')`

flag 可选值有：

`re.I(re.IGNORECASE)`: 忽略大小写（括号内是完整写法，下同）

`re.M(MULTILINE)`: 多行模式，改变`'^'`和`'$'`的行为（参见上图）

`re.S(DOTALL)`: 点任意匹配模式，改变`'.'`的行为

`re.L(LOCALE)`: 使预定字符类 `\w \W \b \B \s \S` 取决于当前区域设定

`re.U(UNICODE)`: 使预定字符类 `\w \W \b \B \s \S \d \D` 取决于unicode定义的字符属性

`re.X(VERBOSE)`: 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。

以下两个正则表达式是等价的：
```
regex_1 = re.compile(r"""\d +  # 数字部分
                         \.    # 小数点部分
                         \d *  # 小数的数字部分""", re.X)
regex_2 = re.compile(r"\d+\.\d*")
```


**Match**
Match 对象是一次匹配的结果，包含了很多关于此次匹配的信息，可以使用Match提供的可读属性或方法来获取这些信息。

`match` 属性：

`string`: 匹配时使用的文本。

`re`: 匹配时使用的Pattern对象。

`pos`: 文本中正则表达式开始搜索的索引。值与`Pattern.match()`和`Pattern.seach()`方法的同名参数相同。

`endpos`: 文本中正则表达式结束搜索的索引。值与`Pattern.match()`和`Pattern.seach()`方法的同名参数相同。

`lastindex`: 最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None。

`lastgroup`: 最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。

方法：
`group([group1, …])`: 
获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。group1可以使用编号也可以使用别名；编号0代表整个匹配的子串；不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。

`groups([default])`: 
以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None。

`groupdict([default])`: 
返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内。default含义同上。

`start([group])`: 
返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。

`end([group])`: 
返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。

`span([group])`: 
返回(start(group), end(group))。

`expand(template)`: 
将匹配到的分组代入template中然后返回。template中可以使用\id或\g、\g引用分组，但不能使用编号0。
\id与\g是等价的；但\10将被认为是第10个分组，如果你想表达\1之后是字符'0'，只能使用\g<1>0。


**Pattern**
Pattern对象是一个编译好的正则表达式，通过Pattern提供的一系列方法可以对文本进行匹配查找。
Pattern不能直接实例化，必须使用 `re.compile()` 进行构造。

Pattern提供了几个可读属性用于获取表达式的相关信息：
`pattern`: 编译时用的表达式字符串。
`flags`: 编译时用的匹配模式。数字形式。
`groups`: 表达式中分组的数量。
`groupindex`: 以表达式中有别名的组的别名为键、以该组对应的编号为值的字典，没有别名的组不包含在内。

