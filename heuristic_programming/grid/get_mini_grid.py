

# For a given grid and two points, it will generate a 'mini grid'.
# Which start in first_point and end in second_point (or vice versa)
# Example: first_point = [1,1]
#          second_point = [0,2]
#          grid = [ p p x ]
#                 [ p e e ]
#                 [ p p p ]
# The mini grid will be: mini_grid = [ p x ]
#                                    [ e e ]
# Other definition: 'mini grid' the minimum rectangle in grid which contains both points
def get_mini_grid(grid, first_point, second_point):
    # Create two points which will define the rectangle by his smallest coordinate (point) and the largest
    start_point = []
    end_point = []
    for i in range(0, 2):
        start_point.append(first_point[i] if first_point[i] < second_point[i] else second_point[i])
    for i in range(0, 2):
        end_point.append(first_point[i] if first_point[i] > second_point[i] else second_point[i])

    # Create the mini grid (the rectangle) by the two points
    return grid[start_point[0]:(end_point[0] + 1), start_point[1]:(end_point[1] + 1)], start_point, end_point