# -*- coding: utf-8 -*-
"""
Created on Sat May  2 12:14:55 2026

@author: 95451
"""
import math
#计算器函数
def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    
print(calculate(2,3))
print(calculate(2,3,'multiply'))

def grade(score):
    if score >90:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C' 
    elif 60 <= score <= 69:
        return 'D'    
    else:
        return 'F'
    
print(grade(93))

def stats(number):
    total = sum(number)
    avg = sum(number)/len(number)
    count = len(number)
    return total,avg,count

total, avg, count = stats([10, 20, 30, 40])
print(f"总和：{total}，平均值：{avg}，个数：{count}")

def average(*args):
    means = sum(args)/len(args)
    return means
print(average(10, 20))
print(average(1, 2, 3, 4, 5))

def build_card(name, **kwargs):
    kwargs['name'] = name
    return kwargs 
card = build_card("小明", age=20, city="北京", job="学生")
print(card)
def smart_print(*args, **kwargs):
    # 第一部分：打印位置参数
    for i, value in enumerate(args,1):
        print(f"[{i}] {value}")

    for key, value in kwargs.items():
        print(f"{key} → {value}")
smart_print("苹果", "香蕉", "橘子", price=5, color="红色")
scores = [45, 78, 92, 33, 67, 85, 59, 71]
s1 = [i for i in scores if i>=60]
s2 = [i+5 for i in scores if i>=60] 
print(s1)
print(s2)

def count_words(words):
    result = {}                     # 空字典
    for word in words:
        if word not in result:      # 判断是否在字典里
            result[word] = 1 
        else:
            result[word] += 1   
    return result

result = count_words(["apple", "banana", "apple", "cherry", "banana", "apple"])
print(result)    
          
def distance(p1, p2):
    d = math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    return d
print(distance((0, 0), (3, 4)))   # 5.0
print(distance((1, 2), (4, 6)))
     
def common_friends(person1, person2):
    set1=set(person1)
    set2=set(person2)
    common = set1 & set2
    only_a = set1 - set2
    only_b = set2 - set1
    return common, only_a, only_b

a = ["小红", "小刚", "小华", "小李"]
b = ["小刚", "小华", "小张", "小王"]

common, only_a, only_b = common_friends(a, b)
print(f"共同好友：{common}")     # {'小刚', '小华'}
print(f"A独有：{only_a}")        # {'小红', '小李'}
print(f"B独有：{only_b}")        # {'小张', '小王'}
     
     
     
     
     
    
    
     
     
     
     
     
     