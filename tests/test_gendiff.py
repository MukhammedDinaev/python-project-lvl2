from gendiff import generate_diff as gd
import json


def test_gen_diff():
    answer = open('tests/fixtures/answer1.json')
    answer = json.dumps(json.load(answer), indent=4).replace('"', '').replace(',', '')
    assert gd.generate_diff('tests/fixtures/filepath1.json', 'tests/fixtures/filepath2.json') == answer


def test_gen_diff2():
    answer = open('tests/fixtures/answer2.json')
    answer = json.dumps(json.load(answer), indent=4).replace('"', '').replace(',', '')
    print(answer)
    print(gd.generate_diff('tests/fixtures/filepath3.json', 'tests/fixtures/filepath4.json'))
    assert gd.generate_diff('tests/fixtures/filepath3.json', 'tests/fixtures/filepath4.json') == answer
