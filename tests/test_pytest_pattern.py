import re

from pytest_pattern import pattern, startswith, contains, endswith


def test_empty():
    assert pattern(r"") == ""
    assert not pattern(r"") != ""


def test_full_match(faker):
    text = faker.sentence()
    assert pattern(re.escape(text)) == text
    assert not pattern(re.escape(text)) != text


def test_beginning(faker):
    text = faker.sentence()
    prefix = re.escape(text[:len(text)//2])
    suffix = re.escape(text[-len(text)//2:])

    assert pattern(f"{prefix}") == text
    assert pattern(f"^{prefix}") == text
    assert pattern(f"^{suffix}") != text


def test_middle(faker):
    text = faker.sentence()
    center = re.escape(text[len(text)//4:-len(text)//4])

    assert pattern(f"{center}") == text


def test_ending(faker):
    text = faker.sentence()
    prefix = re.escape(text[:len(text)//2])
    suffix = re.escape(text[-len(text)//2:])

    assert pattern(f"{suffix}") == text
    assert pattern(f"{suffix}$") == text
    assert pattern(f"{prefix}$") != text


def test_multi_line(faker):
    text = "\n".join(faker.sentences())
    assert pattern(re.escape(text)) == text
    assert not pattern(re.escape(text)) != text


def test_re_pattern():
    text = "A test string to match"

    assert pattern(f"test.*match") == text


def test_constructor_match(faker):
    text = f'Some message about Foo(id={faker.pyint()}, val="{faker.pystr()}") to match'

    assert pattern(r'Foo\(id=\d+, val="\w+"\)') == text


def test_startswith(faker):
    text = faker.sentence()
    prefix = text[:len(text)//2]
    suffix = text[-len(text)//2:]

    assert startswith(prefix) == text
    assert startswith(suffix) != text


def test_contains(faker):
    text = faker.sentence()
    center = text[len(text)//4:-len(text)//4]

    assert contains(center) == text


def test_endswith(faker):
    text = faker.sentence()
    prefix = text[:len(text)//2]
    suffix = text[-len(text)//2:]

    assert endswith(suffix) == text
    assert endswith(prefix) != text


def test_within_containers(faker):
    text = faker.sentence()
    prefix = text[:len(text)//2]
    middle = text[len(text)//4:-len(text)//4]
    suffix = text[-len(text)//2:]

    assert [startswith(prefix), endswith(suffix), {'d': contains(middle)}] == [text, text, {'d': text}]
