"""
判断
isspace()

如果字符串中只包含空白，则返回 True，否则返回 False.

startswith(substr, beg=0,end=len(string))

检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。

endswith(suffix, beg=0, end=len(string))

检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.

查找
find(str, beg=0 end=len(string))

检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1

rfind(str, beg=0,end=len(string))

类似于 find()函数，不过是从右边开始查找.

count(str, beg= 0,end=len(string))

返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

修改
replace(old, new [, max])

把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。

lstrip()

截掉字符串左边的空格或指定字符。

rstrip()

删除字符串字符串末尾的空格.

strip([chars])

在字符串上执行 lstrip()和 rstrip()

lower()

转换字符串中所有大写字符为小写.

upper()

转换字符串中的小写字母为大写

swapcase()

将字符串中大写转换为小写，小写转换为大写

对齐
center(width, fillchar)

返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。

zfill (width)

返回长度为 width 的字符串，原字符串右对齐，前面填充0

ljust(width[, fillchar])

返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。

"""
str01="我媳妇想打我"
str02 = "AaWdXxQs"
str01.isspace() #判断字符串 是否只包含空白 返回True 、False
print(str01.startswith("我", 0, 5)) # 判断字符串再指定区间内是否右 指定字符开头
print(str01.endswith("我",0,5))#判断字符串是否由指定字符串 结束 ,位置遵循左开右闭原则
print(str01.find("人", 0, 6)) #查找指定元素在字符串中的位置 ，如不在字符串中则返回的是 -1
print(str01.rfind("媳妇", 0, 6)) #查找指定元素在字符串中的位置，从右往左找
print(str01.count("我")) #计算元素在字符串中出现的次数
str01.lstrip() #删除左边空格，如指定元素则删除指定元素 如：str01.listrip("我")
str01.rstrip() #删除右边空格，如指定元素则删除指定元素
str01.strip() # 删除字符串前后空格，如指定元素则删除指定元素
str02.lower() #将所有大写字符转为小写
str02.upper()#将所有小写转为大写
str02.swapcase()#将所有大小写进行互换
str02.center(50,"")#返回一个指定长度的字符串，用指定元素填充 默认填充为空隔 居中
str02.zfill(60)#返回一个指定长度字符串，进行右对齐，前面填充为0 ，无法进行指定
str02.ljust(60)#返回一个指定长度的字符串，进行左对齐，默认填充为空格 ，可指定填充字符

print(str01)
Pstr_.py"""
判断
isspace()

如果字符串中只包含空白，则返回 True，否则返回 False.

startswith(substr, beg=0,end=len(string))

检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。

endswith(suffix, beg=0, end=len(string))

检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.

查找
find(str, beg=0 end=len(string))

检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1

rfind(str, beg=0,end=len(string))

类似于 find()函数，不过是从右边开始查找.

count(str, beg= 0,end=len(string))

返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

修改
replace(old, new [, max])

把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。

lstrip()

截掉字符串左边的空格或指定字符。

rstrip()

删除字符串字符串末尾的空格.

strip([chars])

在字符串上执行 lstrip()和 rstrip()

lower()

转换字符串中所有大写字符为小写.

upper()

转换字符串中的小写字母为大写

swapcase()

将字符串中大写转换为小写，小写转换为大写

对齐
center(width, fillchar)

返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。

zfill (width)

返回长度为 width 的字符串，原字符串右对齐，前面填充0

ljust(width[, fillchar])

返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。

"""
str01="我媳妇想打我"
str02 = "AaWdXxQs"
str01.isspace() #判断字符串 是否只包含空白 返回True 、False
print(str01.startswith("我", 0, 5)) # 判断字符串再指定区间内是否右 指定字符开头
print(str01.endswith("我",0,5))#判断字符串是否由指定字符串 结束 ,位置遵循左开右闭原则
print(str01.find("人", 0, 6)) #查找指定元素在字符串中的位置 ，如不在字符串中则返回的是 -1
print(str01.rfind("媳妇", 0, 6)) #查找指定元素在字符串中的位置，从右往左找
print(str01.count("我")) #计算元素在字符串中出现的次数
str01.lstrip() #删除左边空格，如指定元素则删除指定元素 如：str01.listrip("我")
str01.rstrip() #删除右边空格，如指定元素则删除指定元素
str01.strip() # 删除字符串前后空格，如指定元素则删除指定元素
str02.lower() #将所有大写字符转为小写
str02.upper()#将所有小写转为大写
str02.swapcase()#将所有大小写进行互换
str02.center(50,"")#返回一个指定长度的字符串，用指定元素填充 默认填充为空隔 居中
str02.zfill(60)#返回一个指定长度字符串，进行右对齐，前面填充为0 ，无法进行指定
str02.ljust(60)#返回一个指定长度的字符串，进行左对齐，默认填充为空格 ，可指定填充字符

print(str01)
