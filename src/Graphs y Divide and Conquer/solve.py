def solve2(m,n,m0,n0,m1,n1):
  mc = m0 + m1
  nc = n0 + n1
  if mc == n and nc == n:
    return " "
  if m / n < mc/nc :
    return f"L{solve2(m, n, m0, n0, mc, nc)}"
  else:
    return f"R{solve2(m, n, mc, nc, m1, n1)}"
while True:
    m, n = [int(x) for x in input().split()]
    if m == 1 and n == 1:
      break
    resp = solve2(m, n, 0, 1, 1, 0)
