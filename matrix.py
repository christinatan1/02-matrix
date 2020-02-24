# """
# A matrix will be an N sized list of 4 element lists.
# Each individual list will represent an [x, y, z, 1] point.
# For multiplication purposes, consider the lists like so:
# x0  x1      xn
# y0  y1      yn
# z0  z1  ... zn
# 1  1        1
# """
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix(matrix):
    m1 = " "
    m2 = " "
    m3 = " "
    m4 = " "
    x= 0
    #while x < len(matrix):
    for x in range(len(matrix)):
        m1 += (str(matrix[x][0]) + " ")
        m2 += (str(matrix[x][1]) + " ")
        m3 += (str(matrix[x][2]) + " ")
        m4 += (str(matrix[x][3]) + " ")
        x+=1
    print m1
    print m2
    print m3
    print m4

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if x == y:
                matrix[x][y] = 1
            else:
                matrix[x][y] = 0
    return matrix

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult(m1, m2):
    result = new_matrix(cols = len(m2))
    #rows in m1:
    for x in range(len(m2)):
        #columns in m2:
        for y in range(len(m1[0])):
            #rows in m2:
            for z in range(len(m1)):
                result[x][y] += m1[z][y] * m2[x][z]
    for i in range(len(result)):
        for j in range(len(result[0])):
            m2[i][j] = result[i][j]

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
