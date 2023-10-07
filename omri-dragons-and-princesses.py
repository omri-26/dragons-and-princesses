#!/usr/bin/python
import yaml

# Read input from a YAML file
with open('parameters.yaml', 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)

# Extract relevant information from the list of dictionaries
n = data['n'] -1
items = data['items']
cells = [(item['type'], item['value']) for item in items] 


#beauty_levels = [int(cell[1]) if cell[0] == 'p' else float('inf') for cell in cells]
max_gold = 0
dragons_to_kill = []


def backtrack(current_cell, current_gold, dragons_killed):
    global max_gold

    if current_cell == n:  # Reached the last cell
        if (len(dragons_killed)) < (cells[current_cell-1][1]):
            return (-1)
        else:    
            if current_gold > max_gold:
                max_gold = current_gold
                dragons_to_kill[:] = dragons_killed.copy()                
        return

    # Calculate the index of the next cell
    next_cell = current_cell + 1

    # Option 1: Skip the current cell
    backtrack(next_cell, current_gold, dragons_killed)

    # Option 2: Kill the dragon in the current cell
    if cells[current_cell - 1][0] == 'd':
        coins = cells[current_cell - 1][1]
        new_gold = current_gold + coins
        new_dragons_killed = dragons_killed + [current_cell]
        # Check if the knight can marry the princess at the next cell without exceeding n
        if next_cell < n and cells[next_cell - 1][0] == 'p' and len(new_dragons_killed) >= cells[next_cell - 1][1]:
            # Avoid killing the dragon if it would make the number of killed dragons equal to the beauty level
            backtrack(next_cell, current_gold, dragons_killed)
        # elif next_cell == n:
        #      backtrack(next_cell, new_gold, new_dragons_killed)
        else:
            # Continue with killing the dragon
            backtrack(next_cell, new_gold, new_dragons_killed)

# Start from the first cell (cell 1), with 0 gold and no dragons killed
backtrack(1, 0, [])

#if max_gold > 0:
if len(dragons_to_kill) > 0:    
    print(f'max-gold:{max_gold}')
    print(f'num of dragons to kill: {len(dragons_to_kill)}')
    print(f'cells-to-kill: {dragons_to_kill}')
else:
    print(-1)

 
