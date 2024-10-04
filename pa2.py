# Create a class called Node:
class Node:
    def __init__(self, value=None, index=None):
        self.value = value
        self.children = []
        self.index = index

# AlphaBeta Search Function:
def alphaBeta(node, depth, alpha, beta, maximize, pruned):
    # Base Case: Checking for max depth or end of recursion and whether it's a leafNode
    if depth == 0 or not node.children:
        return node.value
        
    if maximize:
        maxVal = float('-inf')
        # Assuming 2 branches per node and consistently evaluating 
        for i, child in enumerate(node.children):
            # Each recursive call decrements depth by 1
            result = alphaBeta(child, depth - 1, alpha, beta, False, pruned)
            maxVal = max(maxVal, result)
            alpha  = max(alpha, result)

            # Pruning begins here!!
            if beta <= alpha:
                for remainingNode in node.children[i + 1:]:
                    countPrunedChildren(remainingNode, pruned)
                break
        return maxVal
    else:
        minVal = float('inf')
        # Assuming 2 branches per node and consistently evaluating
        for i, child in enumerate(node.children):
            # Each recursive call decrements depth by 1
            result = alphaBeta(child, depth - 1, alpha, beta, True, pruned)
            minVal = min(minVal, result)
            beta = min(beta, result)

            # Pruning begins here!!
            if beta <= alpha:
                for remainingNode in node.children[i + 1:]:
                    countPrunedChildren(remainingNode, pruned)
                break
        return minVal
    
# Helper Function: Remaining Pruned Children from leafNodes:
def countPrunedChildren(node, pruned):
    if not node.children:
        pruned.append(node.index)
    else:
        for child in node.children:
            countPrunedChildren(child, pruned)

# Tree Function:
def tree(values):
    # Creating bottomMost level with 12 nodes (indices 0-11)
    leafNodes = [Node(value=values[i], index=i) for i in range(12)]
    
    # Create midway level nodes w/ two leafNode children each:
    midwayNodes = []
    for i in range(6):
        parent = Node()
        parent.children = [leafNodes[2 * i], leafNodes[2 * i + 1]]
        midwayNodes.append(parent)
        
    # Create topMost level nodes w/ two midway level children each:
    topMostNodes = []
    for i in range(3):
        parent = Node()
        parent.children = [midwayNodes[2 * i], midwayNodes[2 * i + 1]]
        topMostNodes.append(parent)
        
    # Create root node w/ two topMost level children:
    root = Node()
    root.children = topMostNodes
    return root
    
# Alpha Beta Search w/ Pruning Function:
def searchPruning(values):
    root = tree(values)
    pruned = []
    alphaBeta(root, 3, float('-inf'), float('inf'), True, pruned)
    return sorted(pruned)
    
if __name__ == "__main__":
    # Input here:
    values = list(map(int, input("Input: ").split()))

    # Limiting output response to only if the input has 12 values:
    if len(values) != 12:
        raise ValueError("Exactly 12 values are required.")

    # Output here:
    pruned = searchPruning(values)
    print("Output: ", " ".join(map(str, pruned)))