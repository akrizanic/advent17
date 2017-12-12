from day3.puzzle_funcs import create_fill_steps, create_empty_array, fill_array_with_neighbour_sums_until_over


size = 325489
arr = create_empty_array(size)
steps = create_fill_steps(size)

over = fill_array_with_neighbour_sums_until_over(steps, arr)
print(over)
