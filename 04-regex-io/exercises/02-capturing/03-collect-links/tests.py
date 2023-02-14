
        testcase('''

        ''')



@pytest.mark.parametrize("string", [
    """
        <a href="a">fdf</a>
        fjklfjls
        <a href="b">qff</a>
        djqkljl
        <a href="abc">dfdg</a>
        fdjflkjdlf
        <a href="fiop">fdghh</a>
        fjdlfjlk
        <a href=""></a>
    """,
    """
        <a href="url1">text1</a>
        <a href="url2">text2</a><a href="url3">text3</a>
    """
])
def test_function(string):
    function_name = 'collect_links'
    assert hasattr(student, function_name), f"Missing function {function_name}"

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(string)
    expected = solution_function(string)

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"