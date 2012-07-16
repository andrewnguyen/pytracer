# film.py
# Andrew Nguyen Jul 15 2012
# Creates the image itself

def create_film(width, height):
    film = []
    for j in range(height):
        w = []
        for i in range(width):
            w.append(0)
        film.append(w)
    return film

def get_pixel(film, x, y):
    return film[y][x]

def develop(film, x, y, color):
    film[y][x] = color

ascii_lst = [' ', '.', ',', '-', '+', '?', '*', '#', '@']
def ascii(c):
    return ascii_lst[c]

def display(film):
    for j in range(len(film)):
        for i in range(len(film[j])):
            disp = ascii(get_pixel(film, i, j))
            print(disp, end = "")
        print("\n", end="")

    
