from gendiff import generate_diff as gd


def test1_json():
    answer = open('tests/fixtures/answer1.txt').read().rstrip()
    assert gd.generate_diff('tests/fixtures/filepath1.json', 'tests/fixtures/filepath2.json') == answer


def test2_json():
    answer = open('tests/fixtures/answer2.txt').read().rstrip()
    assert gd.generate_diff('tests/fixtures/filepath3.json', 'tests/fixtures/filepath4.json') == answer
