# coding=utf-8

"""
July 14 Challenge -  Angle Between Hands of a Clock

Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed
between the hour and the minute hand.


"""


def angleClock(hour, minutes):
    """
    :type hour: int
    :type minutes: int
    :rtype: float
    """
    # minute_deg_per_min = 360° / 60 = 6°
    # hour_deg_per_hour = 360° / 12 = 30°
    # hour_deg_per_min = hour_deg_per_hour / 60 = 30° / 60 = 0.5°

    # hour * hour_deg_per_hour + minutes * hour_deg_per_min
    h_deg = 30 * hour + 0.5 * minutes
    # minutes * minute_deg_per_min
    m_deg = 6 * minutes
    diff = abs(h_deg - m_deg)
    return diff if diff <= 180 else 360 - diff

