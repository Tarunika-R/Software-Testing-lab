import time
import pytest
from auth_module import UserAuth

@pytest.fixture
def auth():
    auth = UserAuth()
    auth.register_user("alice", "password123")
    return auth

# ✅ Should Pass
def test_successful_login(auth):
    success, token = auth.validate_login("alice", "password123")
    assert success
    assert auth.is_token_valid(token)

# ❌ Intentionally Failing - expects wrong password to be valid
def test_failed_login_should_pass_but_fails(auth):
    success, message = auth.validate_login("alice", "wrongpass")
    assert success  # ❌ This will fail because login should fail

# ✅ Should Pass
def test_user_blocking(auth):
    for _ in range(3):
        auth.validate_login("alice", "wrongpass")

    success, msg = auth.validate_login("alice", "password123")
    assert not success
    assert msg == "User is temporarily blocked."

# ❌ Intentionally Failing - trying to login immediately after block
def test_unblock_too_early(auth):
    for _ in range(3):
        auth.validate_login("alice", "wrongpass")
    
    # Not waiting for block period to expire
    success, token = auth.validate_login("alice", "password123")
    assert success  # ❌ Will fail, user is still blocked

# ✅ Should Pass
def test_token_generation(auth):
    success, token = auth.validate_login("alice", "password123")
    assert success
    assert isinstance(token, str)
    assert len(token) == 32
