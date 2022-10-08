class Node(object):
    """二叉树节点"""

    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class LevelTravelBinaryTree(object):
    """二叉树按层打印及寻找最大宽度"""

    def __init__(self, node=None):
        self.head = node

    def level_traversal(self, start: Node):
        """按层打印"""

        print('level-order:')
        if start:
            queue = list()  # 准备一个空队列
            queue.append(start)  # 初始节点从尾部压入队列
            while queue:  # 队列不为空
                current = queue.pop(0)  # 从头部弹出节点，且current指向该节点
                print(current.val, end=' ')  # 打印被弹出节点的元素值
                if current.left:  # 被弹出节点左子节点不为空
                    queue.append(current.left)  # 左子节点从尾部压入队列
                if current.right:  # 被弹出节点右子节点不为空
                    queue.append(current.right)  # 右子节点从尾部压入队列
        else:
            print('Start is None !')
        print('\n')

    def maxWithUseMap(self):
        """使用hash map返回二叉树的最大宽度"""

        start = self.head  # start指针默认从头结点开始
        if start:
            queue = list()
            queue.append(start)  # 头节点从尾部压入队列
            level_map = dict()  # 哈希表，其键值对含义为：key(所代表的节点)在(二叉树的第)value层
            level_map[start] = 1  # 头结点(key=self.head)在第1(value=1)层
            cur_level = 1  # 当前你正在统计序号为cur_level层的宽度
            cur_level_nodes = 0  # 当前你正在统计的层的宽度是cur_level_nodes。初始值为0，约定当节点弹出时再计数。
            max_nodes = 0  # 记录最大宽度，最后返回这个max_nodes
            while queue:  # 队列不为空
                cur = queue.pop(0)  # 弹出队列头部元素，作为当前节点
                cur_node_level = level_map[cur]  # 读取当前节点所在层
                # 1. 宽度优先遍历部分。 在节点压入队列时，用hash去记录节点所在层
                if cur.left:  # 当前层左子树不为空
                    level_map[cur.left] = cur_node_level + 1  # 哈希表记录左子节点层数 = 当前层 + 1
                    queue.append(cur.left)  # 左子节点从尾部压入队列
                if cur.right:  # 当前层右子树不为空
                    level_map[cur.right] = cur_node_level + 1  # 哈希表记录右子节点层数 = 当前层 + 1
                    queue.append(cur.right)  # 右子节点从尾部压入队列

                # 2. 统计结算部分。根据弹出节点与当前层关系来判断需要进行：1)累计节点数，2)结算当前层的节点数
                if cur_node_level == cur_level:  # 所弹出节点的所在层序号 == 正在统计的层序号
                    cur_level_nodes += 1  # 当前层宽度计数 + 1
                else:  # 所弹出节点所在层序号 != 正在统计层序号(意味着所弹出节点所在层是下一层，此时其上一层的节点数要结算)
                    max_nodes = max(max_nodes, cur_level_nodes)  # 更新max_nodes
                    cur_level += 1  # 当前层更新为下一层，所以+1
                    cur_level_nodes = 1  # 当前层节点数直接设置为1(因为已经弹出1个节点)
            # 最后一层没有下一层，再循环中不会触发max_nodes结算，需单独结算
            max_nodes = max(max_nodes, cur_level_nodes)
            return max_nodes

    def maxWithoutMap(self):
        """
        不使用hash map返回二叉树的最大宽度
        (不关心节点在哪一层，只需要在统计过程中知道层结算的时刻)
        """

        start = self.head  # start指针默认从头结点开始
        if start:
            queue = list()
            queue.append(start)
            cur_end = start  # 当前层最右的结点是谁
            next_end = None  # 如果下一层不为空，那么下一层最右节点是谁
            max_nodes = 0  # 记录最大宽度
            curlevel_nodes = 0  # 当前层目前节点个数，在节点弹出时统计
            while queue:
                cur = queue.pop(0)  # 弹出队列头部节点
                # 宽度优先遍历。队列尾部压入节点同时更新下一层最右节点next_end
                if cur.left:
                    queue.append(cur.left)
                    next_end = cur.left
                if cur.right:
                    queue.append(cur.right)
                    next_end = cur.right
                curlevel_nodes += 1  # 弹出节点，因此当前层节点数 + 1
                # 结算。如果弹出节点是当前层最右节点(说明来到了当前层统计结算时刻)
                if cur == cur_end:
                    max_nodes = max(max_nodes, curlevel_nodes)  # 更新max_nodes
                    curlevel_nodes = 0  # 重置当前层节点数
                    cur_end = next_end  # 下一层最右节点“荣升”为当前层最右节点
            return max_nodes


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n5.left = n8
    n6.right = n9

    my_bt = LevelTravelBinaryTree(n1)
    my_bt.level_traversal(my_bt.head)
    m_nodes_01 = my_bt.maxWithUseMap()
    m_nodes_02 = my_bt.maxWithoutMap()
