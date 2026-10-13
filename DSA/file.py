
import tempfile
import unittest
from pathlib import Path

from file import category_for, organize


class TestFileOrganizer(unittest.TestCase):
    def test_category_for_known_extension(self):
        self.assertEqual(category_for(Path("photo.JPG")), "Images")
        self.assertEqual(category_for(Path("notes.pdf")), "Documents")

    def test_unknown_extension(self):
        self.assertEqual(category_for(Path("data.xyz")), "Other")

    def test_organize_moves_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            photo = folder / "photo.png"
            photo.write_text("test image content")

            count = organize(folder)

            self.assertEqual(count, 1)
            self.assertTrue((folder / "Images" / "photo.png").exists())
            self.assertFalse(photo.exists())

    def test_dry_run_does_not_move_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            photo = folder / "notes.pdf"
            photo.write_text("test document")

            count = organize(folder, dry_run=True)

            self.assertEqual(count, 1)
            self.assertTrue(photo.exists())

    def test_invalid_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            missing = Path(temp_dir) / "missing"

            with self.assertRaises(ValueError):
                organize(missing)


if __name__ == "__main__":
    unittest.main()
