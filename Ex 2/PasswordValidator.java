public class PasswordValidator {

    public static boolean isValid(String password) {
        if (password == null || password.equals("null") || password.isEmpty()) {
            return false;
        }

        if (password.length() < 8) return false;
        if (password.contains(" ")) return false;

        boolean hasUpper = false, hasLower = false, hasDigit = false, hasSpecial = false;
        String specials = "!@#$%^&*()-+";

        for (char c : password.toCharArray()) {
            if (Character.isUpperCase(c)) hasUpper = true;
            else if (Character.isLowerCase(c)) hasLower = true;
            else if (Character.isDigit(c)) hasDigit = true;
            else if (specials.contains(String.valueOf(c))) hasSpecial = true;
        }

        return hasUpper && hasLower && hasDigit && hasSpecial;
    }
}
