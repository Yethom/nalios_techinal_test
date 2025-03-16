import time

# https://playgameoflife.com
# if dead cell has 3 living neighbors, it becomes alive
# if living cell has < 2 or > 3 neighbors, it dies
# living cell must have exactly 2 or 3 neighbors to stay alive


# this will display the matrix in the console, if a cell is alive (1) it will be displayed as a "█"
# otherwise (0) it will be displayed as a "."
def display_matrix(matrix):
    for row in matrix:
        print(" ".join("█" if cell else "." for cell in row))
    time.sleep(1)

# bonus
def save_matrix_html(matrix, filename="matrix.html"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("<html><body><h1>Game of Life</h1>\n")
        for row in matrix:
            f.write(" ".join("1" if cell else "0" for cell in row) + "<br>\n")
        f.write("</body></html>")

def count_neighbors(matrix, x, y):
    count = 0
    rows, columns = len(matrix), len(matrix[0])
    # those 2 loops will find the surrounding neighbors of the given cell
    # by going from -1 to 1, so it can move around the cell in the 2D grid (matrix)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nx, ny = x + i, y + j
            if 0 <= nx < rows and 0 <= ny < columns:
                count += matrix[nx][ny]
    return count


# function that will iterate through the matrix and return the new one each time
def iterate(matrix):
    # creation of new matrix filled with zeros
    new_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            neighbors = count_neighbors(matrix, i, j)
            if matrix[i][j] == 0 and neighbors == 3:
                new_matrix[i][j] = 1
            elif matrix[i][j] == 1 and neighbors in [2, 3]:
                new_matrix[i][j] = 1
    # bonus
    save_matrix_html(new_matrix)
    return new_matrix


matrix = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# we want 5 iterations but the first one is the original matrix
for i in range(6):
    print(f"iteration {i}:")
    display_matrix(matrix)
    print("--------------------")
    matrix = iterate(matrix)
