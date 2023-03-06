import sys
import my_module, fake_path.my_path.fake_module

print("this is my main code!!")
print("What if I want to use other functionality here?")
# want to call "my_function" into this application

a = "George"
my_module.my_function()
print(a)  # current namespace
print(my_module.a)  # the namespace of module: my_module
print(f"the list inside the module is {my_module.c}")
my_module.a = "Christina"
print(my_module.a)

print(my_module.module_directory.third_module.my_dictionary)  # very good point

print(f"Python looks for module inside these directories: {sys.path}")
# sys.path.append("fake_path/my_path")

print(fake_path.my_path.fake_module.fake_name)


