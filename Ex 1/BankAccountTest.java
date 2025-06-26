import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class BankAccountTest {

    @Test
    void testValidInitialization() {
        BankAccount account = new BankAccount(100.0);
        assertEquals(100.0, account.getBalance());  // Should pass
    }

    @Test
    void testInvalidInitializationNegativeBalance() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            new BankAccount(-50.0);
        });
        assertEquals("Initial balance cannot be negative.", exception.getMessage());  // Should pass
    }

    @Test
    void testDepositValidAmount() {
        BankAccount account = new BankAccount(100.0);
        account.deposit(50.0);
        assertEquals(200.0, account.getBalance()); // ❌ Intentionally wrong expected value; will FAIL
    }

    @Test
    void testDepositInvalidAmountZeroOrNegative() {
        BankAccount account = new BankAccount(100.0);
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            account.deposit(0);
        });
        assertEquals("Deposit amount must be positive.", exception.getMessage());  // Should pass
    }

    @Test
    void testWithdrawValidAmount() {
        BankAccount account = new BankAccount(200.0);
        account.withdraw(50.0);
        assertEquals(100.0, account.getBalance()); // ❌ Intentionally wrong expected value; will FAIL
    }

    @Test
    void testWithdrawInvalidAmountZeroOrNegative() {
        BankAccount account = new BankAccount(100.0);
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            account.withdraw(-10);
        });
        assertEquals("Withdrawal amount must be positive.", exception.getMessage());  // Should pass
    }

    @Test
    void testWithdrawAmountExceedingBalance() {
        BankAccount account = new BankAccount(100.0);
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            account.withdraw(150.0);
        });
        assertEquals("Insufficient balance.", exception.getMessage());  // Should pass
    }

    // Extra failing test for demonstration
    @Test
    void testIncorrectBalanceCheck() {
        BankAccount account = new BankAccount(300.0);
        assertEquals(0.0, account.getBalance()); // ❌ This will FAIL since balance is 300
    }
}
