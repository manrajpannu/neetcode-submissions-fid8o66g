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
        id_to_name = {}

        for account_id, account in enumerate(accounts): # first pass, set each email to its account_id
            name, emails = account[0], account[1:]
            for email in emails:
                email_to_account[email] = account_id
            id_to_name[account_id] = name
            rank[account_id] = len(emails)

        for account_id, account in enumerate(accounts): # second pass, combining intersecting email's account_id
            name, emails = account[0], account[1:]

            intersecting_accounts = set()
            for email in emails:
                if email in email_to_account:
                    intersecting_accounts.add(email_to_account[email])
            
            list_intersection = list(intersecting_accounts)
            for i in range(len(list_intersection)-1):
                a, b = list_intersection[i], list_intersection[i+1]
                union(a, b)
                
            


        # emails -> account_numbers
        # we know each account_id's true name

        trueid_to_emails = defaultdict(list)

        for email in list(email_to_account.keys()):
            account_id = find(email_to_account[email])
            trueid_to_emails[account_id].append(email)
        
        res = []
        for id in list(trueid_to_emails.keys()):
            emails = trueid_to_emails[id]
            emails.sort()
            res.append([])
            res[-1].append(id_to_name[id])
            res[-1]+=emails
        return res





