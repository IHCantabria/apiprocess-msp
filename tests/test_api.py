import apiDebug
import msptools
import unittest
import json


class TestApiSCTools(unittest.TestCase):
    def setUp(self):
        self.bio_params = {
            "point": {"lon": -13.016, "lat": 28.486, "depth": 0},
            "specie": {
                "name": "European seabass",
                "salinity_min": 30,
                "salinity_max": 40,
                "temperature_min": 18,
                "temperature_max": 26,
            },
            "dates": {"ini": "2015-01-01", "end": "2015-03-01"},
        }
        self.wave_params = {
            "config": {
                "hs_min": 1,
                "hs_max": 5,
                "tp_min": 5,
                "tp_max": 14,
                "cge_min": 15,
            },
            "point": {"lon": -13.016, "lat": 28.486},
            "dates": {"start": "2015-01-01", "end": "2015-03-01",},
        }
        self.wind_params = {
            "config": {"hs_max": 5, "pow": 400},
            "point": {"lon": -7.229, "lat": 48.75895},
            "dates": {"start": "2010-02-01", "end": "2010-02-05",},
        }

    def test_biological(self):
        expected_result = 0.27
        app = apiDebug.app
        tester = app.test_client(self)
        response = (
            tester.post(
                "/msp/biological",
                data=json.dumps(self.bio_params),
                content_type="application/json",
            ),
        )
        status_code = response[0].status_code
        jsonResult = json.loads(response[0].data)
        result = round(float(jsonResult.get("value")), 3)

        self.assertEqual(status_code, 200)
        self.assertAlmostEqual(result, expected_result, delta=0.01)

    def test_biological_error(self):
        app = apiDebug.app
        tester = app.test_client(self)
        payload = {
            "point": {"lon": -13.016, "lat": 28.486},
            "dates": {"ini": "2015-01-01", "end": "2015-03-01"},
        }
        response = (
            tester.post(
                "/msp/biological",
                data=json.dumps(payload),
                content_type="application/json",
            ),
        )

        jsonResult = json.loads(response[0].data)
        exec_status = jsonResult.get("status")
        self.assertEqual(exec_status, "ERROR")

    def test_biological_land_exception(self):
        app = apiDebug.app
        tester = app.test_client(self)
        payload = {
            "point": {"lon": -2.445556, "lat": 42.47},
            "specie": {
                "name": "European seabass",
                "salinity_min": 30,
                "salinity_max": 40,
                "temperature_min": 18,
                "temperature_max": 26,
            },
            "dates": {"ini": "2015-01-01", "end": "2015-03-01"},
        }
        response = (
            tester.post(
                "/msp/biological",
                data=json.dumps(payload),
                content_type="application/json",
            ),
        )

        jsonResult = json.loads(response[0].data)

        exec_status = jsonResult.get("status")
        self.assertEqual(exec_status, "ERROR")
        exec_code = jsonResult.get("value")
        self.assertEqual(exec_code, -997)

    def test_wave_resource(self):
        expected_result = 0.7375
        app = apiDebug.app
        tester = app.test_client(self)
        response = (
            tester.post(
                "/msp/wave",
                data=json.dumps(self.wave_params),
                content_type="application/json",
            ),
        )
        status_code = response[0].status_code
        jsonResult = json.loads(response[0].data)
        result = round(float(jsonResult.get("value")), 3)

        self.assertEqual(status_code, 200)
        self.assertAlmostEqual(result, expected_result, delta=0.01)

    def test_wind_resource(self):
        expected_result = 1
        app = apiDebug.app
        tester = app.test_client(self)
        response = (
            tester.post(
                "/msp/wind",
                data=json.dumps(self.wind_params),
                content_type="application/json",
            ),
        )
        status_code = response[0].status_code
        jsonResult = json.loads(response[0].data)
        result = round(float(jsonResult.get("value")), 3)

        self.assertEqual(status_code, 200)
        self.assertAlmostEqual(result, expected_result, delta=0.01)

    def test_load_historical(self):
        app = apiDebug.app
        tester = app.test_client(self)
        response = (
            tester.post(
                "/msp/historical",
                data=json.dumps(self.bio_params),
                content_type="application/json",
            ),
        )
        status_code = response[0].status_code
        self.assertEqual(status_code, 200)
        jsonResult = json.loads(response[0].data)
        self.assertIsNotNone(jsonResult)

        exec_status = jsonResult.get("status")
        self.assertEqual(exec_status, "OK")
        exec_result = jsonResult.get("value")["measures"][0]["values"]
        self.assertEqual(len(exec_result), 60)

    def test_get_temperature(self):
        timestamp = "1420200000.0"  # 2/1/2015
        expected_value = 18.6481216738  # temp on 2/1/2015(day/month/year)

        app = apiDebug.app
        tester = app.test_client(self)
        response = (
            tester.post(
                "/msp/historical",
                data=json.dumps(self.bio_params),
                content_type="application/json",
            ),
        )
        status_code = response[0].status_code
        self.assertEqual(status_code, 200)
        jsonResult = json.loads(response[0].data)
        self.assertIsNotNone(jsonResult)

        exec_status = jsonResult.get("status")
        self.assertEqual(exec_status, "OK")
        measures = jsonResult.get("value")["measures"]
        for measured_variable in measures:
            if measured_variable["values"][0] == timestamp:
                self.assertEqual(measured_variable["values"][1], expected_value)


if __name__ == "__main__":
    unittest.main()
