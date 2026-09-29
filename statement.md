# Problem Statement

## Problem

People often keep phone numbers and email addresses in scattered places such as notebooks, chat messages or memory. Finding a detail quickly is hard, and small mistakes like a wrong number or a repeated entry are common. A basic contact manager that runs on any computer with Python and keeps data safely between sessions would solve this without needing a heavy application or an internet connection.

## Scope

**Included**
- A console-based contact book written in Python
- Adding, viewing, editing, deleting, listing and searching contacts
- Checking phone numbers and email addresses before saving
- Saving and loading contacts from a local JSON file
- Clear messages for wrong input and file problems

**Not included**
- Graphical or web interface
- User accounts, passwords or encryption
- Cloud sync or sharing contacts between devices
- Importing contacts from a phone

## Target Users

- Students and individuals who want a simple personal contact list on their computer
- Beginners learning Python who want to see how functions, dictionaries and file handling work together

## High-Level Features

1. **Contact management:** add, view, edit and delete contacts, with duplicate and empty-name checks
2. **Data processing and validation:** phone must be 10 digits, email must contain "@" and a dot after it
3. **Reporting:** list all contacts in alphabetical order and search by part of a name
4. **Storage:** automatic saving to `contacts.json` and loading at startup, with protection against a damaged file
