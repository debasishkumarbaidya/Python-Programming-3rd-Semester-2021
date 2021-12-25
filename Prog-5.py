term=int(input())
if term%2==0:
term=term//2
print((1/3)*(3**term))
else:
term=(term//2)+1
print((1/2)*(2**term))