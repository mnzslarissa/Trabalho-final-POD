def interpolationSearch(A, target):

    if not A:
        return -1
    (left, right) = (0, len(A) - 1)
 
    while A[right] != A[left] and A[left] <= target <= A[right]:
        mid = left + (target - A[left]) * (right - left) // (A[right] - A[left])
        # A chave # foi encontrada
        if target == A[mid]:
            return mid
        # descarta todos os elementos no espaço de busca correto, incluindo o elemento do meio
        elif target < A[mid]:
            right = mid - 1
        # descarta todos os elementos no espaço de pesquisa à esquerda, incluindo o elemento do meio
        else:
            left = mid + 1
 
    # se a chave for encontrada
    if target == A[left]:
        return left
    return -1
 
 
if __name__ == '__main__':
 
    A = [2, 5, 6, 8, 9, 10]
    key = 8
 
    index = interpolationSearch(A, key)
 
    if index != -1:
        print('Elemento encontrado no índice', index)
    else:
        print('Elemento não encontrado na lista')
 