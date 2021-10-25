import re
from typing import List


Char = str


class Node:
    """Primitive building block for trie.

    Can hold one-character string for pattern symbol.

    Attributes:
        _symbol: holding character value.
        _children: link to children which is also Node.
    """

    # Regex pattern representing symbol value's restriction.
    SYMBOLS = re.compile('[a-z]{1}')
    # Representing text's suffix's position.
    NUMBERS = re.compile('[0-9]+')
    # Reserved character for representing root Node.
    EMPTY = ' '

    @staticmethod
    def acceptable(symbol):
        is_for_value = Node.SYMBOLS.match(symbol)
        if is_for_value:
            return True
        is_for_position = Node.NUMBERS.match(symbol)
        if is_for_position:
            return True
        is_for_root = symbol is Node.EMPTY
        if is_for_root:
            return True
        return False

    def __init__(self, symbol: Char):
        """Accepts only one character defined as pattern at SYMBOLS.
        """
        if not Node.acceptable(symbol):
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


def append_symbols(node: Node, symbols: str):
    curr = node
    for i, symbol in enumerate(symbols):
        if curr.has_child(symbol):
            curr = curr.child_of(symbol)
        else:
            to_be_added = Node.chain_head(symbols[i:])
            curr = curr.append(to_be_added)


def construct_trie(patterns: List[str]) -> Node:
    """Constructing trie from specified patterns and returning
    root of its trie.
    """
    root = Node.empty()
    for pattern in patterns:
        append_symbols(root, pattern)
    return root


def prefix_trie_matching(text: str, trie: Node) -> bool:
    """Check if given text matches pattern represented as trie node.
    When source text retrieving pattern trie reaches leaf, it means
    that text mathces patterns.
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


def trie_matching(whole_text, trie) -> bool:
    result = False
    # Sliding head of whole_text's substring
    for i in range(len(whole_text)):
        head_truncated_text = whole_text[i:]
        result = prefix_trie_matching(head_truncated_text, trie)
    return result


def construct_incomplete_suffix_trie(text: str) -> Node:
    """Constructing suffix trie from source text beeing checked by pattern.
    Memory inefficient & simple implementation.
    """
    root = Node.empty()
    for i in range(len(text)):
        # Variable i represents position of suffix at text.
        suffix: str = text[i:] + str(i)
        append_symbols(root, suffix)
    return root
