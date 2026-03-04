class WordNode:
    def __init__(self):
        self.children = {}
        self.wordEnd = False

class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = WordNode()
            curr = curr.children[c]
        curr.wordEnd = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                if c not in curr.children:
                    return False
                curr = curr.children[c]
            return curr.wordEnd

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)