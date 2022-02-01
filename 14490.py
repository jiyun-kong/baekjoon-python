import math

n, m = map(int, input().split(':'))
gcd = math.gcd(n, m)
print("{}:{}".format(int(n/gcd), int(m/gcd)))
