def range_overlap(ranges):
    '''Return common overlap among a set of [low, high] ranges.'''
    if not ranges: # empty ranges
        return None
    lowest, highest = ranges[0]
    for (low, high) in ranges:
        lowest = max(lowest, low)
        highest = min(highest, high)
    if (lowest >= highest):
        return None
    return (lowest, highest)

def test_range_overlap():
    assert range_overlap(()) == None
    assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == None
    assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == None
    assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)
    assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)
    assert range_overlap([ (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0) ]) == (0.0, 1.0)

test_range_overlap()

