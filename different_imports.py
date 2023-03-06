#  what if I want to import just some things?
a = "current_namespace"
print(f"a = {a}")


from my_module import a as a_from_my_module  # a does not change!! it is stored into a_from_my_module


print(f"a = {a}, because it is the same namespace")
print(f"a = {a_from_my_module}")

a_from_my_module = "fake"
from my_module import a as a_from_my_module2  # a does not change!! it is stored into a_from_my_module

print(a_from_my_module2)
print(a_from_my_module)

try:
    import my_modules
except ModuleNotFoundError:
    print("hey, that was not a valid import!!!")
