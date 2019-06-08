# 이진 탐색 트리(binary search tree)는 모든 노드에 대해 그 왼쪽 노드들의 값이 현재 노드 값보다 작거나 같음
# 우측은 현재 노드의 값보다 큼


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        print("Node call")

##TODO
print("TODO 코드 작성")