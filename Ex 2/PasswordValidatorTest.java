import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class PasswordValidatorTest {

    @Test
    void testValidPassword() {
        assertTrue(PasswordValidator.isValid("Abcdef1!")); // Should pass
    }

    @Test
    void testPasswordTooShort() {
        assertFalse(PasswordValidator.isValid("Ab1!")); // Too short, should fail
    }

    @Test
    void testPasswordNoUppercase() {
        assertFalse(PasswordValidator.isValid("abcdef1!")); // No uppercase, should fail
    }

    @Test
    void testPasswordNoLowercase() {
        assertFalse(PasswordValidator.isValid("ABCDEF1!")); // No lowercase, should fail
    }

    @Test
    void testPasswordNoDigit() {
        assertFalse(PasswordValidator.isValid("Abcdefg!")); // No digit, should fail
    }

    @Test
    void testPasswordNoSpecialChar() {
        assertFalse(PasswordValidator.isValid("Abcdef12")); // No special char, should fail
    }

    @Test
    void testPasswordWithSpace() {
        assertFalse(PasswordValidator.isValid("Abc def1!")); // Contains space, should fail
    }

    @Test
    void testPasswordNull() {
        assertFalse(PasswordValidator.isValid(null)); // Null password, should fail
    }

    @Test
    void testPasswordEmpty() {
        assertFalse(PasswordValidator.isValid("")); // Empty password, should fail
    }

    // Intentionally failing test for demonstration
    @Test
    void testIncorrectValidPasswordCheck() {
        assertTrue(PasswordValidator.isValid("abcdefg1!")); // ❌ No uppercase, should actually fail but expected true
    }
}
