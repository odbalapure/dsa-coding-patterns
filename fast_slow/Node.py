from dataclasses import dataclass
from typing import Any

@dataclass
class LinkedListNode:
    value: Any
    next: 'LinkedListNode' = None
