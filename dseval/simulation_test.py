from .simulation import Environment


def test_execute():
    env = Environment()
    env.execute("a = 1")
    assert env.namespace["a"] == 1
    assert env.last_cell is not None
    assert env.last_cell.output["namespace_diff"]["a"] == "added"
    assert env.execute("a + 1") == 2
    assert env.execute("print(a + 2)\nraise ValueError('abc')") is None
    assert env.last_cell is not None
    assert env.last_cell.output["stream_output"] == "3\n"
    assert env.last_cell.output["error"]["ename"] == "ValueError"

    env.execute("a = 2")
    assert env.namespace["a"] == 2
    assert env.last_cell.output["namespace_diff"]["a"] == "replaced"


def test_execute_forbid():
    env = Environment()
    assert env.execute("while True: pass") is None
    assert env.last_exception is not None and "TimeLimitError" in env.last_exception

    env.execute("a = 2")
    assert env.execute("a + 2") == 4
    assert env.execute("a + 2", forbid_names=["a"]) is None
    assert env.last_exception is not None and "_Forbidden" in env.last_exception

    assert env.execute("a + 2", forbid_names=["b"]) == 4


def test_execute_namespace_diff():
    env = Environment()

    env.execute("import pandas as pd\ndf = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})")
    assert env.last_cell is not None
    assert env.last_cell.output["namespace_diff"]["df"] == "added"
    env.execute("df['c'] = df['a'] + df['b']")
    assert env.last_cell.output["namespace_diff"]["df"] == "updated"
    env.execute("df = df[['a', 'c']]")
    assert env.last_cell.output["namespace_diff"]["df"] == "replaced"
    env.execute("df.set_index('a', inplace=True)")
    assert env.last_cell.output["namespace_diff"]["df"] == "updated"
    env.execute("del df")
    assert env.last_cell.output["namespace_diff"]["df"] == "deleted"
