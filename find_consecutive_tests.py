import unittest
from find_consecutive import find_consecutive_runs

class TestFindConsecutives(unittest.TestCase):

    def test_forward_run(self):
        """
        Test if forward runs can be found.
        """
        self.assertEqual(find_consecutive_runs([0,1,3,4,5,4,11,12,13]),[2,6])

    def test_reverse_run(self):
        """
        Test if reverse runs can be found.
        """
        self.assertEqual(find_consecutive_runs([0,1,5,4,3,8,7,6]), [2,5])

    def test_forward_and_reverse_run(self):
        """
        Test if a forward run leading into a reverse run can be found.
        """
        self.assertEqual(find_consecutive_runs([0,1,3,4,5,4,3,0]),[2,4])

    def test_no_run(self):
        """
        Test if no runs are present.
        """
        self.assertIsNone(find_consecutive_runs([0,2,4,6,5,6,1,2,9]))

    def test_forward_run_in_run(self):
        """
        Test if multiple consecutive forward runs can be chained together.
        """
        self.assertEqual(find_consecutive_runs([0,1,3,4,5,6,7,12,13,14]),[2,3,4,7])

    def test_reverse_run_in_run(self):
        """
        Test if multiple consecutive reverse runs can be chained together.
        """
        self.assertEqual(find_consecutive_runs([14,13,12,7,6,5,4,3,1,0]),[0,3,4,5])

    def test_non_run_forward_to_reverse_run_length_4(self):
        """
        Test if two element non run leading into reverse run causes false positive.
        """
        self.assertEqual(find_consecutive_runs([4,5,6,5,4,3], run_length=4),[2])

    def test_short_values(self):
        self.assertIsNone(find_consecutive_runs([2]))

if __name__ == '__main__':
    unittest.main()
