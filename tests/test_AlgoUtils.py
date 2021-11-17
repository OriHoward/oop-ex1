from unittest import TestCase

import allocation_algo
from CallForElevator import CallForElevator
from Elevator import Elevator


class Test(TestCase):
    def test_add_qualified_calls(self):
        curr_elev = Elevator(0, '1', '-10', '100', 2, 2, 3, 3)
        calls = [CallForElevator('5', '-6', '46', '0', '-1'),
                 CallForElevator('8', '0', '25', '0', '-1'),
                 CallForElevator('11.0', '5', '28', '0', '-1'),
                 CallForElevator('11.6', '3', '78', '0', '-1')]
        filtered_calls = allocation_algo.add_qualified_calls(CallForElevator('5', '-6', '46', '0', '-1'), calls, curr_elev)
        self.assertEqual(filtered_calls, calls)

    def test_filter_qualified_calls(self):
        curr_elev = Elevator(0, '1', '-10', '100', 2, 2, 3, 3)
        calls = [CallForElevator('8', '0', '25', '0', '-1'),
                 CallForElevator('11.0', '5', '28', '0', '-1'),
                 CallForElevator('18', '3', '78', '0', '-1')]
        filtered_calls = allocation_algo.filter_qualified_calls(CallForElevator('5', '-6', '46', '0', '-1'), calls, curr_elev)
        del calls[-1]
        self.assertEqual(filtered_calls, calls)
