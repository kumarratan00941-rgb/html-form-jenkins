
import unittest
from html.parser import HTMLParser
from pathlib import Path


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.forms = []
        self.inputs = []
        self.buttons = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form":
            self.forms.append(attrs)

        elif tag == "input":
            self.inputs.append(attrs)

        elif tag == "button":
            self.buttons.append(attrs)


class TestHTMLForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        html_file = Path(__file__).parent / "index.html"
        cls.html = html_file.read_text(encoding="utf-8")
        cls.parser = FormParser()
        cls.parser.feed(cls.html)

    def test_form_exists(self):
        self.assertTrue(self.parser.forms, "Form is missing")

    def test_required_input_fields(self):
        fields = {
            item.get("name"): item
            for item in self.parser.inputs
        }

        for field in ("name", "email", "contact"):
            with self.subTest(field=field):
                self.assertIn(field, fields)
                self.assertIn("required", fields[field])

    def test_email_input_type(self):
        email = next(
            (item for item in self.parser.inputs
             if item.get("name") == "email"),
            None
        )
        self.assertIsNotNone(email)
        self.assertEqual(email.get("type"), "email")

    def test_contact_number_validation(self):
        contact = next(
            (item for item in self.parser.inputs
             if item.get("name") == "contact"),
            None
        )
        self.assertIsNotNone(contact)
        self.assertEqual(contact.get("pattern"), "[0-9]{10}")

    def test_submit_button_exists(self):
        self.assertTrue(
            any(button.get("type") == "submit"
                for button in self.parser.buttons),
            "Submit button is missing"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
