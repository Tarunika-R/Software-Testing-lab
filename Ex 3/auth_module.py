import hashlib
import secrets
import time

class UserAuth:
    def __init__(self):
        self.users = {}  # Format: {username: hashed_password}
        self.failed_attempts = {}  # Format: {username: [count, last_failed_time]}
        self.blocked_users = {}  # Format: {username: unblock_time}
        self.sessions = {}  # Format: {session_token: username}

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password):
        self.users[username] = self._hash_password(password)

    def is_blocked(self, username):
        unblock_time = self.blocked_users.get(username)
        if unblock_time and time.time() < unblock_time:
            return True
        elif unblock_time:
            del self.blocked_users[username]  # Unblock if time expired
        return False

    def validate_login(self, username, password):
        if self.is_blocked(username):
            return False, "User is temporarily blocked."

        hashed_input = self._hash_password(password)
        if self.users.get(username) == hashed_input:
            self.failed_attempts.pop(username, None)  # Reset failures
            token = self._generate_session_token(username)
            return True, token
        else:
            self._handle_failed_attempt(username)
            return False, "Invalid credentials."

    def _handle_failed_attempt(self, username):
        count, last_time = self.failed_attempts.get(username, (0, 0))
        count += 1
        self.failed_attempts[username] = (count, time.time())

        if count >= 3:
            self.blocked_users[username] = time.time() + 60  # Block for 1 min
            self.failed_attempts.pop(username)

    def _generate_session_token(self, username):
        token = secrets.token_hex(16)
        self.sessions[token] = username
        return token

    def is_token_valid(self, token):
        return token in self.sessions
