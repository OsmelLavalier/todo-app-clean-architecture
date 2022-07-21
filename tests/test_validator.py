from utils import validator


def test_validate_username_valid():
    assert validator.validate_username("FooBar123") == True


def test_validate_username_only_alphabets():
    assert validator.validate_username("FooBar") == True


def test_validate_username_no_username():
    assert validator.validate_username("") == False


def test_validate_username_illegal_characters():
    assert validator.validate_username("Foo\/B:ar123!@£$$][{") == False


def test_validate_username_only_space():
    assert validator.validate_username(" ") == False


def test_validate_username_with_allowed_characters():
    assert validator.validate_username("fooBar12-_") == True
