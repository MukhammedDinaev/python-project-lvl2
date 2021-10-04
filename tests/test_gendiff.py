from gendiff import engine


def test1_json():
    answer = open('./tests/fixtures/answer1.txt').read().rstrip()
    result = engine.run_diff('tests/fixtures/filepath1.json', 'tests/fixtures/filepath2.json')
    assert result == answer


def test2_json():
    answer = open('./tests/fixtures/answer2.txt').read().rstrip()
    result = engine.run_diff('tests/fixtures/filepath3.json', 'tests/fixtures/filepath4.json')
    assert result == answer


def test1_yaml():
    answer = open('./tests/fixtures/answer1.txt').read().rstrip()
    result = engine.run_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml')
    assert result == answer


def test2_yaml():
    answer = open('./tests/fixtures/answer2.txt').read().rstrip()
    result = engine.run_diff('tests/fixtures/file3.yaml', 'tests/fixtures/file4.yaml')
    assert result == answer


def test1_tree_json():
    answer = open('./tests/fixtures/answer3.txt').read().rstrip()
    result = engine.run_diff('tests/fixtures/filetree1.json', 'tests/fixtures/filetree2.json')
    assert result == answer


def test1_tree_yaml():
    answer = open('./tests/fixtures/answer3.txt').read().rstrip()
    result = engine.run_diff('tests/fixtures/filetree1.yaml', 'tests/fixtures/filetree2.yaml')
    assert result == answer


def test2_tree_json():
    answer = open('./tests/fixtures/answer4.txt').read().rstrip()
    result = engine.run_diff('tests/fixtures/filetree1.json', 'tests/fixtures/filetree2.json', 'plain')
    assert result == answer


def test2_tree_yaml():
    answer = open('./tests/fixtures/answer4.txt').read().rstrip()
    result = engine.run_diff('tests/fixtures/filetree1.yaml', 'tests/fixtures/filetree2.yaml', 'plain')
    assert result == answer

def test1_treeyaml():
    answer = open('./tests/fixtures/answer3.txt').read().rstrip()
    result = engine.run_diff('tests/fixtures/filetree1.yaml', 'tests/fixtures/filetree2.yaml')
    assert result == answer
