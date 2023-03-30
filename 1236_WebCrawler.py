from collections import deque

class Solution:

    def getHostName(self, url: str) -> str:
        return url.split('/')[2]
    
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> list[str]:

        search = set()
        hostName = startUrl.replace('http://' , '')
        hostName = hostName.split('/')[0]

        q = deque()
        q.append(startUrl)
        search.add(startUrl)

        while len(q):
            curr = q.popleft()
            urls = htmlParser.getUrls(curr)
            for url in urls:
                if url not in search and hostName == self.getHostName(url):
                    q.append(url)
                    search.add(url)
        return search
    
class Solution:
    visit = set()
    hostName = ''

    def getHostName(self, url: str) -> str:
        return url.split('/')[2]
    
    def dfs(self, curr: str, htmlParser: 'HtmlParser'):
        urls = htmlParser.getUrls(curr)
        self.visit.add(curr)
        for url in urls:
            if url not in self.visit and self.getHostName(url) == self.hostname:
                self.dfs(url, htmlParser)
        return self.visit

    
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> list[str]:

        self.visit = set()
        self.hostname = self.getHostName(startUrl)
        self.dfs(startUrl, htmlParser)
        return self.visit