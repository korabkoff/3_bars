import unittest
from bars import load_json_data, parse_args, get_user_coordinates,\
    get_biggest_bar, get_smallest_bar, get_closest_bar, get_gps_distance
# import bars

class LoadJsonDataTestCase(unittest.TestCase):
    def test_normal_json(self):
        json_content = load_json_data('test.json')
        self.assertEqual(json_content, {u'wins': [], u'name': u'\u041c\u0430\u0439'})

    def test_JSON_none_passed(self):
        json_content = load_json_data(None)
        self.assertIsNone(json_content)

    def test_JSON_no_File(self):
        json_content = load_json_data('no_file.json')
        self.assertIsNone(json_content)

    def test_not_a_json(self):
        with self.assertRaises(ValueError):
            load_json_data('README.md')

    def test_empty_json(self):
        with self.assertRaises(ValueError):
            load_json_data('empty.json')


class ParseArgsTestCase(unittest.TestCase):

    def test_filepath_arg_given(self):
        parser = parse_args(['test.json'])
        self.assertEqual(parser.filepath.name, 'test.json')

    def test_No_Such_File(self):
        with self.assertRaises(SystemExit):
            parse_args(['test.jso'])

    def test_No_Arg(self):
        with self.assertRaises(SystemExit):
            parse_args([])

    def test_2_args(self):
        with self.assertRaises(SystemExit):
            parse_args(['test.json 234'])


class GetClosestBarTestCase(unittest.TestCase):

    def test_get_user_coordinates_valid_input_grase(self):
        bars_data = load_json_data('data.json')
        user_latitude, user_longitude = 55.7849966, 37.466474
        closest_bar = get_closest_bar(bars_data, user_latitude, user_longitude)
        self.assertEqual(closest_bar, 'Грэйс Бар')


    def test_get_user_coordinates_valid_input_red_car(self):
        bars_data = load_json_data('data.json')
        user_latitude, user_longitude = 55.70111462948684, 37.638228501070095
        closest_bar = get_closest_bar(bars_data, user_latitude, user_longitude)
        self.assertEqual(closest_bar, 'Спорт бар «Красная машина»')

    def test_get_user_coordinates_nones_coordinates_input(self):
        bars_data = load_json_data('data.json')
        user_latitude, user_longitude = None, None
        closest_bar = get_closest_bar(bars_data, user_latitude, user_longitude)
        self.assertIsNone(closest_bar)

    def test_get_user_coordinates_none_data_input(self):
        bars_data = None
        user_latitude, user_longitude = 55.70111462948684, 37.638228501070095
        closest_bar = get_closest_bar(bars_data, user_latitude, user_longitude)
        self.assertIsNone(closest_bar)

class GetGpsDistanceTestCase(unittest.TestCase):

    def test_get_gps_distance_valid_input(self):
        user_latitude, user_longitude = 37.638228501070095, 55.70111462948684
        ref_lat, ref_lon = 37.466474, 55.7849966
        distance = get_gps_distance(ref_lat, ref_lon, user_latitude, user_longitude)
        self.assertEqual(distance, 1215.2643418992445)

    def test_get_gps_distance_valid_equal_input(self):
        user_latitude, user_longitude = 55.70111462948684, 37.638228501070095
        ref_lat, ref_lon = 55.70111462948684, 37.638228501070095
        distance = get_gps_distance(ref_lat, ref_lon, user_latitude, user_longitude)
        self.assertEqual(distance, 0.0)

    def test_get_user_coordinates_none_data_input(self):
        ref_lat, ref_lon = 37.466474, 55.7849966
        user_latitude, user_longitude = None, None
        distance = get_gps_distance(ref_lat, ref_lon, user_latitude, user_longitude)
        self.assertIsNone(distance)

    def test_get_user_coordinates_none_user_input(self):
        ref_lat, ref_lon = None, None
        user_latitude, user_longitude = 37.638228501070095, 55.70111462948684
        distance = get_gps_distance(ref_lat, ref_lon, user_latitude, user_longitude)
        self.assertIsNone(distance)

if __name__ == '__main__':
    unittest.main()
