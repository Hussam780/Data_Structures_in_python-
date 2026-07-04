# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 22:25:46 2026

@author: Amadeus
"""

# إنشاء القواميس
empty_dict = {}
student = {
    "name": "أحمد",
    "age": 20,
    "grades": [85, 90, 78],
    "courses": {
        "math": 95,
        "science": 88
    }
}

# الوصول للقيم
print(student["name"])           # أحمد
print(student.get("age"))        # 20
print(student.get("phone", "غير موجود")) # قيمة افتراضية

# الإضافة والتعديل
student["city"] = "الرياض"       # إضافة جديدة
student["age"] = 21              # تعديل موجود

# الحذف
phone = student.pop("city")      # حذف وإرجاع القيمة
del student["grades"]           # حذف مباشر

# الطرق المهمة
keys = student.keys()           # جميع المفاتيح
values = student.values()       # جميع القيم
items = student.items()         # جميع الأزواج

# التكرار على القاموس
for key, value in student.items():
    print(f"{key}: {value}")

# التحقق من الوجود
if "name" in student:
    print("المفتاح موجود")

# دمج القواميس
additional_info = {"phone": "0555555555", "email": "test@example.com"}
student.update(additional_info)

print("===================================\n")
#أيضا مثال عملي اخر :

person = {
    "name": "Hussam",
    "age": 28,
    "city": "Sana'a"
}
print(person["name"])      # Hussam

# تعديل قيمة
person["age"] = 26

# إضافة مفتاح جديد
person["job"] = "Engineer"

# حذف مفتاح
del person["city"]

print(person)
print("===================================\n")

"""
ملاحظات:
•	المفتاح يجب أن يكون فريدًا.
•	مفيد جدًا لتخزين البيانات المنظمة مثل ملفات JSON ."""

# إنشاء قاموس
car = {
    "brand": "تويوتا",
    "model": "كامري",
    "year": 2022,
    "colors": ["أبيض", "أسود", "فضي"]
}

# الوصول للقيم
print(car["brand"])            # تويوتا
print(car.get("model"))        # كامري

# التعديل والإضافة
car["year"] = 2023             # تحديث قيمة
car["price"] = 90000           # إضافة مفتاح جديد

# الحذف
del car["colors"]              # حذف مفتاح
year = car.pop("year")         # حذف وإرجاع القيمة

# التكرار على القاموس
for key, value in car.items():
    print(f"{key}: {value}")

print("-----------------------------------------------------------------------")

# إنشاء المجموعات
empty_set = set()
numbers = {1, 2, 3, 4, 5}
duplicates = {1, 2, 2, 3, 3, 4} # يصبح {1, 2, 3, 4}
# العمليات الأساسية
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# الإضافة والحذف
set1.add(6)             # إضافة عنصر
set1.remove(3)          # حذف عنصر (يسبب خطأ إذا غير موجود)
set1.discard(10)        # حذف عنصر (لا يسبب خطأ)
popped = set1.pop()     # حذف عنصر عشوائي

# عمليات المجموعات
union = set1 | set2          # الاتحاد {1,2,3,4,5,6,7,8}
intersection = set1 & set2   # التقاطع {4,5}
difference = set1 - set2     # الفرق {1,2,3}
symmetric_diff = set1 ^ set2 # الفرق المتماثل {1,2,3,6,7,8}

# العلاقات
is_subset = {1, 2}.issubset(set1)        # True
is_superset = set1.issuperset({1, 2})    # True
is_disjoint = {1, 2}.isdisjoint({7, 8})  # True

print("===================================\n")
#مثال عملي اخر :

colors = {"red", "blue", "green", "blue"}
print(colors)   # {'red', 'blue', 'green'}
# إضافة عنصر
colors.add("yellow")

# إزالة عنصر
colors.remove("red")
print("===================================\n")
"""
تمرين تطبيقي
اكتب برنامجًا يخزّن معلومات 3 طلاب (الاسم، العمر، التخصص) داخل قائمة من القواميس، ثم يطبعها بطريقة مرتبة.
"""

students = [
    {"name": "Ali", "age": 20, "major": "AI"},
    {"name": "Sara", "age": 22, "major": "CS"},
    {"name": "Omar", "age": 21, "major": "IT"}
]
for student in students:
  print(f"الاسم: {student['name']} - العمر: {student['age']} - التخصص: {student['major']}")

"""
السلاسل النصية (Strings)
 سلسلة من الأحرف
•	الخصائص:
o	مرتبة
o	غير قابلة للتعديل
o	قابلة للتكرار
o	تدعم التقطيع والفهرسة
"""

# إنشاء السلاسل
name = "أحمد"
message = 'مرحبا بالعالم'
multiline = """هذا نص
متعدد الأسطر"""

# العمليات الأساسية
text = "Python Programming"


# الفهرسة والتقطيع
print(text[0])      # P
print(text[-1])     # g
print(text[0:6])    # Python
print(text[7:])     # Programming
# الطرق المهمة
upper_text = text.upper()           # PYTHON PROGRAMMING
lower_text = text.lower()           # python programming
words = text.split()                # ['Python', 'Programming']
joined = " ".join(words)            # 'Python Programming'
replaced = text.replace("Python", "Java") # Java Programming
# الفحص
starts = text.startswith("Python")  # True
ends = text.endswith("ing")         # True
contains = "gram" in text           # True
# التنسيق
name = "محمد"
age = 25
formatted = f"الاسم: {name}, العمر: {age}" # التنسيق الحديث
old_format = "الاسم: {}, العمر: {}".format(name, age)

print("===================================\n")

