import time
from grid import Grid
from algorithm import Search
import argparse

textFile = 'RobotNav-test.txt'


def parse_coordinates(text):
    text = text.strip('[]()\n')
    return tuple(map(int, text.split(',')))

def read_grid_setup(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

        dimensions = parse_coordinates(lines[0])
        starting_location = parse_coordinates(lines[1])[::-1]
        goal_states = [parse_coordinates(goal.strip())[::-1] for goal in lines[2].split('|')]
        walls = [parse_coordinates(line) for line in lines[3:]]
        return dimensions, starting_location, goal_states, walls

parser = argparse.ArgumentParser(description='Robot Navigation Program')
parser.add_argument('filename', type=str, help='Input filename')
parser.add_argument('method', type=str, help='Search method (dfs, bfs, gbfs, a*, ucs, best-first-search)')
args = parser.parse_args()

textFile = args.filename
search_method = args.method

dimensions, starting_location, goal_states, walls = read_grid_setup(textFile)
rows, cols = dimensions

grid = Grid(rows, cols, starting_location, goal_states, walls)
search = Search(grid)

def execute_search(algorithm):
    start_time = time.time()
    result = search.search(algorithm=algorithm)
    end_time = time.time()
    duration = end_time - start_time

    path = result.strip(";").split("; ")

    if not path or all(x.isspace() for x in path):
        path_output = "No Path Found"
    else:
        path_output = ', '.join(path)      
    search_nodes = search.get_search_movement()
    return path, path_output, duration, search_nodes


goals_found = []

path, path_output, duration, search_nodes = execute_search(search_method)

print(f"Search method: {search_method}")
print(f"Path: {path_output}")
print(f"Number of searched nodes: {len(search_nodes)}")
print(f"Time taken: {duration} seconds")
