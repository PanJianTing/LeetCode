class Solution:
    def simplifyPath(self, path: str) -> str:

        paths = path.split('/')
        directory = []

        for p in paths:
            if len(p) > 0:
                if ".." == p:
                    if len(directory) > 0:
                        directory.pop()
                elif '.' == p:
                    continue
                else:
                    directory.append(p)

        return '/' + '/'.join(directory)

Solution().simplifyPath("/a/./b/../../c/")
