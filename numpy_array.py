import numpy  as np
# lst=[1,2,3,4,5]
# arr= np.array(lst)
# print(arr>2)
# print(arr[arr<2])

# arr[3]=8
# print(arr)
# print(arr[1:-1])
# print(arr[:-1])
# print(arr[::-1])
lst1 =[1,2,3,4]
lst2 =[2,3,4,5]
lst3 = [3,4,5,6]
arr1 = np.array([lst1,lst2,lst3])
print(arr1.reshape(4,3))
# print(arr1)
# print(arr1[:,3])
# print(arr1[:,(1,3)])
# print(arr1[:,1:3])
# print(arr1.shape)
# print(np.arange(1,20,2).reshape(1,10,1))'''(1,10,1)-> resemble 1 for row , 10 for column and 1 for dimension'''
print(np.ones((5,3)))
print(np.random.randint(5,12,4).reshape(2,2))
print(np.random.randn(2,5))