import re
from typing import Any


_VERSION_RE = re.compile(r"(\d+|[a-zA-Z]+)")


class LooseVersion:
    def __init__(self, v: str) -> None:
        self.vstring = str(v or "")
        parts = _VERSION_RE.findall(self.vstring)
        self._tokens: tuple[Any, ...] = tuple(
            int(part) if part.isdigit() else part.lower() for part in parts
        )
        numeric_tokens = [part for part in parts if part.isdigit()]
        self.version = [int(numeric_tokens[0])] if numeric_tokens else [0]

    def __repr__(self) -> str:
        return f"LooseVersion({self.vstring!r})"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, LooseVersion):
            return self._tokens == other._tokens
        return NotImplemented

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, LooseVersion):
            return self._tokens < other._tokens
        return NotImplemented

    def __le__(self, other: Any) -> bool:
        return self == other or self < other

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, LooseVersion):
            return self._tokens > other._tokens
        return NotImplemented

    def __ge__(self, other: Any) -> bool:
        return self == other or self > other
