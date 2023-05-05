from hashlib import sha256

class MerkleTree:
    def __init__(self, leaves, hash_leaves = True):
        self.leaves = [sha256(leaf.encode()).hexdigest() if hash_leaves else leaf for leaf in leaves]
        if len(self.leaves) % 2 != 0:
            self.leaves.append(self.leaves[-1])
        self.levels = [self.leaves]
        while len(self.levels[-1]) > 1:
            level = self.levels[-1]
            nextLevel = []
            for i in range(0, len(level), 2):
                left = level[i]
                right = level[i + 1] if i + 1 < len(level) else left
                nextLevel.append(self.hash(left, right))
            self.levels.append(nextLevel)

    def hash(self, left, right):
        return sha256(left.encode() + right.encode()).hexdigest()

    def getRoot(self):
        return self.levels[-1][0]

    def getMerkleProof(self, hash):
        if hash not in self.levels[0]:
            return [],-1
        proof = []
        level = 0
        index = self.levels[0].index(hash)
        leaf_index = index
        while level < len(self.levels) - 1:
            siblingIndex = index + 1 if index % 2 == 0 else index - 1
            sibling = self.levels[level][siblingIndex]
            proof.append(sibling)
            index //= 2
            level += 1
        return proof,leaf_index

    def verifyMerkleProof(self, hash, index, proof):
        if proof == []:
            return False
        currentHash = hash
        for sibling in proof:
            if index % 2 == 0:
                currentHash = self.hash(currentHash, sibling)
            else:
                currentHash = self.hash(sibling, currentHash)
            index //= 2
        return currentHash == self.getRoot()
