# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            n = (not (x or y or z)) == ((not x) and (not y) and (not z))
            print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}  : {n}')
