import yaml
customer = [
    { "name": "InSeong", "age": "24", "gender": "man" },
    { "name": "Akatsuki", "age": "22", "gender": "woman" },
    { "name": "Harin", "age": "23", "gender": "man" },
    { "name": "Yuu", "age": "31", "gender": "woman" }
]

yaml_str = yaml.dump(customer)
data = yaml.load(yaml_str,Loader=yaml.FullLoader)
print(type(yaml_str))
print(yaml_str)
print(type(data))
print(data)