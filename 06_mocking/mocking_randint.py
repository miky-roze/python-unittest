import random
from unittest.mock import patch

# ************************************************

for _ in range(5):
    print(random.randint(1, 6))

with patch('random.randint') as mocked_randint:
    mocked_randint.return_value = 5
    for _ in range(5):
        print(random.randint(1, 6))

for _ in range(5):
    print(random.randint(1, 6))


# *************************************************

def get_value():
    return random.randint(1, 6)


@patch('random.randint')
def test_get_value(mocked_randint):
    mocked_randint.return_value = 5
    result = get_value()
    return result


for _ in range(5):
    print('Mocked value: ', test_get_value())
    print('Random value: ', get_value())
