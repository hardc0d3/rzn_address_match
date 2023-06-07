from unittest import mock
from methods.google_geocode import GoogleGeocodeUtil

INPUT_CSV = 'resources/ResTecDevTask-sample_input_v1.1_EN.csv'
EXPECTED_RESULT = ['Dragan Doichinov, Ilona Ilieva, Ivan Draganov',
                   'Elena Krasna, Elon Krasnii',
                   'Frieda Müller',
                   'Ivan Grozni',
                   'Leon Wu, Li Deng']


def fake_geocode(*args, **kwargs):
    place__id = {
        'st. Shipka 34, 1000 Sofia, Bulgaria': 1,
        '1 Guanghua Road, Beijing, China 100020': 2,
        '34 Shipka Street, Sofia, Bulgaria': 1,
        'Shipka Street 34, Sofia, Bulgaria': 1,
        '1 Guanghua Road, Chaoyang District, Beijing, P.R.C 100020': 2,
        'Konrad-Adenauer-Strasse 7, 60313 Frankfurt am Main, Germany': 3,
        'Horodotska street, 273, sq. 640, 34151, Chernihiv, Ternopil region, Ukraine': 4,
        'sq. Stryyska, 39, sq. 646, 38967, Kryvyi Rih, Cherkasy Region, Ukraine': 5,
        'Ukraine, 34151, Horodotska str., 273, nh. 646, Chernigiv, Ternopil region': 4,
    }
    _, query = args
    return [{'place_id': place__id[query]}]


@mock.patch("googlemaps.Client.geocode", fake_geocode)
def test_method_goolegeocode():
    gl = GoogleGeocodeUtil(api_key='AIza')
    r = gl.from_csv(input_file_name=INPUT_CSV, have_header=False)
    assert r == EXPECTED_RESULT
