test = {   'name': 'q7_8',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(revenue_by_genre, bpd.DataFrame) and revenue_by_genre.shape == (12, 1)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> 'Adventure' in revenue_by_genre.index\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> int(revenue_by_genre.get('adjusted_gross_millions').iloc[4] * 10 ** 3 % 10 ** 2) == 67 # Try again!\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
