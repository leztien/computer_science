"""
Compresses Sparse Row (CSR) matrix

https://www.researchgate.net/publication/357418189/figure/fig1/AS:1106555248345089@1640834738634/The-Compressed-Sparse-Row-CSR-format-for-representing-sparse-matrices-provides-a.ppm
"""


class CSR:
    """Converts a matrix to a Compresses Sparse Row (CSR) matrix"""
    def __init__(self, matrix):
        self.row_pointers = [0,]
        self.column_offsets = []
        self.data = []
        self.shape = (len(matrix), len(matrix[0]))
        
        for i in range(self.shape[0]):
            for j,v in enumerate(matrix[i]):
                if v:
                    self.column_offsets.append(j)
                    self.data.append(v)
            self.row_pointers.append(len(self.data))
        
    def to_dense_matrix(self):
        # initialize a matrix full of zeros
        mx = [[0 for _ in range(self.shape[1])] for _ in range(self.shape[0])]
        
        # fill in the matrix with values
        for i in range(self.shape[0]):
            a = self.row_pointers[i]
            b = self.row_pointers[i+1]
            idx = self.column_offsets[a:b]
            for j,v in zip(idx, self.data[a:b]):
                mx[i][j] = v
        return mx
            
    
    def __getitem__(self, index):
        i,j = index
        if not (0 <= i < self.shape[0] and 0 <= j < self.shape[1]):
            raise IndexError("bad index")
        a = self.row_pointers[i]
        b = self.row_pointers[i+1]
        idx = self.column_offsets[a:b]
        return self.data[a:b][idx.index(j)] if j in idx else 0



if __name__ == '__main__':
    
    import numpy as np
    
    # make a random sparse matrix
    mx = np.clip(np.random.randint(-200, 100, size=np.random.randint(1, 20, size=2)),
                 0, np.inf).astype(np.uint8).tolist()
    
    # convert to a CSR
    sm = CSR(mx)
    
    # restore back to a dense matrix
    out = sm.to_dense_matrix()
    
    # test
    for i in range(len(mx)):
        for j in range(len(mx[0])):
            assert mx[i][j] == sm[i,j]
    
    # report
    print(np.array(out))
    print("\nrestored correctly:", mx == out)

