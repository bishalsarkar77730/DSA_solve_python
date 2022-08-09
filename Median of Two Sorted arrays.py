nums1 = [1, 2]
nums2 = [4, 5]

new = sorted(nums1 + nums2)
if len(new) % 2 != 0:
    med = new[(len(new) // 2)]
else:
    med = (new[(len(new) // 2)] + new[(len(new) // 2) - 1]) / 2
print(med)
