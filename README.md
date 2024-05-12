# MailGuardian
MailGuardian is a best-effort email validation class written in Python. It ensures that email addresses are properly formatted, have MX records configured, and are associated with a mailbox on the remote mail server.

**Note:** While this email validation strategy is effective with most mainstream email providers, it may encounter limitations with remote mail servers configured to conceal the presence of user mailboxes. Consequently, some legitimate email addresses might be misclassified as invalid. Therefore, I highly recommend flagging invalid email addresses for manual review instead of outright discarding them.

# Features
- **Format Validation:** Quickly validate email addresses to ensure they follow RFC 5322 standards.

- **MX Record Check:** Check if Mail Exchange (MX) records exist for an email addresses top-level domain (TLD).

- **Mailbox Verification:** Communicate over Simple Mail Transfer Protocol (SMTP) to verify the existence of mailboxes associated with an email address.

- **Simple Integration:** Seamlessly incorporate MailGuardian into an existing project to enhance email validation capabilities.

# Example
```python
  # Instantiate MailGuardian
  guardian = MailGuardian(sender='sender@example.com', smtp_port=25)
  
  # Attempt to validate an email address
  is_valid = guardian.validate_email("user@example.com")

  # Do something with the result
  print(f"The email address user@example.com is {'valid' if is_valid else 'invalid'}.")
```

# Requirements
- Python 3.x
- PythonDNS (https://www.dnspython.org/)

# Contributions
Contributions are welcome! If you encounter any issues, have suggestions for improvements, or would like to add new features, feel free to open an issue or submit a pull request.
