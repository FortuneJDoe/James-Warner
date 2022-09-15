import numpy as np
import random


def localminarrgen(max_len, max_val):
    """存在局部最小值的非负数组生成器"""

    l = random.randint(0, max_len)
    a = np.zeros(l, dtype=int)
    for i in range(l):
        a[i] = random.randint(0, max_val)  # 生成非负数组
    if len(a) > 2:
        a[0] = max_val + 1
        a[-1] = max_val + 1
    print(f"生成数组：{a}")
    return a


def findonelocalminindex(arr_input):
    """
    寻找局部最小值
    :param arr_input:输入数组
    :return:返回一个局部最小值的索引，没有则返回-1
    """

    local_min = -1
    if len(arr_input) == 0:
        return local_min
    elif len(arr_input) == 1:
        return 0
    # elif len(arr_input) == 2:
    #     return 0 if arr_input[0] <= arr_input[1] else 1
    else:
        lf = 0
        rt = len(arr_input) - 1
        while lf < rt - 1:
            local_min = lf + ((rt - lf) >> 1)
            if arr_input[local_min - 1] <= arr_input[local_min]:
                rt = local_min
            elif arr_input[local_min] >= arr_input[local_min + 1]:
                lf = local_min
            else:
                return local_min
        return lf if arr_input[lf] <= arr_input[rt] else rt


def check(arr_in, ind):
    if len(arr_in) == 0:
        return False
    elif len(arr_in) == 1:
        return True
    else:
        if ind == 0:
            return True if arr_in[0] <= arr_in[1] else False
        elif ind == len(arr_in) - 1:
            return True if arr_in[ind - 1] >= arr_in[ind] else False
        else:
            return True if (arr_in[ind - 1] >= arr_in[ind] and arr_in[ind] <= arr_in[ind + 1]) else False


if __name__ == '__main__':
    count = 0
    correct = 0
    times = 100
    for v in range(times):
        print(f"第{v + 1}次尝试：")
        test_arr = localminarrgen(30, 100)
        result_index = findonelocalminindex(test_arr)
        check_res = check(test_arr, result_index)
        if check_res:
            correct += 1
            print(f"找到索引{result_index}的元素{test_arr[result_index]}为局部最小值，验证结果为{check_res}。\n")
        else:
            print(f"数组为空，跳过。\n")
            count += 1
    print(f"验证正确率：{correct / (times - count) * 100}%")

