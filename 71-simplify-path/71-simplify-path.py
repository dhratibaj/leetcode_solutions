class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        for p in path.split('/'):
            if p in {'', '.'}:
                continue  
            if s and p == '..':
                s.pop()
            if p != '..':
                s.append(p)
        return '/' + '/'.join(s)