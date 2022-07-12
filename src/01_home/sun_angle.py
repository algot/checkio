def sun_angle(time: str) -> float | str:
    # replace this for solution
    sunrise_time = 360
    sunset_time = 720

    hours, minutes = time.split(':')
    time_in_minutes = 60 * int(hours) + int(minutes)
    time_from_sunset = time_in_minutes - sunrise_time

    if 0 <= time_from_sunset <= sunset_time:
        angle = time_from_sunset * 0.25
        return angle
    else:
        return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
