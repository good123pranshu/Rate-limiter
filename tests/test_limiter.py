from app.limiter import is_allowed

def test_rate_limiter():
    identifier = "test-user"

    allowed = True
    for _ in range(15):
        allowed = is_allowed(identifier)

    assert allowed is False
