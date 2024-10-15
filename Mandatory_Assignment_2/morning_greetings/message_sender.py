def send_message(email: str, message: str):
    """
    Simulates sending a message to the provided email.
    """
    if not email:
        raise ValueError("Email address is missing")
    print(f"Sending message to {email}: {message}")
