import unittest
from gld_script_portfolio.calc_aniv_semana import *

class TestTypeAnalysis(unittest.TestCase):
    def test_yeartype(self):
        self.assertEqual(type_analysis(1600)[0],'Leap')
        self.assertEqual(type_analysis(1601)[0], 'Later')
        self.assertEqual(type_analysis(1602)[0], 'Middle')
        self.assertEqual(type_analysis(1603)[0], 'Previous')
        self.assertEqual(type_analysis(1700)[0], 'Anomalous')
        self.assertEqual(type_analysis(1900)[0], 'Anomalous')
        self.assertEqual(type_analysis(2000)[0], 'Leap')
        self.assertEqual(type_analysis(2099)[0], 'Previous')
        self.assertEqual(type_analysis(2100)[0], 'Anomalous')

    def test_index(self):
        self.assertEqual(type_analysis(1600)[1], 0)
        self.assertEqual(type_analysis(1601)[1], 1)
        self.assertEqual(type_analysis(1602)[1], 2)
        self.assertEqual(type_analysis(1603)[1], 3)
        self.assertEqual(type_analysis(1700)[1], 4)
        self.assertEqual(type_analysis(1900)[1], 4)
        self.assertEqual(type_analysis(2000)[1], 0)
        self.assertEqual(type_analysis(2099)[1], 3)
        self.assertEqual(type_analysis(2100)[1], 4)


class TestAnomalyIdentifier(unittest.TestCase):
    def test_boolean(self):
        """
        Tests whether the answer (first index content) of the method "anomaly_identifier"
        returns True or False correctly.
        :return:
        """
        self.assertTrue(anomaly_identifier(1899, 1901)[0])
        self.assertTrue(anomaly_identifier(1800, 1899)[0])
        self.assertTrue(anomaly_identifier(1900, 1999)[0])
        self.assertTrue(anomaly_identifier(1900, 2000)[0])
        self.assertTrue(anomaly_identifier(1901, 2100)[0])
        self.assertFalse(anomaly_identifier(1901, 2000)[0])
        self.assertFalse(anomaly_identifier(1901, 2099)[0])

    def test_values(self):
        """
        Tests whether the array "anomalies" (second index content) of the method "anomaly_identifier"
        returns its content correctly.
        :return:
        """
        self.assertListEqual(anomaly_identifier(1899, 1920)[1], [1900])
        self.assertListEqual(anomaly_identifier(1800, 1899)[1], [1800])
        self.assertListEqual(anomaly_identifier(1900, 2000)[1], [1900])
        self.assertListEqual(anomaly_identifier(2000, 2099)[1], [])
        self.assertListEqual(anomaly_identifier(1901, 2099)[1], [])
        self.assertListEqual(anomaly_identifier(1700, 2099)[1], [1700, 1800, 1900])
        self.assertListEqual(anomaly_identifier(1600, 2101)[1], [1700, 1800, 1900, 2100])


class TestWhatYearsContemporary(unittest.TestCase):
    def test_values(self):
        self.assertRaises(TypeError, what_years_contemporary, 1988, 3, 2030)  # First arg should be a list.
        # self.assertRaises(ValueError, what_years_contemporary, [1899], 3, 1910)  # Time span shouldn't have anomalies.
        self.assertListEqual(what_years_contemporary([1988], 3, 2030), [1988, 1994, 2005, 2011, 2016, 2022])
        self.assertListEqual(what_years_contemporary([1988], 1, 2030), [1988, 1993, 1999, 2010, 2016, 2021, 2027])
        self.assertListEqual(what_years_contemporary([1899], 1, 1900), [1899])


class TestWhatYearsComplete(unittest.TestCase):
    def test_values(self):

        self.assertListEqual(what_years_complete(1988, 3, 2030), [1988, 1994, 2005, 2011, 2016, 2022])
        self.assertListEqual(what_years_complete(1988, 1, 2030), [1988, 1993, 1999, 2010, 2016, 2021, 2027])
        self.assertListEqual(what_years_complete(1899, 3, 1920), [1899, 1905, 1911, 1916])
        self.assertListEqual(what_years_complete(1898, 3, 1920), [1898, 1904, 1910])
        self.assertListEqual(what_years_complete(1897, 3, 1920), [1897, 1909, 1915, 1920])
        self.assertListEqual(what_years_complete(1896, 3, 1920), [1896, 1903, 1908, 1914])
        # self.assertListEqual(what_years_complete(1895, 3, 1920), [1895, 1901, 1907, 1912, 1918]) ???????? Looping?
        self.assertListEqual(what_years_complete(1894, 3, 1920), [1894, 1900, 1906, 1917])
        self.assertListEqual(what_years_complete(1890, 3, 1920), [1890, 1902, 1913, 1919])

if __name__ == '__main__':
    unittest.main()

# help(unittest.TestCase)
