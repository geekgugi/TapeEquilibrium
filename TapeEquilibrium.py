def solution(A):
    # when p = 0, left element is left sum
    leftSum = A[0]
    # sum of all element in list - left sum gives right sum
    rightSum = sum(A) - leftSum
    # get the difference
    minDiff = abs(leftSum - rightSum)
    
    # iterate through list starting from second element
    for i in range(1, len(A) - 1):
        # add next element to left sum
        leftSum += A[i]
        # deduct next element from right sum
        rightSum -= A[i]
        # check the difference
        diff = abs(leftSum - rightSum)
        # get latest minimum difference
        minDiff = min([minDiff, diff])
    # return result    
    return minDiff
