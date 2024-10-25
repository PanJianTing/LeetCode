class TrieNode:
        def __init__(self, val = ''):
            self.val = val
            self.children = {}
            self.is_end = False

class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort(key=lambda x: len(x))
        folder_set = set()

        for f in folder:
            cur = ''
            is_sub = False
            for sub_f in f.split('/')[1:]:
                cur += '/'+sub_f
                if cur in folder_set:
                    is_sub = True
                    break
            if is_sub == False:
                folder_set.add(f)
        return list(folder_set)
    

    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder_set = set(folder)
        res = []

        for f in folder:
            prefix = f
            is_sub = False

            while prefix:
                pos = prefix.rfind('/')
                if pos == -1:
                    break
                prefix = prefix[:pos]
                if prefix in folder_set:
                    is_sub = True
                    break
            if is_sub == False:
                res.append(f)
        return res
    
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        N = len(folder)
        folder.sort()
        res = [folder[0]]

        for i in range(1, N):
            last = res[-1]

            if folder[i].startswith(last+'/') == False:
                res.append(folder[i])
        
        return res
    

        
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        root = TrieNode()
        res = []

        for f in folder:
            cur = root
            for f in f.split('/'):
                if f == "":
                    continue
                    
                if f not in cur.children:
                    cur.children[f] = TrieNode()
                cur = cur.children[f]
            
            cur.is_end = True

        for f in folder:
            cur = root
            all_f = f.split('/')[1:]
            N = len(all_f)
            is_sub = False
            for i in range(N):
                cur = cur.children[all_f[i]]

                if cur.is_end and i != N-1:
                    is_sub = True
                    break

            if is_sub == False:
                res.append(f)
        return res



                

print(Solution().removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))

