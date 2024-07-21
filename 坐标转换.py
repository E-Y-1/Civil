import os
import re

file=open("F:\\node.txt","r")    #以只读方式打开文件
text=file.read()                 #读取文件内容
##########
start_string="*Node"             #查找内容区间起始字符串
end_string="*Element"            #查找内容区间终止字符串

start_index=text.find(start_string)        #查找内容区间起始字符串位置
end_index=text.find(end_string)            #查找内容区间终止字符串

result=[]

while start_index!=-1 and end_index!=-1:
    content=text[start_index+len(start_string):end_index].strip()
    result.append(content)

    start_index=text.find(start_string,end_index+len(end_string))
    end_index=text.find(end_string,start_index)

#print(result)                  #以字符串形式输出查找内容
#############
string=result[0]                #将查找的内容从列表中提取出来以备后续处理
pattern=r"\n"                   #定义分割字符

segments=re.split(pattern,string)        #将字符串切片
lis=[]
for i in segments:                       #遍历切片后生成的若干子字符串
    lis_1=[]
    segment=re.findall(r"-?\d+",i)         #从子字符串中索引所需内容
    for j in segment:
        j=j.replace(" ","")                 #删除索引对象的空格
        lis_1.append(int(j))                #将处理后的对象放入列表
        
    lis.append(lis_1)
#print(lis)
###################
import math

sita=float(input("请输入主梁的斜交角（角度,以y轴右侧为正、左侧为负）："))
direction_cross=input("请输入主梁横桥向所在坐标轴（x or y or z）：")
direction_straight=input("请输入主梁顺桥向所在坐标轴（x or y or z）：")

if direction_cross=="x":
    col_c=1
elif direction_cross=="y":
    col_c=2
elif direction_cross=="z":
    col_c=3
else:
    print("输入的坐标轴有误！")

if direction_straight=="x":
    col_s=1
elif direction_straight=="y":
    col_s=2
elif direction_straight=="z":
    col_s=3
else:
    print("输入的坐标轴有误！")

for i in range(0,len(lis)):
    lis[i][col_s]=lis[i][col_s]+lis[i][col_c]*math.tan(math.radians(sita))
print(lis)

import matplotlib.pyplot as plt

plt_x,plt_y=[],[]
for i in range(len(lis)):
    plt_x.append(lis[i][col_s])
    plt_y.append(lis[i][col_c])

plt.scatter(plt_x,plt_y)
plt.show()






