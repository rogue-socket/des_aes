# take 64bit input for key, K
# K = "0001001100110100010101110111100110011011101111001101111111110001"
K = input("Enter 64bit key in binary: ")
# M = "0000000100100011010001010110011110001001101010111100110111101111"
M = input("Enter the 64bit input: ")
print("Key: ", K)

# convert K to K+ using PC1
pc1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

# Number of bit shifts
shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

pc2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]

# permutation for IP
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

e_bit_exp = [32, 1, 2, 3, 4, 5, 4, 5,
             6, 7, 8, 9, 8, 9, 10, 11,
             12, 13, 12, 13, 14, 15, 16, 17,
             16, 17, 18, 19, 20, 21, 20, 21,
             22, 23, 24, 25, 24, 25, 26, 27,
             28, 29, 28, 29, 30, 31, 32, 1]

sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

ptable = [16, 7, 20, 21,
          29, 12, 28, 17,
          1, 15, 23, 26,
          5, 18, 31, 10,
          2, 8, 24, 14,
          32, 27, 3, 9,
          19, 13, 30, 6,
          22, 11, 4, 25]

ipinv = [40, 8, 48, 16, 56, 24, 64, 32,
         39, 7, 47, 15, 55, 23, 63, 31,
         38, 6, 46, 14, 54, 22, 62, 30,
         37, 5, 45, 13, 53, 21, 61, 29,
         36, 4, 44, 12, 52, 20, 60, 28,
         35, 3, 43, 11, 51, 19, 59, 27,
         34, 2, 42, 10, 50, 18, 58, 26,
         33, 1, 41, 9, 49, 17, 57, 25]


def xor(a, b):
    ans = []
    for i in range(len(a)):
        if a[i] == b[i]:
            ans.append('0')
        else:
            ans.append('1')
    return ans


def func(rprev, key):
    # expand rn-1 32 -> 48
    e_rprev = ["0"] * 48
    i = 0
    for elem in e_bit_exp:
        e_rprev[i] = rprev[elem - 1]
        i += 1

    e_rprev = xor(e_rprev, key)
    ans = ""
    j = 0
    for i in range(0, 48, 6):
        bt = e_rprev[i:(i + 6)]
        row = bt[0] + bt[-1]
        col = "".join(bt[1:5])
        row_i = int(row, 2)
        col_i = int(col, 2)
        print(f"col_i: {col_i}, row_i: {row_i}, ans: {bin(sbox[j][row_i][col_i])[2:].zfill(4)}")
        ans += bin(sbox[j][row_i][col_i])[2:].zfill(4)
        j += 1

    ans = list(ans)
    penans = ["0"] * 32
    for idx, pos in enumerate(ptable):
        penans[idx] = ans[pos - 1]
    return penans


def encrypt(K, M):
    Kplus = ["0"] * 56
    i = 0

    for elem in pc1:
        Kplus[i] = K[elem - 1]
        i += 1

    # make c0 and d0 by halving k+
    c0 = Kplus[:28]
    d0 = Kplus[28:]

    #generating c0n0, c1n1, c2n2, ...., using shifting table
    cknk = []
    cknk.append(c0 + d0)
    ct = c0
    dt = d0
    for i in shift_table:
        if i == 1:
            # shift once
            ct = ct[1:] + [ct[0]]
            dt = dt[1:] + [dt[0]]
        else:
            # 2ice
            ct = ct[2:] + ct[:2]
            dt = dt[2:] + dt[:2]
        cknk.append(ct + dt)

    # forming k1, k2, k3... using PC2 table on c1 d1, c2 d2...
    kfinal = []

    for i in range(1, 17):
        kt = cknk[i]
        knt = ["0"] * 48
        idx = 0
        for p in pc2:
            knt[idx] = kt[p - 1]
            idx += 1
        kfinal.append(knt)

    print("The final 16keys are: ")
    for elem in kfinal:
        print("".join(elem))

    Mn = ["0"] * 64
    j = 0
    for i in IP:
        Mn[j] = M[i - 1]
        j += 1

    # Dividing the Mn to L0 and R0
    l0 = Mn[:32]
    r0 = Mn[32:]
    lt = l0
    rt = r0

    for i in range(16):
        ltt = rt
        print(i, " done")
        rt = xor(lt, func(rt, kfinal[i]))
        lt = ltt

    temp = rt + lt
    ans_pen = ['0'] * 64
    j = 0
    for i in ipinv:
        ans_pen[j] = temp[i - 1]
        j += 1

    enc = "".join(ans_pen)
    return enc, kfinal


def decrypt(M, kfinal):
    Mn = ["0"] * 64
    j = 0
    for i in IP:
        Mn[j] = M[i - 1]
        j += 1

    # Dividing the Mn to L0 and R0
    l0 = Mn[:32]
    r0 = Mn[32:]
    lt = l0
    rt = r0

    for i in range(16):
        ltt = rt
        print(i, " done")
        rt = xor(lt, func(rt, kfinal[i]))
        lt = ltt

    temp = rt + lt
    ans_pen = ['0'] * 64
    j = 0
    for i in ipinv:
        ans_pen[j] = temp[i - 1]
        j += 1
    enc = "".join(ans_pen)
    return enc, kfinal


encrypted_text, keys = encrypt(K, M)
decrypting_ip = encrypted_text
decrypted_text, decrypting_keys = decrypt(decrypting_ip, keys[::-1])  # reversing the keys for the decryption process
print(f"\nInput: {M}\nKey: {K}\nEncrypted Output: {encrypted_text}")
print(f"For decryption\nInput: {decrypting_ip}\nOutput(original input): {decrypted_text}")