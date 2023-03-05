# dict  erstellen
info = {
    "name":"ziad",
    "age":27,
    "country":"german"
}
print(info.keys())                       # dict_keys(['name', 'age', 'country'])
print(info.values())                     # dict_values(['ziad', 27, 'german']) just the dict_values
print(info.get("age"))                   # 27 ,when the key not found than using .get(key,"message") to user
thisdict = dict(x=[2, 3, 4], y=[2, 3, 4], z=[2, 3, 4])
print(thisdict)