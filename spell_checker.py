"""
https://sigmoidal.io/fuzzy-matching-a-simple-trick/
"""

import numpy as np
import scipy.sparse


class Vectorizer:
    """simulation of sklearn's CountVectorizer + some additional functionality"""
    def __init__(self, n_grams=None):
        self.n_grams = n_grams or 2
        self.features = None
        self.data = None
    
    def fit(self, data):
        start = self.n_grams[0] if hasattr(self.n_grams, '__iter__') else self.n_grams
        end = (self.n_grams if isinstance(self.n_grams, int) else self.n_grams[-1]) + 1
        features = set()
        [features.add(s.strip().lower()[i:i+n]) for s in data for n in range(start,end) for i in range(len(s)-(n-1)) ]
        self.features = tuple(sorted(features))
        return self
        
    def transfrom(self, data, normalize=False):
        if self.features is None: raise TypeError("You must fit the model first")
        if isinstance(data, str): data = [data,]
        m,n = (len(data), len(self.features))
        mx = scipy.sparse.lil_matrix((m, n), dtype='uint16')
        for i,s in enumerate(data):
            s = s.strip().lower()
            mx[i] = [s.count(self.features[j]) for j in range(n)]
        mx = mx.tocsr()
        return self.normalize(mx) if normalize else mx
    
    def fit_transform(self, data, normalize=False):
        self.fit(data)
        return self.transfrom(data, normalize)
    
    def normalize(self, data):
        """Normalizes each row so that the sum of components is equal to one."""
        if self.features is None: raise TypeError("You must fit the model first")
        totals = data.sum(axis=1).A.flatten()
        diagonal = 1 / (totals + 0.001)
        m = len(totals)
        N = scipy.sparse.csr_matrix((diagonal, (range(m), range(m))), shape=(m,m), dtype=np.float_)
        A = data if isinstance(data, scipy.sparse.csr.csr_matrix) else scipy.sparse.csr_matrix(data)
        return N.dot(A)
        
    def _compute_magnitudes(self, data):
        A = data if isinstance(data, scipy.sparse.csr.csr_matrix) else scipy.sparse.csr_matrix(data)
        return np.sqrt(A.multiply(A).sum(axis=1).A.flatten())

    def cosine_similarities(self, query, data):
        if not isinstance(data, (scipy.sparse.csr.csr_matrix, scipy.sparse.lil.lil_matrix)):
            data = self.fit_transform(data, normalize=True)
        if not isinstance(query, (scipy.sparse.csr.csr_matrix, scipy.sparse.lil.lil_matrix)):
            query = self.transfrom(query, normalize=True)
        data_norms = self._compute_magnitudes(data)
        query_norm = self._compute_magnitudes(query) 
        return data.dot(query.T).A.flatten() / (data_norms * query_norm)



def edit_distance(s1, s2, replacement_cost=2):
    """Stanford's Percy Liang (the fastest)"""
    
    # Cache for memoization
    cache = dict()
    
    # Inner recursive function
    def recurse(i, j, replacement_cost=2):
        # If cached - retrun from chache
        if (i,j) in cache: return cache[(i,j)]
        
        # Base case
        if i == 0: return j
        if j == 0: return i
        
        # If last letters are the same
        if s2[i-1] == s1[j-1]:
            ans = recurse(i-1, j-1, replacement_cost=replacement_cost)
            
        # If last letters differ
        else:
            sub_cost = recurse(i-1, j-1, replacement_cost=replacement_cost) + replacement_cost   # substitution cost
            ins_cost = recurse(i-1, j, replacement_cost=replacement_cost) + 1   # insertion cost
            del_cost = recurse(i, j-1, replacement_cost=replacement_cost) + 1   # deletion cost
            ans = min(sub_cost, ins_cost, del_cost)
        
        # Cache and return
        cache[(i,j)] = ans
        return ans
    return recurse(len(s2), len(s1), replacement_cost=replacement_cost)

####################################################################################



import os

# load and build
PATH = os.path.expanduser(r"~/Datasets/1000_common_english_words.txt")
PATH = os.path.expanduser(r"~/Datasets/10000words.txt")
with open(PATH, mode='rt', encoding='utf-8') as fr:
    vocabulary = fr.read().split('\n')

vec = Vectorizer(n_grams=(2,3))
X = vec.fit_transform(vocabulary, normalize=True)



# query
queries = ("musik", "gurl", "execushan", "peeple", "sheap", "teh", 
           "pahe", "camputar", "Lundan",
           "good", "perfect", "yes")

for q in queries:
    q = q.strip().lower()
    y = vec.transfrom(q, normalize=True)
    cosine_similarities = vec.cosine_similarities(query=y, data=X)
    
    threshold = sorted(cosine_similarities)[-300]    
    suggestions = [vocabulary[i] for i in range(len(cosine_similarities)) if cosine_similarities[i] > threshold and q[0]==vocabulary[i][0]]

    distances = [edit_distance(q, s, replacement_cost=1) for s in suggestions]
    threshold = sorted(distances)[min(len(distances)-1, 10)]
    
    suggestions = [(suggestions[i], distances[i]) for i in range(len(distances)) if distances[i] < threshold]
    suggestions = [t[0] for t in sorted(suggestions, key=lambda t : t[-1])][:3]
    suggestions = None if q.lower() in suggestions else suggestions
    
    print(q, suggestions)
