from unittest import TestCase
from src.data_structures.table.hash_table import HashTable


class TestTable(TestCase):
    def test_hash_table(self):
        ht = HashTable()
        ht.set('foo', 'bar')

        self.assertEqual(ht.get_keys(), {'foo': 4})
        self.assertEqual(ht.get('foo'), 'bar')

        ht.delete('foo')
        self.assertEqual(ht.get_keys(), {})
        self.assertIsNone(ht.get('foo'))

