import logging
from typing import NamedTuple

import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("double_min")


class Points:
    first_min: list[[int, float]]
    max_in_interval: list[[int, float]]
    second_min: list[[int, float]]
    invest_th: list[[int, float]]


class DoubleMin:
    def __init__(self,
                 last_min_window_atleast=10,
                 last_min_window_atmost=90,
                 after_double_min_atmost=45,
                 double_min_tolerance=0.005,
                 down_after_double_min_tolerance=0.01,
                 up_after_double_min_tolerance=0.01,
                 double_min_dim_atleast=0.05):
        self.last_min_window_atleast = last_min_window_atleast
        self.last_min_window_atmost = last_min_window_atmost
        self.after_double_min_atmost = after_double_min_atmost
        self.double_min_tolerance = double_min_tolerance
        self.down_after_double_min_tolerance = down_after_double_min_tolerance
        self.up_after_double_min_tolerance = up_after_double_min_tolerance
        self.double_min_dim_atleast = double_min_dim_atleast

    def detect(self, data):
        logger.debug("")
        logger.debug("")
        logger.debug(f"Provided data has {len(data)} data points.")
        first_min = np.inf
        second_min = np.inf
        max_in_interval = 0
        interval = 0
        second_interval = 0
        points = Points()
        tot_idx = 0
        for i, x in enumerate(data):
            if interval < self.last_min_window_atleast:
                if x < first_min * (1 - min(0.99, self.double_min_tolerance)):
                    first_min = x
                    points.first_min = [i, first_min]
                    max_in_interval = 0
                    interval = 0
                    logger.debug(f"First min found {first_min}.")
                else:
                    interval += 1
                    if x > max_in_interval:
                        max_in_interval = x
                        points.max_in_interval = [i, max_in_interval]
            else:
                data = data[i:]
                tot_idx += i
                logger.debug(f"Interval after first min matched. Searching second min.")
                logger.debug(f"First min: {points.first_min}")
                logger.debug(f"Max in interval: {points.max_in_interval}")
                logger.debug(f"Current value: {x}")
                logger.debug(f"Interval: {interval}")
                break

        if interval < self.last_min_window_atleast or tot_idx == 0:
            logger.debug(f"Interval after first min not found before end of data. "
                         f"Searching second min. Double min conditions not fulfilled.")
            return None

        for i, x in enumerate(data):
            if interval <= self.last_min_window_atmost:
                if (x - first_min) / first_min <= self.double_min_tolerance:
                    if max_in_interval / first_min >= (1 + self.double_min_dim_atleast):
                        second_min = x
                        points.second_min = [tot_idx + i, second_min]
                        logger.info("Found second min with adequate max. Waiting for overcoming the max to invest.")
                        logger.debug(f"First min: {points.first_min}")
                        logger.debug(f"Second min: {points.second_min}")
                        logger.debug(f"Max in interval: {points.max_in_interval}")
                        logger.debug(f"Interval: {interval}")
                        data = data[i:]
                        tot_idx += i
                        break
                    else:
                        logger.info("Double min found but max isn't big enough. Double min conditions not fulfilled.")
                        logger.debug(f"First min: {points.first_min}")
                        logger.debug(f"Second min: {x}")
                        logger.debug(f"Interval: {interval}")
                    return None
                else:
                    interval += 1
                    if x > max_in_interval:
                        max_in_interval = x
                        points.max_in_interval = [tot_idx + i, max_in_interval]
            else:
                logger.info("Double min window passed and second min hasn't been found. Double min conditions not fulfilled.")
                logger.debug(f"First min: {points.first_min}")
                logger.debug(f"Last value: {data[i-1]}")
                logger.debug(f"Interval: {interval}")
                return None

        if second_min == np.inf:
            logger.info("Data reached its end and second min hasn't been found. Double min conditions not fulfilled.")
            logger.debug(f"First min: {points.first_min}")
            logger.debug(f"Interval: {interval}")
            return None

        for i, x in enumerate(data):
            if (second_min - x) / second_min > self.down_after_double_min_tolerance:
                logger.info("After second min value went down too much. Double min conditions not fulfilled.")
                logger.debug(f"First min: {points.first_min}")
                logger.debug(f"Second min: {points.second_min}")
                logger.debug(f"Latest value: {x}")
                logger.debug(f"Max in interval: {points.max_in_interval}")
                logger.debug(f"Interval: {interval}")
                logger.debug(f"Second interval: {second_interval}")
                return None
            elif second_interval > self.after_double_min_atmost:
                logger.info("After second min value hasn't raised fast enough. Double min conditions not fulfilled.")
                logger.debug(f"First min: {points.first_min}")
                logger.debug(f"Second min: {points.second_min}")
                logger.debug(f"Latest value: {x}")
                logger.debug(f"Max in interval: {points.max_in_interval}")
                logger.debug(f"Interval: {interval}")
                logger.debug(f"Second interval: {second_interval}")
                return None
            elif (max_in_interval - x) / max_in_interval <= self.up_after_double_min_tolerance:
                points.invest_th = [tot_idx + i, x]
                logger.info("Value went up over previous max, investment recommended.")
                logger.debug(f"First min: {points.first_min}")
                logger.debug(f"Second min: {points.second_min}")
                logger.debug(f"Latest value: {x}")
                logger.debug(f"Max in interval: {points.max_in_interval}")
                logger.debug(f"Interval: {interval}")
                logger.debug(f"Second interval: {second_interval}")
                return points
            else:
                second_interval += 1

        logger.info("After second min value hasn't raised enough yet. Double min conditions not fulfilled.")
        logger.debug(f"First min: {points.first_min}")
        logger.debug(f"Second min: {points.second_min}")
        logger.debug(f"Latest value: {data[-1]}")
        logger.debug(f"Max in interval: {max_in_interval}")
        logger.debug(f"Interval: {interval}")
        logger.debug(f"Second interval: {second_interval}")
        return None

