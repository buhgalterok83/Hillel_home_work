def skip(condition, reason=''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                print(f"Skipped {func.__name__}() because {reason}")
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator
@skip(condition=True, reason='Skipped because of JIRA-123 bug')
def test_two_plus_two():
    assert 2 + 2 == 5

test_two_plus_two()  # Skipped because of JIRA-123 bug
