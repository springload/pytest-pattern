import re


def pattern(pat, flags=0):
    return RegexPattern(pat, flags)


def startswith(prefix):
    return pattern(f"^{re.escape(prefix)}")


def endswith(suffix):
    return pattern(f"{re.escape(suffix)}$")


def contains(text):
    return pattern(re.escape(text))


class RegexPattern:
    """Assert that a given string matches a pattern.

    Essentially wrapps a compiled re pattern and calls match(other) when testing for
    equality. Use like:

    >>> RegexPattern(r'text to match') == "A string containing text to match."
    True

    A RegexPattern instance cen be used when constructing more complex expected types to
    match against with pytest. For example:

    ```
    assert [1, False, 'Foo(id=123)'] == [1, False, RegexPattern(r'Foo\(id=\d+\)')]
    ```
    """

    def __init__(self, pattern, flags=0):
        self._matcher = re.compile(pattern, flags)

    def __eq__(self, actual):
        return bool(self._matcher.search(actual))

    # def __ne__(self, actual):
    #     return not bool(self == actual)

    def __repr__(self):
        return self._matcher.pattern
