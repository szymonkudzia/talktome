USE talk_to_me;

DROP TABLE `localization`;

CREATE TABLE `localization` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `localization` varchar(10) NOT NULL,
  `fieldName` varchar(45) NOT NULL,
  `value` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `talk_to_me`.`localization`
	(`localization`, `fieldName`, `value`)
VALUES
	('pl-pl', 'languageName', 'Polski'),
	('en-us', 'languageName', 'English'),
	('pl-pl', 'loginError', 'Podałeś nieprawidłowe dane!'),
	('en-us', 'loginError', 'You have entered wrong credentials!'),
    ('pl-pl', 'loginButton', 'Zaloguj'),
	('en-us', 'loginButton', 'Login'),
    ('pl-pl', 'rememberMe', 'Zapamiętaj mnie'),
	('en-us', 'rememberMe', 'Remember me'),
    ('pl-pl', 'email', 'Email'),
	('en-us', 'email', 'Email'),
    ('pl-pl', 'password', 'Hasło'),
	('en-us', 'password', 'Password'),
    ('pl-pl', 'loginChangePassword', 'Nie pamiętasz hasła?'),
	('en-us', 'loginChangePassword', 'Forgot your password?'),
    ('pl-pl', 'loginPageSlogan', 'Poznaj nowych przyjaciół z całego świata!'),
	('en-us', 'loginPageSlogan', 'Meet new friends from all around of the world!'),
    ('pl-pl', 'loginAddNewAccount', 'Załóż nowe konto'),
	('en-us', 'loginAddNewAccount', 'Create a new account'),
	('pl-pl', 'languageSelectBoxLabel', 'Zmień język'),
	('en-us', 'languageSelectBoxLabel', 'Change language'),
	('pl-pl', 'firstName', 'Imię'),
	('en-us', 'firstName', 'First name'),
	('pl-pl', 'lastName', 'Nazwisko'),
	('en-us', 'lastName', 'Last name'),
	('pl-pl', 'passwordRepeated', 'Powtórz hasło'),
	('en-us', 'passwordRepeated', 'Repeat password'),
	('pl-pl', 'registerButton', 'Zarejestruj'),
	('en-us', 'registerButton', 'Register'),
	('pl-pl', 'birthdate', 'Data urodzenia'),
	('en-us', 'birthdate', 'Birth date');