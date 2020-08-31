n=int(input());v=0
     
poly = {
    'Tetrahedron':4,
    'Cube':6,
    'Octahedron':8,
    'Dodecahedron':12,
    'Icosahedron':20
}
     
for i in range(n):
    v+=poly.get(input())
     
     
print(v)