in_str = input("Please input a the string \"Python\": ")
new_str = in_str[2:]
out_str = ""
for char in new_str:
    out_str = char + out_str
print(out_str)

x = input("Please input any number for x: ")
y = input("Please input any number for y: ")

print(x + " + " + y + " = " + str(int(x)+int(y)))
print(x + " - " + y + " = " + str(int(x)-int(y)))
print(x + " * " + y + " = " + str(int(x)*int(y)))
print(x + " / " + y + " = " + str(int(x)/int(y)))
print(x + " ^ " + y + " = " + str(int(x)**int(y)))

