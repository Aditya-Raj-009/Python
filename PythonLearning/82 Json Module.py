# Json- Python has inbuilt package called json , which is use to work with json (javascript object notation) data.

import json

# loads():  use to convert json to python.
data = '{"var1": "Harry","var2": "Prince"}'  # a type of json data.
print(data)
# print(data["var2"]) # show error.
parsed = json.loads(data)  # json to python.
print(parsed)  # this make data as dictinary.
print(parsed['var2'])  # we can do this.

# dumps(): use to convert python to json.
# data2 is a dictionary of python type:
data2 = {
    "zebra": "Black",
    "yak": "animal",
    "channer name": "COdeWithHarry",
    "cars": ["BMW", "Ferrari", "Audi"],
    "Fridge": ("Roti", 565),
    "jbad": False
}
parsed2 = json.dumps(data2)  # convert to json
print(
    parsed2)  # {"channer name": "COdeWithHarry", "cars": ["BMW", "Ferrari", "Audi"], "Fridge": ["Roti", 565], "jbad": false}

# dumps() method has parameter to order the keys in the result:
# sort_keys parameter to specify if the result should be sorted or not:
parsed3 = json.dumps(data2, separators=(":", "="), indent=4, sort_keys=True)  # indent use to keep space,readable.
print(parsed3)
