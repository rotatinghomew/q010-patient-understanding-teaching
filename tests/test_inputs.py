from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from humanities_analytics.inputs import read_table


class InputFixtureTests(unittest.TestCase):
    def test_synthetic_tables_have_declared_columns_and_rows(self):
        paths = sorted((ROOT / 'data').glob('*.csv'))
        self.assertGreaterEqual(len(paths), 2)
        for path in paths:
            with self.subTest(path=path.name):
                rows = read_table(path)
                self.assertTrue(rows)
                self.assertTrue(all(all(isinstance(value, str) for value in row.values()) for row in rows))
                self.assertEqual(set(rows[0]), set(rows[-1]))


if __name__ == '__main__':
    unittest.main()
