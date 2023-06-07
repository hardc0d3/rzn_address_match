
from methods.levenshtein_distance import LevenshteinDistUtil

INPUT_CSV = 'resources/ResTecDevTask-sample_input_v1.1_EN.csv'
LEVENSHTEIN_METHOD_RATIO_LIMIT = 0.656789
EXPECTED_RESULT = ['Dragan Doichinov, Ilona Ilieva, Ivan Draganov',
                   'Elena Krasna, Elon Krasnii',
                   'Frieda Müller',
                   'Ivan Grozni',
                   'Leon Wu, Li Deng']


def fake_some():
    pass


def test_method_levenshtein_distance():
    ld = LevenshteinDistUtil(acceptance_ratio_limit=LEVENSHTEIN_METHOD_RATIO_LIMIT)
    r = ld.from_csv(input_csv=INPUT_CSV)
    assert EXPECTED_RESULT == r




