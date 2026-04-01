class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(node) -> int:
            if parent[node] == node:
                return node
            else:
                true_parent = find(parent[node])
                parent[node] = true_parent
                return true_parent

        def union(a, b) -> bool:
            parent_a = find(a)
            parent_b = find(b)
            if parent_a == parent_b:
                return False
            else:
                if rank[parent_a] >= rank[parent_b]:
                    parent[parent_b] = parent[parent_a]
                    rank[parent_a]+=rank[parent_b]
                else:
                    parent[parent_a] = parent[parent_b]
                    rank[parent_b]+=rank[parent_a]

        n = len(accounts)
        parent = list(range(n))
        rank = [0] * n
        email_to_account = {}

        for account_id, account in enumerate(accounts): # second pass, combining intersecting email's account_id
            name, emails = account[0], account[1:]

            for email in emails:
                if email in email_to_account:
                    union(account_id, email_to_account[email])
                else:
                    email_to_account[email] = account_id
           

        emailGroup = defaultdict(list)
        for email, id in email_to_account.items():
            leader = find(id)
            emailGroup[leader].append(email)
        
        res = []

        for id, emails in emailGroup.items():
            res.append([accounts[id][0]] + sorted(emails))

        return res





