def is_safe(region, color, assignment, neighbors):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment, regions, colors, neighbors):
    # If all regions are assigned a color
    if len(assignment) == len(regions):
        return assignment

    # Select an unassigned region
    unassigned = [r for r in regions if r not in assignment]
    region = unassigned[0]

    for color in colors:
        if is_safe(region, color, assignment, neighbors):
            assignment[region] = color
            result = backtrack(assignment, regions, colors, neighbors)
            if result:
                return result
            # Undo assignment (backtrack)
            del assignment[region]

    return None

# Define regions (like states or countries)
regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

# Define colors
colors = ['Red', 'Green', 'Blue']

# Define neighbors (adjacency)
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []  # Tasmania is an island, no neighbors
}

solution = backtrack({}, regions, colors, neighbors)

if solution:
    print("Solution found:")
    for region in regions:
        print(f"{region}: {solution[region]}")
else:
    print("No solution found.")
