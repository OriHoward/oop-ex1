from unittest import TestCase

from CallForElevator import CallForElevator
from Elevator import Elevator


class TestElevator(TestCase):
    def test_get_path_load(self):
        self.assertEqual(1,1)

    def test_get_path_load_factor_estimation(self):
        curr_elev = Elevator(0, '1', '-10', '100', 2, 2, 3, 3)
        calls = [CallForElevator('8', '0', '25', '0', '-1'),
                 CallForElevator('11.0', '5', '28', '0', '-1')]
        curr_elev.allocate_calls_with_loadfactor(calls)

        calls = [CallForElevator('10', '0', '20', '0', '-1'),
                 CallForElevator('15', '10', '45', '0', '-1')]

        #68 + 85
        self.assertEqual(153, curr_elev.get_path_load_factor_estimation(calls))

    def test_allocate_calls_with_loadfactor(self):
        curr_elev = Elevator(0, '1', '-10', '100', 2, 2, 3, 3)
        calls = [CallForElevator('8', '0', '25', '0', '-1'),
                 CallForElevator('11.0', '5', '28', '0', '-1')]
        curr_elev.allocate_calls_with_loadfactor(calls)
        for call in calls:
            self.assertEqual(call.curr_allocation, curr_elev.id)
        self.assertEqual(68, curr_elev.load_factor)

    def test_get_call_load_factor(self):
        self.assertEqual(1,1)

    def test_get_call_endtime(self):
        curr_elev = Elevator(0, '1', '-10', '100', 2, 2, 3, 3)
        estimated_end_time = curr_elev.get_call_endtime(CallForElevator('8', '0', '25', '0', '-1'))
        self.assertEqual(43, estimated_end_time)
