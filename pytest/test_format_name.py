from format_name import get_format_name

def test_first_last_name():
    """能够正确处理像'Nuj Oul'这样的姓名?"""
    format_name = get_format_name("nuj", "oul")
    assert format_name == 'Nuj Oul'