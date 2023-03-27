[toc]

# 比较器与堆

## 堆结构
&emsp;&emsp;逻辑上是一个完全二叉树结构
### 完全二叉树
#### 概念与图表示
&emsp;&emsp;一棵深度为k的有n个结点的二叉树，对树中的结点按从上至下、从左到右的顺序进行编号，如果编号为i（1≤i≤n）的结点与满二叉树中编号为i的结点在二叉树中的位置相同，则这棵二叉树称为完全二叉树。
&emsp;&emsp;翻译翻译就是：完全二叉树要么是满二叉树，要么最后一层不满但是最后一层在从左到右长满的状态中。

![image](https://img2023.cnblogs.com/blog/2745075/202303/2745075-20230327204319820-676641961.png)


#### 数组表示

![image](https://img2023.cnblogs.com/blog/2745075/202303/2745075-20230327204340305-165760417.png)


&emsp;&emsp;规律：
- $ i $的左孩子节点为$ 2i+1 $
- $ i $的右孩子节点为$ 2i+2 $
- $ i $的父节点为$ \frac{i-1}{2} $

>&emsp;&emsp;思考，如果完全二叉树的首个节点序号为1，那么上述规律中公式如何改写？

### 大根堆
&emsp;&emsp;每一棵子树的最大值都是它头结点的元素

![](./images/1679904266784_image.png)

### 小根堆
&emsp;&emsp;每一棵子树的最小值都是它头结点的元素

![](./images/1679904580856_image.png)

### 堆的代码实现
#### 问题1：用户依次给出数字，要求返回大(小)根堆
&emsp;&emsp;你有一个空数组，此时heap_size = 0。用户依次给你数字：3,2,4,1,3,5,0，请你实现大根堆。
&emsp;&emsp;实现步骤：
1. 接收1个元素，放入数组最后位置，heap_size += 1;
2. 将该元素与其父节点元素比较，如果不大于父节点则不做任何动作；否则与父节点交换，并继续与新的父节点作比较。

```python
import random


def swap(arr, ind_01, ind_02):
    """交换数组中2个元素的位置"""
    arr[ind_01], arr[ind_02] = arr[ind_02], arr[ind_01]


def heap_insert(heap, index):
    """将现有数组组织成大根堆"""
    while index != 0 and heap[index] > heap[int((index - 1) / 2)]:
        swap(heap, index, int((index - 1) / 2))
        index = int((index - 1) / 2)


class MaxHeap:

    def __init__(self, limit: int):
        """实例化一个大根堆时，需指定大根堆的大小上限"""
        self.limit = limit if limit > 0 else 1
        self.heap_size = 0
        self.heap = [0] * limit

    def is_empty(self):
        return self.heap_size == 0

    def is_full(self):
        return self.heap_size == self.limit

    def push(self, val: int):
        """向大根堆中插入元素"""
        if self.is_full():
            print("Heap is full !!!")
        else:
            self.heap[self.heap_size] = val
            heap_insert(self.heap, self.heap_size)
            self.heap_size += 1

    def get_heap(self):
        """返回数组中堆的部分"""
        return self.heap[:self.heap_size]


def gen_test_arr(size=10, min_num=0, max_num=100):
    """随机数组生成器"""
    t_arr = list()
    cnt = 0
    while cnt < size:
        t_arr.append(random.randint(min_num, max_num))
        cnt += 1
    return t_arr


if __name__ == "__main__":
    test_arr = gen_test_arr()
    my_heap = MaxHeap(len(test_arr))
    print(my_heap.heap)
    for i in test_arr:
        my_heap.push(i)
    print(my_heap.get_heap())

```
&emsp;&emsp;不难看出，当用户给我们第i个数字时，我们组织大根堆的时间复杂度为$ O(logN) $, 小根堆的代码与复杂度同理。

#### 用户在过程中弹出元素场景
&emsp;&emsp;用户在过程中需要返回此时堆中最大(小)值，并删除这个元素，且要求剩下元素继续保持大(小)根堆的组织形式

```python
--snip--

def heapify(arr, index, hesp_size):
    """从index位置往下看，如果有孩子节点且孩子节点更大，与最大的孩子节点交换"""
    left = index * 2 + 1
    while left < hesp_size:
        # 左右两个孩子(如果有)中，获取最大的孩子的下标
        largest = left + 1 if left + 1 < hesp_size and arr[left + 1] > arr[left] else left
        # 最大孩子与父相比，获取最大值的下标
        largest = largest if arr[largest] > arr[index] else index
        if largest == index:
            break
        swap(arr, largest, index)
        index = largest
        left = index * 2 + 1

class MaxHeap:
    --snip--

    def pop(self):
        """返回当前堆的最大值并删除，剩余元素仍组织为大根堆"""
        ans = self.heap[0]
        self.heap_size -= 1
        swap(self.heap, 0, self.heap_size)
        heapify(self.heap, 0, self.heap_size)

        return ans

    def get_heap(self):
        --snip


if __name__ == "__main__":
    test_arr = gen_test_arr()
    my_heap = MaxHeap(len(test_arr))
    print(f"初始化:{my_heap.heap}")
    for i in test_arr:
        my_heap.push(i)
    print(f"完成大根堆:{my_heap.get_heap()}")
    m = my_heap.pop()
    print(f"max_val:{m}")
    print(f"变更后的大根堆:{my_heap.get_heap()}")

```
&emsp;&emsp;不难看出，这个过程的间复杂度也是$ O(logN) $

## 堆排序
&emsp;&emsp;首先将需排序的数组组织成大根堆，然后反复将堆堆头尾元素互换，将heap_size - 1后的数组再组成大根堆直至heap_size = 0。
```python
def swap(arr, ind_01, ind_02):
    """交换数组中2个元素的位置"""
    arr[ind_01], arr[ind_02] = arr[ind_02], arr[ind_01]


def heap_insert(heap, index):
    """将现有数组组织成大根堆"""
    while index != 0 and heap[index] > heap[int((index - 1) / 2)]:
        swap(heap, index, int((index - 1) / 2))
        index = int((index - 1) / 2)


def heapify(arr, index, hesp_size):
    """从index位置往下看，如果有孩子节点且孩子节点更大，与最大的孩子节点交换"""
    left = index * 2 + 1
    while left < hesp_size:
        # 左右两个孩子(如果有)中，获取最大的孩子的下标
        largest = left + 1 if left + 1 < hesp_size and arr[left + 1] > arr[left] else left
        # 最大孩子与父相比，获取最大值的下标
        largest = largest if arr[largest] > arr[index] else index
        if largest == index:
            break
        swap(arr, largest, index)
        index = largest
        left = index * 2 + 1


class HeapSort:

    def __init__(self):
        pass

    # 排序额外空间复杂度O(1)
    def heap_sort(self, arr):
        if not arr or len(arr) < 2:
            return
        # O(logN)
        for i in range(len(arr)):  # O(N)
            heap_insert(arr, i)  # O(logN)
        heap_size = len(arr)
        heap_size -= 1
        swap(arr, 0, heap_size)
        # O(N*logN)
        while heap_size > 0:  # O(N)
            heapify(arr, 0, heap_size)  # O(logN)
            heap_size -= 1
            swap(arr, 0, heap_size)  # O(1)

    def heap_sort_better(self, arr):
        """时间复杂度O(N) + O(NlogN)"""
        if not arr or len(arr) < 2:
            return
        # O(N)
        n = len(arr) - 1
        while n >= 0:
            heapify(arr, n, len(arr))
            n -= 1
        heap_size = len(arr)
        heap_size -= 1
        swap(arr, 0, heap_size)
        # O(N*logN)
        while heap_size > 0:  # O(N)
            heapify(arr, 0, heap_size)  # O(logN)
            heap_size -= 1
            swap(arr, 0, heap_size)  # O(1)

```
