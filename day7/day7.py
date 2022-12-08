ans1 = 0
ans2 = float("inf")
class Node():
    def __init__(self, fileName, children=[], isDirectory=True, parent=None, fileSize=0, total=0):
        self.fileName = fileName
        self.children = children
        self.isDirectory = isDirectory
        self.parent = parent
        self.fileSize = int(fileSize)
        self.total = total

head = None
with open("input.txt") as f:
    curr = Node("/",[], True, None, 0)
    head = curr
    for line in f:
        line=line.strip()
        if line.startswith("$ cd .."):
            curr=curr.parent
        elif line.startswith("$ cd"):
            _, _, dirName = line.split(" ")
            if dirName == '/': 
                continue
            for node in curr.children:
                if node.fileName == dirName and node.isDirectory:
                    curr = node
                    break
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            _, dirName = line.split(" ")
            curr.children.append(Node(dirName, [], True, curr, 0))
        else:
            fileSize, fileName = line.split(" ")
            curr.children.append(Node(fileName, [], False, curr, fileSize))

def bfs(node):
    print(node.fileName)
    for n in node.children:
        print('-', n.fileName)
    for n in node.children:
        bfs(n)
def dfs(node, isans2=False):
    global ans1, ans2, total
    size = node.fileSize
    for n in node.children:
        size += dfs(n, isans2)
    if node.isDirectory and size <= 100000:
        ans1 += size
    if isans2 and node.isDirectory and (30000000 - (70000000 - head.total)) <= size:
        ans2 = min(ans2, size)
    if size > 10000000:
        node.total = size
    return size
#bfs(head)
total = dfs(head)
print('total', total)
dfs(head, isans2=True)
print(ans1)
print(ans2)
