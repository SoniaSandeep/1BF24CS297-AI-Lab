# Alpha-Beta Pruning

def alpha_beta(node, alpha, beta, maximizing):

    if isinstance(node, int):
        return node

    if maximizing:
        value = float('-inf')

        for child in node:
            value = max(value, alpha_beta(child, alpha, beta, False))
            alpha = max(alpha, value)

            if alpha >= beta:
                print("Pruned:", node)
                break

        return value

    else:
        value = float('inf')

        for child in node:
            value = min(value, alpha_beta(child, alpha, beta, True))
            beta = min(beta, value)

            if beta <= alpha:
                print("Pruned:", node)
                break

        return value


# Game tree
tree = [
    [
        [10, 9],
        [14, 18]
    ],
    [
        [5, 4],
        [50, 3]
    ]
]

# Root is MAX
result = alpha_beta(tree, float('-inf'), float('inf'), True)

print("Root value:", result)
