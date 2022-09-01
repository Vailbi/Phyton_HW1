# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
X = True
Y = True
Z = True

print(not (X and Y and Z) == (not X) or (not Y) or (not Z))
