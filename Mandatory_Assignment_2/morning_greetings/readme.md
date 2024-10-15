# Morning Greetings Package

## Description
The morning_greetings package automates sending personalized "Good Morning" messages to contacts. The messages are customized based on the recipient’s name and the day of the week and are sent at a preferred time. Each message is logged for record-keeping.

## Installation

Clone or download the repository.
Install the package using: pip install .

## Features
Add, remove, and list contacts (name, email, preferred time).
Messages are customized based on the day of the week.
Simulates sending messages by printing them to the console.
Automatically send messages at scheduled times.
Logs all sent messages with timestamps.
Usage

Add a contact:
python main.py add-contact "Name" "email@example.com" --preferred-time "08:00 AM"

List all contacts:
python main.py list-contacts

Remove a contact:
python main.py remove-contact "Name"

Send messages manually:
python main.py send-messages

Run scheduled tasks:
python main.py run-scheduled-tasks

## Testing
To run unit tests, use the command:
python test.py

## Logging
All sent messages are logged in message_log.txt with timestamps and recipient details.