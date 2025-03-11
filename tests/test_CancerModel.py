import unittest
from cancer_prediction.cancer_model import CancerModel

class TestCancerModel(unittest.TestCase):

    def test_diagnosis_to_target(self):
        model = CancerModel()
        diagnosis = "Malignant"
        target = model.diagnosis_to_target(diagnosis)
        self.assertEqual(target, 0)

if __name__ == "__main__":
    unittest.main()