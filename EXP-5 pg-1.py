def merge_dict(d1,d2):
    d1.update(d2)
    return d1
dict1=eval(input("Enter first dictionary:"))
dict2=eval(input("Enter second dictionary:"))
result=merge_dict(dict1,dict2)
print("Merged Dictionary:",result)

