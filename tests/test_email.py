import unittest

from aprsd.plugins import email


class TestEmail(unittest.TestCase):
    def test_get_email_from_shortcut(self):
        email_address = "something@something.com"
        addr = f"-{email_address}"
        actual = email.get_email_from_shortcut(addr)
        self.assertEqual(addr, actual)

        config = {"aprsd": {"email": {"nothing": "nothing"}}}
        actual = email.get_email_from_shortcut(addr)
        self.assertEqual(addr, actual)

        config = {"aprsd": {"email": {"shortcuts": {"not_used": "empty"}}}}
        actual = email.get_email_from_shortcut(addr)
        self.assertEqual(addr, actual)

        config = {"aprsd": {"email": {"shortcuts": {"-wb": email_address}}}}
        short = "-wb"
        actual = email.get_email_from_shortcut(short)
        self.assertEqual(email_address, actual)
