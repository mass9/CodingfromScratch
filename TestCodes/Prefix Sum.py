    """
    Prefix sum is to be use of
    1. Equlibrium index of an array: sum of lower indexes is equal to sum higher indexes
    2. If  there is a subarray with ) sum
    3. Maximum subarray size
    4. Find the prime numbers which can written as sum of most comsecutive primes
    5. Longes Span with same Sum of two Binary Arrays.
    6. Maximum subarray size mudulo m
    7. Maximum subarray size , such that all subarrays of that size have sum less than k
    8. Maximum occured integer in n ranges
    9.  Minimu cost of acquiring all doins eith k extra coins
    10. Random number generator in probability distribution fashion
    .
    
    """

# Python Program for Implementing  
# prefix sum array 
  
# Fills prefix sum array 
def fillPrefixSum(arr, n, prefixSum): 
  
    prefixSum[0] = arr[0] 
  
    # Adding present element 
    # with previous element 
    for i in range(1, n): 
        prefixSum[i] = prefixSum[i - 1] + arr[i] 
  
# Driver code 
arr =[10, 4, 16, 20 ] 
n = len(arr) 
  
prefixSum = [0 for i in range(n + 1)] 
  
fillPrefixSum(arr, n, prefixSum) 
  
for i in range(n): 
    print(prefixSum[i] , " ", end="") 
  