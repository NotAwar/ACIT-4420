import datetime

def log_message(contact: dict, message: str):
    """
    Logs the message sent to the contact in a log file with a timestamp.
    """
    with open("message_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - Sent to {contact['name']} ({contact['email']}): {message}\n")
