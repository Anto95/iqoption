import unittest
import logging
from modelling.double_min.double_min import DoubleMin

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("test_double_min")


class TestStringMethods(unittest.TestCase):
    def test_double_min_detected(self,):
        data = [4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13,
                12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 5, 10, 15, 25]
        logger.info(" ############ Run simple test ############")
        self.assertTrue(DoubleMin().detect(data))
        logger.info(" ############ Shrink time window but increase tolerance ############")
        self.assertTrue(DoubleMin(last_min_window_atmost=36, double_min_tolerance=2).detect(data))

    def test_double_min_not_detected(self, ):
        logging.getLogger("double_min").setLevel(logging.DEBUG)
        data = [4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14,
                13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        logger.info(" ############ Run simple test ############")
        self.assertFalse(DoubleMin().detect(data))
        logger.info(" ############ Shrink time window ############")
        self.assertFalse(DoubleMin(last_min_window_atmost=36).detect(data))
        logger.info(" ############ Shrink time window and increase tolerance but not enough ############")
        self.assertFalse(DoubleMin(last_min_window_atmost=36, double_min_tolerance=0.5).detect(data))
