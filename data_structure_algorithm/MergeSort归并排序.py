import random


def gen_int_list(mx_no_elems=100, start=-1000, end=1000):
    mx_num = random.randint(0, mx_no_elems)
    test_list = []
    for i in range(mx_num):
        test_list.append(random.randint(start, end))
    return test_list


class MergeSort:

    def __init__(self):
        pass

    def merge(self, arr, left, middle, right):
        """
        合并2个有序区间成为1个有序区间
        :param arr: 需要归并排序的数组
        :param left: 第1个有序区间的左边界
        :param middle: 第1个有序区间的右边界
        :param right: 第2个有序区间的左边界
        """

        help_arr = list()  # 辅助数组，用于存放合并后的有序数组
        pos_01, pos_02 = left, middle + 1  # 定义指针分别指向需要合并的2个有序区间各自的左边界
        # 如果两个指针均不越界(各自右边界)，那么继续比较，谁小复制谁到help_arr，指针右移一位
        while pos_01 <= middle and pos_02 <= right:

            if arr[pos_01] <= arr[pos_02]:
                help_arr.append(arr[pos_01])
                pos_01 += 1
            else:
                help_arr.append(arr[pos_02])
                pos_02 += 1

        # 如果某个指针越界，则跳转至此继续
        # 如果第1个区间左指针没有越界，则将其剩余元素直接复制到help_arr末尾
        if pos_01 <= middle:
            help_arr.extend(arr[pos_01: middle + 1])
        # 如果第2个区间左指针没有越界，则将其剩余元素直接复制到help_arr末尾
        if pos_02 <= right:
            help_arr.extend(arr[pos_02: right + 1])

        # 将原数组对应区间用help_arr刷新一下
        i = 0
        while i < len(help_arr):
            arr[left + i] = help_arr[i]
            i += 1

    def merge_sort_recursion(self, arr):
        """
        归并排序的递归版本
        :param arr: 需要归并排序的数组
        """

        # 如果列表为空或者单元素列表，则直接返回
        if not arr or len(arr) == 1:
            return arr
        else:
            lf, arr_len = 0, len(arr)

            def recrusion(arr, left, right):
                """
                递归函数，将主任吴分解为子任务调用自身
                :param arr: 需要归并排序的数组
                :param left: 左边界
                :param right: 右边界
                """

                # 如果左右边界相等，区间内只有一个元素，自然有序，直接返回该元素
                if left == right:
                    return arr
                # 如果左右边界不相等，则需要拆分成子任务
                else:
                    mid = left + ((right - left) >> 1)  # 计算中点作为分割区间的点
                    recrusion(arr, left, mid)  # 子任务，归并排序arr[left:mid]
                    recrusion(arr, mid + 1, right)  # 子任务，归并排序arr[mid+1:right]
                    self.merge(arr, left, mid, right)  # 合并2个有序区间成为1个有序区间

            recrusion(arr, lf, arr_len - 1)  # 调用递归函数

    def merge_sort_arr(self, arr):
        """
        归并排序的非递归版本
        :param arr: 需要归并排序的数组
        """

        if not arr or len(arr) == 1:
            return arr
        else:
            n = len(arr)
            merge_size = 1
            while merge_size < n:
                lf = 0
                while lf < n:
                    mid = lf + merge_size - 1  # 找到中点
                    if mid >= n:
                        break  # 中点超越arr右边界，说明当前lf:m区间都是左组，必然有序，跳过
                    rt = min(mid + merge_size, n - 1)  # 右组右边界
                    self.merge(arr, lf, mid, rt)
                    lf = rt + 1  # 下一个循环左组的左边界
                if merge_size > (n >> 1):
                    break  # 防止n趋近于系统最大值时，merge_size溢出(python3 中貌似已经不存在这个问题)
                merge_size <<= 1


if __name__ == "__main__":

    mergesort = MergeSort()
    # 对数器
    for j in range(1000):
        res01 = gen_int_list(start=-100, end=300000)
        mergesort.merge_sort_recursion(res01)  # 归并排序
        ans01 = sorted(res01)  # 返回系统(绝对正确算法)的结果
        if ans01 != res01:
            print(f"WRONG!:{j}\nans1={ans01},\nbut res1={res01}")
            print("Wrong with recursion!")
            break
        res02 = gen_int_list(start=-100, end=3000)
        mergesort.merge_sort_arr(res02)
        ans02 = sorted(res02)
        if ans02 != res02:
            print(f"WRONG!:{j}\nans2={ans02},\nbut res2={res02}")
            print("Wrong with non-recursion!")
            break
