def div(a, b):
  d = a // b
  r = a % b

  return d, r

def euclides(p1, p2):
  a = p1 if p1 > p2 else p2
  b = p2 if p1 > p2 else p1

  d, r = div(a, b)

  print(f"{a} = {d} * {b} + {r}")

  if r == 0:
    return b
  else:
    return euclides(b, r)

print(euclides(210, 45))



