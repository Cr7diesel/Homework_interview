import pytest
from balancing import balance

fixtures = [('(((([{}]))))', 'сбалансировано'),
            ('[([])((([[[]]])))]', 'сбалансировано'),
            ('{()}', 'сбалансировано'),
            ('{{[()]}}', 'сбалансировано'),
            ('}{}', 'Не сбалансировано'),
            ('{{[(])]}}', 'Не сбалансировано'),
            ('[[{())}]', 'Не сбалансировано')]


@pytest.mark.parametrize('strings, expect_result', fixtures)
def test_balance(strings, expect_result):
    assert balance(strings) == expect_result
