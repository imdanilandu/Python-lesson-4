import pytest
from string_utils import StringUtils
    
string = StringUtils()

# Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
# позитивные тесты
@pytest.mark.parametrize('text, result', [
    ('skypro', 'Skypro'),
    ('Skypro', 'Skypro'),
    ('sky_pro', 'Sky_pro'),
    ('sky pro', 'Sky pro'),
    (' skypro', ' skypro'),
    ('sKYPRO', 'SKYPRO'),
    ('1', '1')
    ])
def test_positive_capitalize(text, result):
    string = StringUtils()
    res = string.capitalize(text)
    assert res == result

# негативные тесты
@pytest.mark.xfail (strict = True)
@pytest.mark.parametrize('nottext, result', [
    ('', ''),
    (' ', ' '),
    (None, 'None'),
    (1, '1'),
    (True, 'True')
    ])
def test_negative_capitalize(nottext, result):
    string = StringUtils()
    res = string.capitalize(nottext)
    assert res == result

# Принимает на вход текст и удаляет пробелы в начале, если они есть
# позитивные тесты
@pytest.mark.parametrize('text, result', [
    (' skypro', 'skypro'),
    (' sky_pro', 'sky_pro'),
    (' sky pro', 'sky pro'),
    ('skypro', 'skypro'),
    (' 1', '1'),
    ])
def test_positive_trim(text, result):
    string = StringUtils()
    res = string.trim(text)
    assert res == result

# негативные тесты
@pytest.mark.xfail (strict = True)
@pytest.mark.parametrize('nottext, result', [
    ('', ''),
    (' ', ''),
    (None, 'None'),
    (1, '1'),
    (True, 'True')
    ])
def test_negative_trim(nottext, result):
    string = StringUtils()
    res = string.trim(nottext)
    assert res == result

# Принимает на вход текст с разделителем и возвращает список строк
# позитивные тесты
@pytest.mark.parametrize('text, delim, result', [
    ('a,b,c', ',', ['a', 'b', 'c']),
    ('1:2:3', ':', ['1', '2', '3']),
    ('sky-pro-1', '-', ['sky', 'pro', '1']),
    ('skypro', ',', ['skypro']),
    ('a,b,c', ':', ['a,b,c'])
    ])
def test_positive_to_list(text, delim, result):
    string = StringUtils()
    res = string.to_list(text, delim)
    assert res == result

# негативные тесты
@pytest.mark.xfail (strict = True)
@pytest.mark.parametrize('nottext, delim, result', [
    ('', ',', []),
    (' ', ':', []),
    (None, '-', []),
    (1, ',', ['1']),
    (True, ',', ['True'])
    ])
def test_negative_to_list(nottext, delim, result):
    string = StringUtils()
    res = string.to_list(nottext, delim)
    assert res == result

# Возвращает `True`, если строка содержит искомый символ и `False` - если нет
# позитивные тесты
@pytest.mark.parametrize('text, sym, result', [
    ('skypro', 's', True),
    ('Skypro', 'S', True),
    ('Skypro', 's', False),
    ('skypro', 'S', False),
    ('skypro', 'a', False),
    ('sky_pro', '_', True),
    ('sky pro', ' ', True),
    ('skypro', '', False),
    ('1', '1', True),
    ('1', '2', False)
    ])
def test_positive_contains(text, sym, result):
    string = StringUtils()
    res = string.contains(text, sym)
    assert res == result

# негативные тесты
@pytest.mark.xfail (strict = True)
@pytest.mark.parametrize('nottext, sym, result', [
    ('', '', True),
    (' ', ' ', True),
    (None, 'N', True),
    (1, '1', True),
    (True, 'T', True)
    ])
def test_negative_contains(nottext, sym, result):
    string = StringUtils()
    res = string.contains(nottext, sym)
    assert res == result

# Удаляет все подстроки из переданной строки
# позитивные тесты
@pytest.mark.parametrize('text, sym, result', [
    ('skypro', 's', 'kypro'),
    ('skypro', 'pro', 'sky'),
    ('sky_pro', '_', 'skypro'),
    ('sky pro', ' ', 'skypro'),
    ('skypro', '', 'skypro'),
    ('12', '1', '2')
    ])
def test_positive_delete_symbol(text, sym, result):
    string = StringUtils()
    res = string.delete_symbol(text, sym)
    assert res == result

# негативные тесты
@pytest.mark.xfail (strict = True)
@pytest.mark.parametrize('nottext, sym, result', [
    ('', '', ''),
    (' ', ' ', ''),
    (None, 'N', 'one'),
    (12, '1', '2'),
    (True, 'T', 'rue')
    ])
def test_negative_delete_symbol(nottext, sym, result):
    string = StringUtils()
    res = string.delete_symbol(nottext, sym)
    assert res == result

# Возвращает `True`, если строка начинается с заданного символа и `False` - если нет
# позитивные тесты
@pytest.mark.parametrize('text, sym, result', [
    ('skypro', 's', True),
    ('Skypro', 'S', True),
    ('skypro', 'S', False),
    ('Skypro', 's', False),
    ('skypro', 'p', False),
    ('_skypro', '_', True),
    (' skypro', ' ', True),
    ('skypro', '', False),
    ('12', '1', True)
    ])
def test_positive_starts_with(text, sym, result):
    string = StringUtils()
    res = string.starts_with(text, sym)
    assert res == result

# негативные тесты
@pytest.mark.xfail (strict = True)
@pytest.mark.parametrize('nottext, sym, result', [
    ('', '', True),
    (' ', ' ', True),
    (None, 'N', True),
    (12, '1', True),
    (True, 'T', True)
    ])
def test_negative_starts_with(nottext, sym, result):
    string = StringUtils()
    res = string.starts_with(nottext, sym)
    assert res == result

# Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет
# позитивные тесты
@pytest.mark.parametrize('text, sym, result', [
    ('skypro', 'o', True),
    ('skyprO', 'O', True),
    ('skypro', 'O', False),
    ('kyprO', 'o', False),
    ('skypro', 'p', False),
    ('skypro_', '_', True),
    ('skypro ', ' ', True),
    ('skypro', '', False),
    ('12', '2', True)
    ])
def test_positive_end_with(text, sym, result):
    string = StringUtils()
    res = string.end_with(text, sym)
    assert res == result

# негативные тесты
@pytest.mark.xfail (strict = True)
@pytest.mark.parametrize('nottext, sym, result', [
    ('', '', True),
    (' ', ' ', True),
    (None, 'e', True),
    (12, '2', True),
    (True, 'e', True)
    ])
def test_negative_end_with(nottext, sym, result):
    string = StringUtils()
    res = string.end_with(nottext, sym)
    assert res == result

# Возвращает `True`, если строка пустая и `False` - если нет
# позитивные тесты
@pytest.mark.parametrize('text, result', [
    ('', True),
    (' ', True),
    ('skypro', False),
    ('_', False),
    ('1', False)
    ])
def test_positive_is_empty(text, result):
    string = StringUtils()
    res = string.is_empty(text)
    assert res == result

# негативные тесты
@pytest.mark.xfail (strict = True)
@pytest.mark.parametrize('nottext, result', [
    (None, False),
    (1, False),
    (True, False)
    ])
def test_negative_is_empty(nottext, result):
    string = StringUtils()
    res = string.is_empty(nottext)
    assert res == result

# Преобразует список элементов в строку с указанным разделителем   
# позитивные тесты
@pytest.mark.parametrize('text, join, result', [
    (['sky', 'pro'], ',', 'sky,pro'),
    (['sky', 'pro'], '_', 'sky_pro'),
    (['sky', 'pro'], ' ', 'sky pro'),
    (['sk', 'pro'], 'y', 'skypro'),
    ([None, ''], ',', 'None,'),
    ([1, 2], ':', '1:2'),
    ([True, False], '-', 'True-False')
    ])
def test_positive_list_to_string(text, join, result):
    string = StringUtils()
    res = string.list_to_string(text, join)
    assert res == result

# негативные тесты
@pytest.mark.xfail (strict = True)
@pytest.mark.parametrize('nottext, join, result', [
    (['', ''], ',', ','),
    ([' ', ' '], ',', ' , '),
    ([], ',', '')
    ])
def test_negative_list_to_string(nottext, join, result):
    string = StringUtils()
    res = string.list_to_string(nottext, join)
    assert res == result