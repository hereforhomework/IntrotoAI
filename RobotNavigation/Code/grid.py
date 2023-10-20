class Grid:
    def __init__(self, rows, cols, starting_location, goal_states, walls):
        self.rows = rows
        self.cols = cols
        self.starting_location = starting_location
        self.goal_states = goal_states
        self.walls = walls

    def initial_state(self):
        grid = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        for goal_state in self.goal_states:
            x, y = goal_state
            grid[x][y] = 'G'
        x, y = self.starting_location
        grid[x][y] = 'S'
        for wall in self.walls:
            x, y, width, height = wall
            for i in range(x, x + width):
                for j in range(y, y + height):
                    grid[i][j] = 'W'
        return grid

    def print_grid(self, path=None):
        grid = self.initial_state()
        if path:
            x, y = self.starting_location
            for direction in path:
                if direction == 'up':
                    x -= 1
                elif direction == 'down':
                    x += 1
                elif direction == 'left':
                    y -= 1
                elif direction == 'right':
                    y += 1
                grid[x][y] = '*'
        for row in grid:
            print(' '.join(row))

    def draw_path(self, path, search_nodes):
        self.print_grid(path)
