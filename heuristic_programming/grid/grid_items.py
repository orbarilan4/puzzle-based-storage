

# For a given grid and item name it finds all the items in it
# Return the locations
def get_grid_items(grid, item):
    items = []
    for row in range(0, grid.shape[0]):
        for col in range(0, grid.shape[1]):
            if grid[row, col] == item:
                items.append([row, col])
    return items


