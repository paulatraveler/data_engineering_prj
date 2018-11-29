import pandas as pd
import numpy as np

from vente_privee.calculate import calculate


class TestCalculate:

    def test_calculate_for_empty_data_frame_return_empty_list(self):
        data = {
            'bone': [],
            'muscle': [],
            'number': [],
        }
        df = pd.DataFrame(data)
        expected_output = []
        output = calculate(df)
        assert output == expected_output

    def test_calculate_for_one_element_return_one_row_with_mean(self):
        data = {
            'bone': ['bone'],
            'muscle': ['muscle'],
            'number': [1.0],
        }
        df = pd.DataFrame(data)
        expected_output = [1.0]
        output = calculate(df)
        assert output == expected_output

    def test_calculate_for_two_element_return_two_rows_with_mean_and_std(self):
        data = {
            'bone': ['bone', 'bone'],
            'muscle': ['muscle', 'muscle'],
            'number': [1.0, 1.0],
        }
        df = pd.DataFrame(data)
        expected_output = [1.0, 0]
        output = calculate(df)
        assert output == expected_output

    def test_calculate_for_three_elements_returns_correct_mean_and_std(self):
        data = {
            'bone': ['bone', 'bone', 'bone'],
            'muscle': ['muscle', 'muscle', 'muscle'],
            'number': [1.0, 2.0, 3.0],
        }
        df = pd.DataFrame(data)
        expected_output = [2.0, np.std([1.0, 2.0, 3.0], ddof=True), 2.0]
        output = calculate(df)
        assert output == expected_output

    def test_calculate_for_four_elements_returns_correct_mean_and_std(self):
        data = {
            'bone': ['bone', 'bone', 'bone', 'bone'],
            'muscle': ['muscle', 'muscle', 'muscle', 'muscle'],
            'number': [1.0, 2.0, 3.0, 4.0],
        }
        df = pd.DataFrame(data)
        expected_output = [
            2.5,
            np.std([1.0, 2.0, 3.0, 4.0], ddof=True),
            2.5,
            np.std([1.0, 2.0, 3.0, 4.0], ddof=True)
        ]
        output = calculate(df)
        assert output == expected_output

    def test_bigger_dataset(self):
        data = pd.read_csv(
            'data.csv',
            header=None,
            names=["bone", "muscle", "number"])
        output = calculate(data)
        print(output)
        assert len(output) == 10000

