import sys
print(str(sorted(set([int(sys.argv[6 * i]) for i in range(1, (len(sys.argv)-1) // 6 + 1) if int(sys.argv[6 * i]) % 6 == 0]))).replace(',', '').replace('[', '').replace(']', ''))