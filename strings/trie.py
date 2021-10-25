import re


Char = str


class Node:
    """Primitive building block for trie.

    Can hold one-character string for pattern symbol.

    Attributes:
        _symbol: holding character value.
        _children: link to children which is also Node.
    """

    # Regex pattern representing symbol value's restriction.
    SYMBOLS = re.compile('([a-z]{1}|[0-9]+)')
    # Reserved character for representing root Node.
    EMPTY = ' ' 

    def __init__(self, symbol: Char):
        """Accepts only one character defined as pattern at SYMBOLS.
        """
        if not (Node.SYMBOLS.match(symbol) or symbol == Node.EMPTY):
            msg = "symbol must be alphaneumeric or empty character"
            raise RuntimeError(msg)

        self._symbol: Char = symbol
        self._children: dict[Char, 'Node'] = {}

    def has_child(self, symbol: Char) -> bool:
        """Return if this Node has child whose _symbol is symbol.
        """
        return symbol in self._children

    def child_of(self, symbol: Char) -> 'Node':
        """Get Node object if this object has child whose _symbol is given one.
        """
        if not self.has_child(symbol):
            raise RuntimeError(f'no corresponding child: symbol={symbol}')
        return self._children[symbol]

    def append(self, node: 'Node'):
        """Append node to _children.
        """
        symbol = node.symbol()
        if self.has_child(symbol):
            raise RuntimeError(f'given child already exists: symbol={symbol}')
        self._children[symbol] = node
        return self

    def symbol(self):
        return self._symbol

    def is_leaf(self):
        return not bool(self._children)

    @staticmethod
    def empty():
        return Node(Node.EMPTY)

    @staticmethod
    def of(symbol):
        return Node(symbol)

    @staticmethod
    def chain_head(symbols):
        """return n[s] -> n[y] -> n[m] -> n[b] -> n[o] -> n[l] -> [s].
        where n represent Node object and -> represent _children link
        """
        if len(symbols) == 0:
            return Node.empty()
        nodes = map(Node.of, symbols)
        # chaining
        for i in range(0, len(nodes)-1):
            nodes[i].append(nodes[i+1])
        return nodes[0]


def construct_trie(patterns):
    """Constructing trie from specified patterns and returning
    root of its trie.
    """
    root = Node.empty()
    for pattern in patterns:
        curr = root
        for i, symbol in enumerate(pattern):
            if curr.has_child(symbol):
                curr = curr.child_of(symbol)
            else:
                to_be_added = Node.chain_head(pattern[i:])
                curr = curr.append(to_be_added)
    return root


def prefix_trie_matching(text, trie):
    """Check if given text matches pattern represented as trie node.
    """
    if not text:
        return text
    sym_iter = iter(text)
    curr_sym = next(sym_iter, False)
    v = trie
    while curr_sym:
        # End checking
        if v.is_leaf():
            return True
        # Continue checking
        elif v.has_child(curr_sym):
            v = v.child_of(curr_sym)
            curr_sym = next(sym_iter, False)
        else:
            return False
    return False


def trie_matching(whole_text, trie):
    result = False
    # Sliding head of whole_text's substring
    for i in range(len(whole_text)):
        head_truncated_text = whole_text[i:]
        result = prefix_trie_matching(head_truncated_text, trie)
    return result
