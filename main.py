from display import *
from draw import *
from matrix import *
import random

print("TESTING MATRIX MULT...")
a =[[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]]
b = [[10, 11, 12, 13], [11, 12, 13, 14]]
print("MATRIX ONE: ")
print_matrix(a)
print("\nMATRIX TWO: ")
print_matrix(b)
matrix_mult(a, b)
print("\nFINAL MATRIX: ")
print_matrix(b)

print("\n\nTESTING IDENT...")
x = new_matrix()
add_point(x,1,2,3)
add_point(x,2,3,5)
add_point(x,2,3,3)
add_point(x,2,3,4)
add_edge(x,1,3,5,3,4,1)
print('ORIGINAL MATRIX: ')
print_matrix(x)
x = ident(x)
print('\nFINAL MATRIX: ')
print_matrix(x)


print("GENERATING IMAGE...")

screen = new_screen()
matrix = new_matrix()
c = [ 210, 145, 188 ]
for x in range(100):
    add_edge(matrix, random.randrange(120), random.randrange(120), random.randrange(120), random.randrange(120), random.randrange(120), random.randrange(120))
    add_edge(matrix, random.randint(400, 500), random.randint(400, 500), random.randint(400, 500), random.randint(400, 500), random.randint(400, 500), random.randint(400, 500))
    add_edge(matrix, random.randint(100, 220), random.randint(100, 220), random.randint(100, 220), random.randint(100, 220), random.randint(100, 220), random.randint(100, 220))
    add_edge(matrix, random.randint(300, 420), random.randint(300, 420), random.randint(300, 420), random.randint(300, 420), random.randint(300, 420), random.randint(300, 420))
    add_edge(matrix, random.randint(400, 500), random.randint(0, 120), random.randint(400, 500), random.randint(400, 500), random.randint(0, 120), random.randint(400, 500))
    add_edge(matrix, random.randint(300, 420), random.randint(100, 220), random.randint(300, 420), random.randint(300, 420), random.randint(100, 220), random.randint(300, 420))
    add_edge(matrix, random.randint(100, 220), random.randint(300, 420), random.randint(100, 220), random.randint(100, 220), random.randint(300, 420), random.randint(100, 220))
    add_edge(matrix, random.randrange(120), random.randint(400, 500), random.randrange(120), random.randrange(120), random.randint(400, 500), random.randrange(120))
    add_edge(matrix, random.randint(220, 300), random.randint(200, 320), random.randint(200, 320), random.randint(200, 320), random.randint(200, 320), random.randint(200, 320))

draw_lines(matrix, screen, c)
print("image generated: img.png")
save_ppm(screen, 'img.ppm')
display(screen)
save_extension(screen, 'img.png')
