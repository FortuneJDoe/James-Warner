```python3
"""
注意函数传参时机、代码执行顺序(尤其是return语句何时执行)、语句执行内容和语句执行的效果
"""


def set_fun1(func):
    print("set_fun1 has been defined.")  # 打印用于验证在多个装饰器的情况下，多个装饰器之间的执行顺序

    def call_fun1(*args, **kwargs):
        print("call_fun1 has been executed")  # 当被装饰函数执行时，会打印
        return func()

    return call_fun1


def set_fun2(func):
    print("set_fun2 has been defined.")

    def call_fun2(*args, **kwargs):
        print("call_fun2 has been executed")
        return func()

    return call_fun2


# 装饰函数
@set_fun2
@set_fun1
def test():
    print("======Congratulations======")


if __name__ == "__main__":
    test()
```

>Out:
><br>set_fun1 has been defined.
><br>set_fun2 has been defined.
><br>call_fun2 has been executed
><br>call_fun1 has been executed
><br>======Congratulations======
