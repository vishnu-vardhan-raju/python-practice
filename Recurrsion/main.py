# N = int(input())
# def series(n):
#     if n == 0:
#         return
#     series(n - 1)
#     print(n,end=" ")
#
#
#
# series(N)


# def power(N, R):
#     # Your code here
#
# def power1(N, R):
#     if R <= 0:
#        return 1
#     return (N ** (R & 1) * power1(N, R >> 1) ** 2) % 1000000007
#
#
# print(power1(12,21))\
# def subsetSums(arr, N):
#     # combisum=[]
#     if N==0:
#         return 0
# arr=[2,3]
# N=2
# def sumsub(arr,N):
#     c=[]
#     c.append(sum(arr))
#     c.append(0)
#     def helper(arr,N):
#         if N<=0:
#             return 0
#         c.append((sum(arr)-arr[N-1]))
#         if (sum(arr) - arr[N - 1]) == arr[N - 1]:
#             c.append(arr[N-1])
#         # arr.pop(N-1)
#         # print(sum(arr))
#         # print(arr)
#         return helper(arr,N-1)
#     helper(arr,N)
#     return c
#

# print(sumsub(arr,N))
import pandas
data = pandas.read_excel("Distances.xlsx")
print(data)

