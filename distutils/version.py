# Compatibility shim for environments where stdlib 'distutils' is removed.
# Only provides what undetected_chromedriver expects: LooseVersion with .vstring and .version.
import re
from typing import Any, List


_VERSION_RE = re.compile(r"(\d+|[a-zA-Z]+)")


class LooseVersion:
    def __init__(self, v: str) -> None:
        if v is None:
            v = ""
        self.vstring = str(v)

        parts = _VERSION_RE.findall(self.vstring)
        token_list: List[Any] = []
        numeric_tokens: List[int] = []

        for p in parts:
            if p.isdigit():
                num = int(p)
                token_list.append(num)
                numeric_tokens.append(num)
            else:
                token_list.append(p.lower())

        # undetected_chromedriver does: release.version[0]
        # so ensure .version is present and indexable.
        if numeric_tokens:
            self.version = [numeric_tokens[0]]
        else:
            self.version = [0]

        self._tokens = tuple(token_list)

    def __repr__(self) -> str:
        return f"LooseVersion({self.vstring!r})"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, LooseVersion):
            return self._tokens == other._tokens
        return False

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
