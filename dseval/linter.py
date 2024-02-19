from __future__ import annotations


class LintError:
    pass


class Linter:
    def lint(self, code: str) -> list[LintError]:
        raise NotImplementedError()
