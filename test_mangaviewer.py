# test_mangaviewer.py
"""
Tests for MangaViewer module.
"""

import unittest
from mangaviewer import MangaViewer

class TestMangaViewer(unittest.TestCase):
    """Test cases for MangaViewer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MangaViewer()
        self.assertIsInstance(instance, MangaViewer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MangaViewer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
