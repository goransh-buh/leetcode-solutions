"""
Detect Cycle in Directed Graph

Approach: DFS with three states per node — unvisited, visiting, visited.
A cycle exists if we encounter a node currently being visited.
Time: O(V + E), Space: O(V)
"""

from typing import List, Dict


def has_cycle(graph: Dict[int, List[int]]) -> bool:
    WHITE, GRAY, BLACK = 0, 1, 2
    state = {node: WHITE for node in graph}

    def dfs(node: int) -> bool:
        state[node] = GRAY
        for neighbor in graph.get(node, []):
            if state.get(neighbor, WHITE) == GRAY:
                return True
            if state.get(neighbor, WHITE) == WHITE and dfs(neighbor):
                return True
        state[node] = BLACK
        return False

    for node in graph:
        if state[node] == WHITE:
            if dfs(node):
                return True
    return False


if __name__ == "__main__":
    assert has_cycle({0: [1], 1: [2], 2: [0]}) == True
    assert has_cycle({0: [1], 1: [2], 2: []}) == False
    print("All tests passed.")
