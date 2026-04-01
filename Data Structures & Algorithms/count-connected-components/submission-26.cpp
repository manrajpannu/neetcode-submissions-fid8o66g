class Solution {
public:
    int find(int node, vector<int> &parents) 
    {
        int parent {parents[node]};

        if (parent == node)
        {
            return parent;
        };

        int true_parent {find(parent, parents)};
        parents[node] = true_parent;
        return true_parent;
        
    }
    bool _union(int node_a, int node_b, vector<int> &parents, vector<int> &rank)
    {

        int par_a = find(node_a, parents);
        int par_b = find(node_b, parents);

        if (par_a != par_b) {

            if (rank[node_a] >= rank[node_b])
            {
                parents[par_b] = par_a;
                rank[par_a] += rank[par_b];
            } else {
                parents[par_a] = par_b;
                rank[par_b] += rank[par_a];
            };

            return true;
        }
        return false;
    }

    int countComponents(int n, vector<vector<int>>& edges) {
        vector<int> pars {};
        vector<int> rank {};

        for (int i = 0; i < n; i++) 
        {
            pars.push_back(i);
            rank.push_back(1);
        };
        
        for (vector<int> edge: edges) 
        {
            if (_union(edge[0], edge[1], pars, rank)) {
                n--; 
            }
        };
        
        return n;


    }
};
