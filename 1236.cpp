class Solution {
public:

    vector<string> res;
    string hostname;

    string getHostname(string url) {
        int pos = min(url.size(), url.find('/', 7));
        return url.substr(7, pos-7);
    }

    void dfs(string curr, HtmlParser htmlParser, unordered_set<string>& visit) {
        visit.insert(curr);
        res.push_back(curr);
        for (string url : htmlParser.getUrls(curr)) {
            if (getHostname(url) == hostname && !visit.count(url)){
                dfs(url, htmlParser, visit);
            }
        }
    }

    vector<string> crawl(string startUrl, HtmlParser htmlParser) {
        unordered_set<string> visit;
        hostname = getHostname(startUrl);
        dfs(startUrl, htmlParser, visit);

        return res;
    }
};

class Solution {
public:
    vector<string> crawl(string startUrl, HtmlParser htmlParser) {
        const string& hostname = startUrl.substr(0, startUrl.find('/', 7));
        vector<string> res{startUrl};
        unordered_set<string> seen(res.cbegin(), res.cend());
        for (int i = 0; i < res.size(); i++) {
            string &url = res[i];
            for (const auto& child : htmlParser.getUrls(url)) {
                if (child.find(hostname) == string::npos || seen.count(child))
                    continue;
                res.push_back(child);
                seen.insert(child);
            }
        }
        return res;
    }
};