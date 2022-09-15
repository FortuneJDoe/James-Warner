import numpy as np
import random

def localminarrgen(max_len, max_val):
    """存在局部最小值的非负数组生成器"""

    l = random.randint(0, max_len)
    a = np.zeros(l, dtype=int)
    for i in range(l):
        a[i] = random.randint(0, max_val)  # 生成非负数组
    if len(a) > 2:  # 长度大于2的数组将头尾元素变更为max_val + 1，确保局部最小值不在端点
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
    if len(arr_input) == 0:  # 数组为空则返回-1
        return local_min
    elif len(arr_input) == 1:  # 单元素数组返回该元素索引
        return 0
    # elif len(arr_input) == 2:
    #     return 0 if arr_input[0] <= arr_input[1] else 1
    else:
        lf = 0
        rt = len(arr_input) - 1
        while lf < rt - 1:
            local_min = lf + ((rt - lf) >> 1)  # 计算中点
            if arr_input[local_min - 1] <= arr_input[local_min]:
                rt = local_min
            elif arr_input[local_min] >= arr_input[local_min + 1]:
                lf = local_min
            else:
                return local_min
        return lf if arr_input[lf] <= arr_input[rt] else rt  # 如果最后范围内剩下2个元素的比较


def check(arr_in, ind):
    """对数器"""

    if len(arr_in) == 0:  # 空数组，不必检查，返回False，寻找局部极小值无意义
        return False
    elif len(arr_in) == 1:  # 单元素数组，可认为该元素即为所求
        return True
    else:
        if ind == 0:  # 如果输入局部最小值索引在0位置，只有后面有元素
            return True if arr_in[0] <= arr_in[1] else False
        elif ind == len(arr_in) - 1:  # 如果输入局部最小值索引在最后位置，只有前面有元素
            return True if arr_in[ind - 1] >= arr_in[ind] else False
        else:  # 如果在中间，则前后都有元素，比较确认是否为局部极小值
            return True if (arr_in[ind - 1] >= arr_in[ind] and arr_in[ind] <= arr_in[ind + 1]) else False

# (可选)自己检测实例代码
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

