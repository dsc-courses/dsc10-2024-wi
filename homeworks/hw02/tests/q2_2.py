test = {   'name': 'q2_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> callable(extract_year_as_int) # Make sure your function name is correct.\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> import numbers\n>>> isinstance(extract_year_as_int('Sep 15, 2015'), numbers.Integral)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> result = extract_year_as_int('Sep 15, 2015')\n>>> (result >= 1980) and (result <= 2023)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
