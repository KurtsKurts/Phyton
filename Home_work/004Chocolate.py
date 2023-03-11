# Требуется определить, можно ли от шоколадки размером m × n долек
# отломить k долек, если разрешается сделать один разлом по прямой
# между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

Choco_vert = int(input('Размер плитки по вертикали : '))
Choco_horiz = int(input('Размер плитки по горизонтали : '))
Piece = int(input('Количество долек : '))
if Piece < Choco_vert * Choco_horiz and ((Piece % Choco_vert == 0) or (Piece % Choco_horiz == 0)):
    print('YES')
else: print('NO')