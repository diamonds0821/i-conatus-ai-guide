import unittest
from unittest.mock import patch

from scripts.export_notion import fetch_page


class FetchPageTests(unittest.TestCase):
    @patch("scripts.export_notion.subprocess.run")
    def test_reads_nested_cli_markdown_response(self, run):
        run.return_value.stdout = """
        {
          "markdown": {
            "markdown": "# 본문",
            "truncated": false,
            "unknown_block_ids": []
          },
          "page": {"id": "page-id"}
        }
        """

        self.assertEqual(fetch_page("page-id"), "# 본문")

    @patch("scripts.export_notion.subprocess.run")
    def test_rejects_incomplete_page(self, run):
        run.return_value.stdout = """
        {
          "markdown": {
            "markdown": "# 일부 본문",
            "truncated": true,
            "unknown_block_ids": ["block-id"]
          }
        }
        """

        with self.assertRaises(RuntimeError):
            fetch_page("page-id")


if __name__ == "__main__":
    unittest.main()

