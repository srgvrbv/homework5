immutable_var = 0,1,2,3,4,5,True,"string"
print(immutable_var)# 3.кортеж не поддерживает обращение по элементам
mutable_list = [0,1,6,7,8,"modified",True]
print(mutable_list)
mutable_list[2] = "apple"
mutable_list.append("lime")
mutable_list.extend(["string",False])
mutable_list.remove(7)
print(mutable_list)