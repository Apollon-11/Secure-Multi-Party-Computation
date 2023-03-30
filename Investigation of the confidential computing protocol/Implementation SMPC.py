# Implementation SMPC

def next_prime(n):
    if n < 0:
        raise ValueError

    for next1 in range(n + 1, n + 200):
        if next1 > 1:
            for i in range(2, next1):
                if (next1 % i) == 0:
                    break
                else:
                    return next1


# Selecting Options RSA
p = next_prime(22)
q = next_prime(28)
N = p * q
m = (p - 1) * (q - 1)
e = 13
d = pow(e, -1, m)
print("N=", N, "e=", e, "d=", d)

# Selecting Protocol Options
A0 = 11  # Secret number Alice 1<=A0<=NN
B0 = 12  # Secret number Bob 1<=B0<=NN
NN = 20
P = next_prime(460)
print("P=", P)

# Step 1 (Bob)
x = 84
print("x=", x)
k = pow(x, e, N)
print('k=', k)
# Step 2 (B -> A)
kB = k - B0
print('kj=', kB)

# Step 3 (Alice)
y = [pow(kB + u, d, N) for u in range(1, NN + 1)]
print("y=", y)
z = [int(v) % P for v in y]
print("z=", z)

# Step 4 (A -> B)
z1 = [z[i] for i in range(0, A0)]
z2 = [z[i] + 1 for i in range(A0, NN)]
z1.extend(z2)
z1.append(P)
print("z1=", z1)

# Step 5 (Bob)
pz = z1[-1]
print('P=', pz)
xz = z1[B0 - 1]
print('xz=', xz)
rez = xz - x
print('x=', x, 'rez=', rez)
if rez % pz == 0 % pz:
    print('A >= B')
else:
    print('A < B')
