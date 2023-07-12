import math

def jumpSearch( arr , x , n ):
	
	step = math.sqrt(n)

	prev = 0
	while arr[int(min(step, n)-1)] < x:
		prev = step
		step += math.sqrt(n)
		if prev >= n:
			return -1
	
	while arr[int(prev)] < x:
		prev += 1
		
		if prev == min(step, n):
			return -1
	
	#If elemento encontrado
	if arr[int(prev)] == x:
		return prev
	
	return -1

#Código para testar a função
arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
	34, 55, 89, 144, 233, 377, 610 ]
x = 55
n = len(arr)

#Encontre o índice de 'x' usando Jump Search
index = jumpSearch(arr, x, n)

# Imprima o índice onde 'x' está localizado
print("Número" , x, "está no índice" ,"%.0f"%index)
