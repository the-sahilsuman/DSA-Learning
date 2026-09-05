class UnionFind:
    def __init__(self, size):
        self.parent=list(range(size))

    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x=self.find(x)
        root_y=self.find(y)
        if root_x!=root_y:
            self.parent[root_y]=root_x

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_id={}
        email_to_name={}
        size=0

        for acc in accounts:
            name=acc[0]
            for email in acc[1:]:
                if email not in email_to_id:
                    email_to_id[email]=size
                    email_to_name[email]=name
                    size+=1

        uf=UnionFind(size)

        for acc in accounts:
            first_email=acc[1]
            for email in acc[2:]:
                uf.union(email_to_id[first_email],email_to_id[email])

        root_to_emails=defaultdict(list)
        for email,email_id in email_to_id.items():
            root_id=uf.find(email_id)
            root_to_emails[root_id].append(email)

        print(uf.parent)
        print(email_to_id)
        print(email_to_name)
        print(root_to_emails)

        result=[]
        for emails in root_to_emails.values():
            name=email_to_name[emails[0]]
            result.append([name]+sorted(emails))

        return result
