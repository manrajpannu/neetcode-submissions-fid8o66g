class SegmentTree:
    def __init__(self, N):
        self.n = N
        self.tree = [float('inf')] * (4 * N)
        self.lazy = [float('inf')] * (4 * N)

    def propagate(self, treeidx, lo, hi):
        if self.lazy[treeidx] != float('inf'):
            self.tree[treeidx] = min(self.tree[treeidx], self.lazy[treeidx])
            if lo != hi:
                self.lazy[2 * treeidx + 1] = min(self.lazy[2 * treeidx + 1], self.lazy[treeidx])
                self.lazy[2 * treeidx + 2] = min(self.lazy[2 * treeidx + 2], self.lazy[treeidx])
            self.lazy[treeidx] = float('inf')

    def update(self, treeidx, lo, hi, left, right, val):
        self.propagate(treeidx, lo, hi)
        if lo > right or hi < left:
            return
        if lo >= left and hi <= right:
            self.lazy[treeidx] = min(self.lazy[treeidx], val)
            self.propagate(treeidx, lo, hi)
            return
        mid = (lo + hi) // 2
        self.update(2 * treeidx + 1, lo, mid, left, right, val)
        self.update(2 * treeidx + 2, mid + 1, hi, left, right, val)
        self.tree[treeidx] = min(self.tree[2 * treeidx + 1], self.tree[2 * treeidx + 2])

    def query(self, treeidx, lo, hi, idx):
        self.propagate(treeidx, lo, hi)
        if lo == hi:
            return self.tree[treeidx]
        mid = (lo + hi) // 2
        if idx <= mid:
            return self.query(2 * treeidx + 1, lo, mid, idx)
        else:
            return self.query(2 * treeidx + 2, mid + 1, hi, idx)

    def update_range(self, left, right, val):
        self.update(0, 0, self.n - 1, left, right, val)

    def query_point(self, idx):
        return self.query(0, 0, self.n - 1, idx)

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        st = SegmentTree(10000)
        def size_of_interval(interval):
            l, r = interval
            return r - l + 1

        intervals.sort(key=size_of_interval, reverse=True)

        for l, r in intervals:
            st.update_range(l, r, r - l + 1)
        res = []
        for query in queries:
            answer = st.query_point(query)
            if answer == float("inf"):
                answer = -1
            res.append(answer)
        
        return res

