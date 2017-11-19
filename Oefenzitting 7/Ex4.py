def mystery(a,b):
	if b==0:
		return 0
	elif b % 2 == 0:
		return mystery(a + a, b/2)
	else:
		return mystery(a + a, b // 2) + a

# mystery(14,3), mystery(3,14), mystery(2,21)
#
# mystery(14,3):
# (14,3) -> (28,1) + 14 -> (56,0) + 28 -> 0 ==> 14 + 28 = 42
#
# mystery(3,14):
# (3,14) -> (6,7) -> (12,3) + 6 -> (24,1) + 12 -> (48,0) + 24 ==> 6+12+24 = 42
#
# mystery(2,21):
# (2,21) -> (4,10) + 2 -> (8,5) -> (16,2) + 8 -> (32,1) -> (64,0) + 32 ==> 32+8+2 = 42

print(mystery(14,3))
print(mystery(3,14))
print(mystery(2,21))