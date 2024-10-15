import typer
import schedule
import time
from contacts_manager import ContactsManager
from message_generator import generate_message
from message_sender import send_message
from logger import log_message

# Initialize Typer app
app = typer.Typer()

@app.command()
def add_contact(name: str, email: str, preferred_time: str = "08:00 AM"):
    """
    Adds a new contact to the list.
    """
    cm = ContactsManager()
    cm.add_contact(name, email, preferred_time)
    typer.echo(f"Contact {name} added successfully!")

@app.command()
def remove_contact(name: str):
    """
    Removes a contact by name.
    """
    cm = ContactsManager()
    cm.remove_contact(name)
    typer.echo(f"Contact {name} removed successfully!")

@app.command()
def list_contacts():
    """
    Lists all contacts.
    """
    cm = ContactsManager()
    cm.list_contacts()

@app.command()
def send_messages():
    """
    Sends 'Good Morning' messages to all contacts.
    """
    cm = ContactsManager()
    contacts = cm.get_contacts()

    if not contacts:
        typer.echo("No contacts available to send messages.")
        return

    for contact in contacts:
        try:
            message = generate_message(contact['name'])
            send_message(contact['email'], message)
            log_message(contact, message)
        except Exception as e:
            typer.echo(f"Failed to process contact {contact['name']}: {e}")

def schedule_message_sending():
    """
    Schedules sending of messages based on the contacts' preferred times.
    """
    cm = ContactsManager()
    contacts = cm.get_contacts()

    if not contacts:
        typer.echo("No contacts available.")
        return

    for contact in contacts:
        preferred_time = contact['preferred_time']

        # Convert the preferred time to 24-hour format
        hour, minute = map(int, preferred_time[:-3].split(":"))
        am_pm = preferred_time[-2:]
        if am_pm == "PM" and hour != 12:
            hour += 12
        if am_pm == "AM" and hour == 12:
            hour = 0

        # Schedule the message sending
        schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(
            send_message, contact['email'], generate_message(contact['name'])
        )
        typer.echo(f"Scheduled message for {contact['name']} at {preferred_time}.")

@app.command()
def run_scheduled_tasks():
    """
    Runs scheduled message tasks continuously.
    """
    schedule_message_sending()
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    app()  # Ensure this runs the Typer app
