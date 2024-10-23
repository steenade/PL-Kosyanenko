import math
a=[1,2,3,4,5,6,7,8]
b=[]
i=0
for i in range(i,len(a)):
	if i%2==0:
		b.append(a[i])
print(sum(b), math.prod(b))


a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
max_index = a.index(max(a))
min_index = a.index(min(a))
a[max_index], a[min_index] = a[min_index], a[max_index]
print(a)

	





	

	

	
	
