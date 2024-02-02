test = {   'name': 'q1_3',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> isinstance(avg_age,bpd.DataFrame) and avg_age.shape == (606, 3) and 'Average_Age' in avg_age.columns and baby.shape == (314767, 5) # Don't change "
                                               'the original baby DataFrame.\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.isclose(avg_age[(avg_age.get('Name') == 'Alexander') & (avg_age.get('Gender') == 'F')].get('Average_Age').iloc[0], 33.33983402489626)\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> int(avg_age.get('Average_Age').mean()) % 10 == 2 # Try again!\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
