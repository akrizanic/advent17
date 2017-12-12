from day3.puzzle_funcs import create_fill_steps, calculate_last_step_distance


size = 325489
steps = create_fill_steps(size)
print(calculate_last_step_distance(steps))
