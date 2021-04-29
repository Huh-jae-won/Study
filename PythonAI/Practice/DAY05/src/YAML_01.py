import yaml
yaml_str = """ 
Date: 2017-03-10 
PriceList: 
    -
        item_id: 1000 
        name: Banana 
        color: yellow 
        price: 800 
    -
        item_id: 1001 
        name: Orange 
        color: orange 
        price: 1400 
"""
data = yaml.load(yaml_str, Loader=yaml.FullLoader) # 파이썬객체로 변환

for item in data['PriceList']:
    print(item["name"],":",item["price"])
