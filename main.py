# main.py

# ✅ ১. ভ্যারিয়েবল ও ডাটা টাইপ:
name = "Mahmudul Hasan Fahim"
age = 24
is_student = True

print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of is_student:", type(is_student))

print("\n--- Arithmetic Operations ---")
# ✅ ২. অ্যারিথমেটিক অপারেশন:
print("Age + 5 =", age + 5)
print("Age - 2 =", age - 2)
print("Age * 2 =", age * 2)
print("Age / 2 =", age / 2)

print("\n--- Comparison Operators ---")
# ✅ ৩. কম্পারিজন অপারেটর:
print("Is age > 18?", age > 18)
print("Is age == 24?", age == 24)
print("Is age != 30?", age != 30)
print("Is age < 18?", age < 18)

print("\n--- Logical Operators ---")
# ✅ ৪. লজিক্যাল অপারেটর:
has_id_card = True
has_library_access = False

print("Can enter exam hall (has_id_card and has_library_access)?", has_id_card and has_library_access)
print("Can access campus (has_id_card or has_library_access)?", has_id_card or has_library_access)
print("Not a student?", not is_student)

print("\n--- Assignment Operators ---")
# ✅ ৫. অ্যাসাইনমেন্ট অপারেটর:
money = 1000
money += 500
print("After += 500:", money)
money -= 200
print("After -= 200:", money)
money *= 2
print("After *= 2:", money)
money /= 4
print("After /= 4:", money)

print("\n--- Identity Operators ---")
# ✅ ৬. আইডেন্টিটি অপারেটর:
x = 10
y = 10
z = 20

print("x is y?", x is y)
print("x is not z?", x is not z)

print("\n--- Membership Operators ---")
# ✅ ৭. মেম্বারশিপ অপারেটর:
fruits = ["apple", "banana", "mango"]
print("Is 'banana' in fruits?", "banana" in fruits)
print("Is 'orange' not in fruits?", "orange" not in fruits)