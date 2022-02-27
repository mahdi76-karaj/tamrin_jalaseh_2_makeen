"""
تبدیل فارنھایت بھ سلسیوس
برنامھ ای بنویسید کھ از کاربر ورودی بھ عنوان  Fیا  Cبگیرد و یک عدد دیگر بھ عنوان مقدار آن از کاربر بگیرد و تبدیل متناسب
را انجام دھد
"""

f = int(input("Enter the temperature as Fahrenheit : "))

c = f * (9/5) + 32

print("The temperature is ",c ,"degrees Celsius ")
