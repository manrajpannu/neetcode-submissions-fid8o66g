

class Solution {
public:

    int countComponents(int n, vector<vector<int>>& edges) {
        std::cout << __cplusplus;
        std::unordered_set<int> visited {};
        std::unordered_map<int, vector<int>> graph {};

        for (vector<int> edge : edges) 
        {
            int a { edge[0] };
            int b { edge[1] }; 
            
            vector<int> &a_list {graph[a]};
            vector<int> &b_list {graph[b]};
            a_list.push_back(b);
            b_list.push_back(a);
        };

        

        int res {};
        for (int i = 0; i<n; i++) 
        {
            if (!visited.count(i) )
            {
                dfs(i, visited, graph);
                res++;
            }
        };

        return res;
    }
    bool dfs(int node, std::unordered_set<int> &visited, std::unordered_map<int, vector<int>> &graph) 
    {
        if (visited.count(node) )
        {
            return false;
        }

        visited.insert(node);

        vector<int> &neighbours = graph[node];

        for (int &neighbour: neighbours)
        {
            dfs(neighbour, visited, graph);

        }

        return true;
    }
};
