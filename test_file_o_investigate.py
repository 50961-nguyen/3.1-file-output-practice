from file_o_investigate import main

file_contents = []


class MockFile:
    def __init__(self):
        self.data = ["1\n", "2\n", "3\n"]
    
    def read(self):
        assert False, "Plaese don't use read() function"

    def readline(self):
        assert False, "Please don't use readline() function"

    def readlines(self):
        assert False, "Plaese don't use readlines() function"
    
    def write(self):
        assert False, "Please don't use the write() function"
    
    def writelines(self, lst):
        global file_contents
        file_contents = lst
        return lst

class MockReader:
    def __init__(self, file_name, *args, **kwargs):
        assert file_name == "scores.txt", "Please write to a file called scores.txt"

    def __enter__(self):
        return MockFile()

    def __exit__(self, *args, **kwargs):
        pass


def test_file_o_investigate(monkeypatch):
    global file_contents
    inputs = ["n","User3","y","User2","y","User1","y"]
    monkeypatch.setattr("builtins.open", lambda file_name, *args, **kwargs: MockReader(file_name, *args, **kwargs))
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop())
    main()
    
    assert len(file_contents) == 3
    assert "\n" in file_contents[0], "Must append new line character (\\n) to score"
    assert "User2: " in file_contents[1], "Be sure to add the username to each score in scores.txt"
