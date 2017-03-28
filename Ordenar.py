from Artista import Artista
def mergeSort(arreglo):
	size = len(arreglo)
	if (size < 2):
		return
	mid = int(size+1/2)
	left = arreglo[:mid]
	right = arreglo[mid:]
	mergeSort(left)
	mergeSort(right)
	merge(left, right, arreglo)


def merge(left, right, arreglo):
	leftSize = len(left)
	rightSize = len(right)
	i = 0
	j = 0
	k = 0

	while(i < leftSize and j < rightSize):
		if (left[i].getReputacion() > right[i].getReputacion()):
			arreglo[k] = left[i]
			i += 1
			k += 1
		else:
			arreglo[k] = right[j]
			k += 1
			j += 1

	while(i < leftSize):
		arreglo[k] = left[i]
		k += 1
		i += 1

	while(j < rightSize):
		arreglo[k] = right[j]
		k += 1
		j += 1
