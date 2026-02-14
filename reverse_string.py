def reverse_string(s):
 n = len(s)
 print(n)
 while n > 0:
    #for i in range(len(s)-1):
        print(s[n-1])
        n-=1


v = "vinay"
reverse_string(v)

print(v[::-1])