import yaml

with open("./data2.yml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
    print("返回的字典数据：", data)
    # print("返回的数据类型：", type(data.get("int_value")))
    # print("返回的数据类型：", type(data.get("float_value")))
