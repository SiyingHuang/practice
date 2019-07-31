import numpy as np

arr2d.ndim
arr2d.shape
arr2d.reshape(2,6)

arr = np.array(list(np.arange(0,10)))

arr2d = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]])
arr2d[0][2] # arr2d[0,2]

arr3d = np.array([[[1,2,3],
                   [4,5,6]],

                 [[7,8,9],
                  [10,11,12]]])
arr3d[0]