def test_on_line():
    from coordinate import on_line
    answer = on_line((0, 0), (2, 2), 1)
    expected = 1
    assert answer == expected
