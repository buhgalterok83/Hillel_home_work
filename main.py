# s = input("Enter a string: ").strip().lower()
# n = len(s)
# for i in range(n // 2):
#     if s[i] != s[n - i - 1]:
#         print(False)
#         break
# else:
#     print(True)


s = input("Enter a string: ").strip().lower()
if s == s[::-1]:
    print(True)
else:
    print(False)