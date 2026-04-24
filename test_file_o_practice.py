from file_o_practice import main
from datetime import datetime
file_contents = []


class MockFile:
    def __init__(self):
        self.data = ["1\n", "2\n", "3\n"]
    
    def read(self):
        assert False, "Plaese don't use read() function"

    def readline(self):
        assert False, "Please don't use readline() function"

    def readlines(self):
        assert False, "Please don't use readlines() function"
    
    def write(self, text):
        global file_contents
        file_contents.append(text)
      
        
    def writelines(self, lst):
        assert False, "Please don't use the writelines() function"

class MockReader:
    def __init__(self, file_name, mode):
        assert file_name.endswith(".py"), "Please ensure you add .py to the end of your filename"
        assert ( "explore" in file_name or
             "investigate" in file_name or
             "practice" in file_name or
             "make" in file_name), "Your file placed in one of the EIPM folders"
        assert mode is not None, "Please provide mode when opening the file"
        assert mode == "w", "Please open the file in write mode ('w')"

    def __enter__(self):
        return MockFile()

    def __exit__(self, *args, **kwargs):
        pass


def test_write_file(monkeypatch):
    global file_contents
    file_contents = []
    inputs = ["One sentence", "Author", "filename", "practice"]
    def mock_open(*args, **kwargs):
        assert len(args) >= 1, "open() must include a filename"
        file_name = args[0]
        mode = args[1] if len(args) >= 2 else kwargs.get("mode")
        return MockReader(file_name, mode)

    monkeypatch.setattr("builtins.open", mock_open)
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop())
    main()

    user_file = "".join(file_contents)
    today_date = datetime.today().strftime("%B %d, %Y")
    
    
    assert '"""\n' in user_file
    assert "author: Author\n" in user_file
    assert f"date: {today_date}\n" in user_file
    assert "One sentence\n" in user_file

    assert "def main():\n" in user_file
    assert "#input" in user_file.lower().replace(" ", "")
    assert "#processing" in user_file.lower().replace(" ", "")
    assert "#output" in user_file.lower().replace(" ", "")

    assert 'if __name__ == "__main__":\n' in user_file