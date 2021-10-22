import re


class Node:
    SYMBOLS = re.compile('[a-z]{1}')
    EMPTY = ' '

    def __init__(self, symbol):
        if not (Node.SYMBOLS.match(symbol) or symbol == Node.EMPTY):
            raise RuntimeError("symbol must be 1 character string")
        self._symbol = symbol
        self._children = {}

    def has_child_of(self, symbol):
        return symbol in self._children

    def child_of(self, symbol):
        if not self.has_child_of(symbol):
            raise RuntimeError(f'no corresponding child: symbol={symbol}')
        return self._children[symbol]

    def append(self, node):
        symbol = node.symbol()
        if self.has_child_of(symbol):
            raise RuntimeError(f'given child already exists: symbol={symbol}')
        self._children[symbol] = node
        return self

    def symbol(self):
        return self._symbol

    @staticmethod
    def empty():
        return Node(Node.EMPTY)

    @staticmethod
    def of(symbol):
        return Node(symbol)

    @staticmethod
    def chain_head(symbols):
        if len(symbols) == 0:
            raise RuntimeError("given symbols is empty string")
        nodes = map(Node.of, symbols)
        # chaining
        for i in range(0, len(nodes)-1):
            nodes[i].append(nodes[i+1])
        return nodes[0]


def construct_trie(patterns):
    root = Node.empty()
    for pattern in patterns:
        curr = root
        for i, symbol in enumerate(pattern):
            if curr.has_child_of(symbol):
                curr = curr.child_of(symbol)
            else:
                to_be_added = Node.chain_head(pattern[i:])
                curr = curr.append(to_be_added)
    return root
