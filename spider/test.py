key_value = {}

# 初始化
key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323

print("按值(value)排序:")
mylist = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
print(mylist)
print(mylist[0])
print(mylist[0][0])