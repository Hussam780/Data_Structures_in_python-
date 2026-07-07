class Stack:
    def __init__(self):
        """منشئ الفئة - ينشئ ستاك فارغ"""
        self.items = []  # نستخدم قائمة لتخزين العناصر
    
    def push(self, item):
        """إضافة عنصر إلى قمة الستاك"""
        self.items.append(item)  # نضيف العنصر إلى نهاية القائمة
    
    def pop(self):
        """إزالة وإرجاع العنصر من قمة الستاك"""
        if self.is_empty():
            raise Exception("لا يمكن إجراء pop، الستاك فارغ!")  # خطأ إذا كان الستاك فارغاً
        return self.items.pop()  # نزيل آخر عنصر من القائمة
    
    def peek(self):
        """إرجاع العنصر في قمة الستاك دون إزالته"""
        if self.is_empty():
            raise Exception("لا يمكن إجراء peek، الستاك فارغ!")  # خطأ إذا كان الستاك فارغاً
        return self.items[-1]  # نعود بقيمة آخر عنصر دون حذفه
    
    def is_empty(self):
        """التحقق مما إذا كان الستاك فارغاً"""
        return len(self.items) == 0  # نعود بـ True إذا كان الطول يساوي صفر
    
    def size(self):
        """إرجاع عدد العناصر في الستاك"""
        return len(self.items)  # نعود بطول القائمة

# مثال على استخدام الفئة المخصصة
print("=== استخدام الـ Stack المخصص ===")
book_stack = Stack()

# إضافة عناصر إلى الستاك
book_stack.push("رواية 1984")
book_stack.push("قصة الحيوانات")
book_stack.push("كتاب البرمجة")

print("حجم الستاك:", book_stack.size())  # 3
print("العنصر في القمة:", book_stack.peek())  # كتاب البرمجة

# إزالة عنصر
removed_book = book_stack.pop()
print("تمت إزالة:", removed_book)  # كتاب البرمجة
print("العنصر في القمة الآن:", book_stack.peek())  # قصة الحيوانات
print("حجم الستاك بعد pop:", book_stack.size())  # 2


"""
تطبيقات عملية إضافية للـ Stack
لنرى كيف يمكن استخدام الستاك في مواقف حقيقية:
"""
# مثال 1: محاكاة زر الرجوع (Undo) في برنامج نصي
class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = Stack()  # ستاك لحفظ الحالات السابقة
    
    def write(self, new_text):
        """إضافة نص جديد وحفظ الحالة السابقة"""
        self.undo_stack.push(self.text)  # حفظ الحالة الحالية قبل التعديل
        self.text += new_text
    
    def undo(self):
        """التراجع عن آخر عملية"""
        if not self.undo_stack.is_empty():
            self.text = self.undo_stack.pop()  # استعادة الحالة السابقة

# اختبار محرر النص
editor = TextEditor()
editor.write("مرحبا")
editor.write(" بالعالم")
print("النص الحالي:", editor.text)  # مرحبا بالعالم

editor.undo()
print("بعد التراجع:", editor.text)  # مرحبا

# مثال 2: التحقق من توازن الأقواس
def check_parentheses(expression):
    """التحقق مما إذا كانت الأقواس متوازنة في التعبير"""
    stack = Stack()
    opening_brackets = "({["
    closing_brackets = ")}]"
    matching = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in opening_brackets:
            stack.push(char)  # نضيف الأقواس الافتتاحية إلى الستاك
        elif char in closing_brackets:
            if stack.is_empty() or stack.pop() != matching[char]:
                return False  # الأقواس غير متوازنة
    
    return stack.is_empty()  # يجب أن يكون الستاك فارغاً إذا كانت الأقواس متوازنة

# اختبار توازن الأقواس
print("التوازن الصحيح:", check_parentheses("(a + b) * (c - d)"))  # True
print("التوازن الخاطئ:", check_parentheses("((a + b) * (c - d)"))  # False
"""
التحقق من الستاك الفارغ
من المهم جداً التحقق من أن الستاك ليس فارغاً قبل إجراء عمليتي pop() أو peek.
"""
# المثال مع القوائم المدمجة
stack_example = []

# محاولة pop من ستاك فارغ ستسبب خطأ
# stack_example.pop()  # سيثير خطأ: IndexError: pop from empty list

# الطريقة الصحيحة: التحقق أولاً
if not stack_example:  # إذا كان الستاك فارغاً
    print("⚠️  تحذير: لا يمكن إجراء pop، الستاك فارغ!")
else:
    item = stack_example.pop()
    print("تمت إزالة:", item)
