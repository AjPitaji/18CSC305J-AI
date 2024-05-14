class BlockWorld:
    def __init__(self, n):
        self.table = [[] for _ in range(n)]  # Initialize table with n stacks

    def move(self, source, destination):
        if source == destination or not self.table[source]:
            return False
        block = self.table[source].pop()
        self.table[destination].append(block)
        return True

    def stack(self, source, destination):
        if source == destination or not self.table[source]:
            return False
        block = self.table[source][-1]
        if self.table[destination] and self.table[destination][-1] == block:
            return False  # Cannot stack on itself
        self.table[source].pop()
        self.table[destination].append(block)
        return True

    def unstack(self, source, destination):
        if source == destination or not self.table[source] or not self.table[destination]:
            return False
        block = self.table[source][-1]
        if self.table[destination] and self.table[destination][-1] != block:
            return False  # Cannot unstack from a different block
        self.table[destination].pop()
        self.table[source].append(block)
        return True


    def print_table(self):
        for i, stack in enumerate(self.table):
            print(f"Stack {i}: {stack}")

if __name__ == "__main__":
        bw = BlockWorld(3) # Create a block world with 3 stacks
        bw.table = [[3, 2, 1], [], []] # Initial configuration
        # Example operations
        bw.move(0, 2) # Move block from stack 0 to stack 2
        bw.stack(1, 2) # Stack block from stack 1 onto stack 2
        bw.unstack(0, 1) # Unstack block from stack 0 onto stack 1
        bw.print_table() # Print current table configuration   
