class TrieNode:
    def __init__(self):
        self.children = {} # a set of children - 26 alphabets
        self.endOfWord = False

# Time complexity: O(n) where n is the length of the word being inserted, searched, or checked for prefix. 
# This is because in the worst case, we may have to traverse through all characters of the word to insert it, 
# search for it, or check for its prefix in the Trie.
# Space complexity: O(n) where n is the length of the word being inserted. 
# This is because in the worst case, we may have to create a new TrieNode for each character in the word, 
# resulting in a space complexity proportional to the length of the word. 
# However, if we are searching for a word or checking for a prefix, the space complexity is O(1) 
# since we are not creating any new nodes and only traversing through existing nodes in the Trie.

class Trie:

    def __init__(self):
        # we initialize to empty Trie Node 
        # since root just points to children
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)