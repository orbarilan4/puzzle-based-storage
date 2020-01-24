from copy import deepcopy


# Return the all possible paths from top left to bottom right of a mXn grid
def find_paths(grid):
    all_paths = []
    m = grid.shape[0]
    n = grid.shape[1]
    path = [0 for d in range(m + n - 1)]

    def find_paths_(grid, m, n, i, j, path, indx):
        if i == m - 1:
            for k in range(j, n):
                path[indx + k - j] = grid[i][k]
                # if we hit this block, it means one path is completed.
            # Add it to paths list and print
            all_paths.append(deepcopy(path))
            return
            # if we reach to the right most corner, we can only move down
        if j == n - 1:
            for k in range(i, m):
                path[indx + k - i] = grid[k][j]
            # if we hit this block, it means one path is completed.
            # Add it to paths list and print
            all_paths.append(deepcopy(path))
            return

        # add current element to the path list
        path[indx] = grid[i][j]

        # move down in y direction and call findPathsUtil recursively
        find_paths_(grid, m, n, i + 1, j, path, indx + 1)

        # move down in x direction and call findPathsUtil recursively
        find_paths_(grid, m, n, i, j + 1, path, indx + 1)

    find_paths_(grid, m, n, 0, 0, path, 0)
    return all_paths

