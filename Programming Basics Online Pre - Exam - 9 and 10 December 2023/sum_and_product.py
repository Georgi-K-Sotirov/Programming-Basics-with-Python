number = int(input())
condition = False
for a in range(1, 9 + 1):
 for b in range(9, a, -1):
  for c in range(9 + 1):
   for d in range(9, c, -1):
    if (a + b + c + d) == (a * b * c * d) and number % 10 == 5:
     print(f"{a}{b}{c}{d}")
     condition = True
     break
    if (a * b * c * d) // (a + b + c + d) == 3 and number % 3 == 0:
     print(f"{d}{c}{b}{a}")
     condition = True
     break
   if condition:
    break
  if condition:
   break
 if condition:
  break
if not condition:
 print("Nothing found")