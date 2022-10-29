nums1 = [1, 2, 3, 2, 1]
nums2 = [3, 2, 1, 4, 7]
strnum2 = ''.join([chr(x) for x in nums2])
strmax = ''
ans = 0
for num in nums1:
    strmax += chr(num)
    if strmax in strnum2:
        ans = max(ans, len(strmax))
    else:
        strmax = strmax[1:]
print(ans)
