# -*- coding: utf-8 -*-

import json

if __name__ == "__main__":
    # 使用JSON
    params = {
        "symbol": "123456",
        "type": "limit",
        "price": 123.4,
        "amount": 23
    }
    params_str = json.dumps(params)
    print("序列化以后")
    print("类型{},值{}".format(type(params_str), params_str))

    original_params = json.loads(params_str)
    print("在去序列化之后")
    print("类型{},值{}".format(type(original_params), original_params))
