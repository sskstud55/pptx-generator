import unittest
import os
from main import app, PRESENTATIONS_DIR
import shutil
import re

class PresentationGenerationTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        if os.path.exists(PRESENTATIONS_DIR):
            shutil.rmtree(PRESENTATIONS_DIR)
        os.makedirs(PRESENTATIONS_DIR)

    def test_presentation_creation_and_download(self):
        # Test presentation creation
        response = self.app.post("/chat", data={"message": "create presentation My Test Presentation"})
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertIn("created", json_data['response'])

        # Extract filename from the response
        match = re.search(r"href='/download/([^']+)'", json_data['response'])
        self.assertIsNotNone(match)
        filename = match.group(1)

        # Test download
        response = self.app.get(f"/download/{filename}")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data)


    def tearDown(self):
        if os.path.exists(PRESENTATIONS_DIR):
            shutil.rmtree(PRESENTATIONS_DIR)

if __name__ == "__main__":
    unittest.main()
