# Contact Book

A simple command-line contact book written in Python. It lets you add, view, edit, delete, list and search contacts, and it saves everything to a JSON file so your contacts are still there the next time you run it.

Built for the VITyarthi "Build Your Own Project" evaluation.

## Features

- Add a contact (name, phone, email, address)
- View the details of one contact
- Edit a contact (leave a field blank to keep the old value)
- Delete a contact
- List all contacts in alphabetical order
- Search contacts by full or partial name (not case sensitive)
- Contacts are saved automatically to `contacts.json`
- Input checks: name cannot be empty, phone must be exactly 10 digits, email must look like an email
- Handles a missing or damaged data file without crashing

## Technologies Used

- Python 3.8 or above
- Standard library only (`json`, `os`), so nothing extra to install
- Git and GitHub for version control

## Project Structure

```
ContactBook_Project/
├── Contact_Book.py      # the whole program
├── contacts.json        # created automatically when you add your first contact
├── README.md
├── statement.md
├── screenshots/         # console output screenshots
└── docs/                # design diagrams (architecture, workflow, UML, data model)
```

## How to Install and Run

1. Install Python 3 from https://www.python.org if you do not have it.
2. Clone the repository (or download it as a ZIP):
   ```
   git clone <your-repository-link>
   cd ContactBook_Project
   ```
3. Run the program:
   ```
   python Contact_Book.py
   ```
   On some systems the command is `python3 Contact_Book.py`.
4. Type the number of the option you want and press Enter. Choose `7` to exit.

## Menu

```
Contact Book Menu:
1. Add Contact
2. View Contact
3. Edit Contact
4. Delete Contact
5. List All Contacts
6. Search Contacts
7. Exit
```

## Testing

The project was tested manually by running the program and entering the inputs below. The full list of 19 test cases with results is in the project report.

| Test | Input | Expected result |
|---|---|---|
| Add valid contact | Ravi, 9876543210, ravi@mail.com | Contact added successfully! |
| Duplicate name | Add Ravi again | Contact already exists! |
| Bad phone | 12345678 | Invalid phone number message, contact not saved |
| Bad email | asha.com | Invalid email address! |
| Edit with blank fields | Change only the phone | Email and address stay the same |
| Search | `an` | Shows every name containing "an" |
| Restart the program | View a saved contact | Contact is still there |
| Damaged file | Put `{bad json` in `contacts.json` | Warning shown, old file kept as `contacts.json.bak` |

To repeat a test, delete `contacts.json` first so you start with an empty contact book.

## Screenshots

| Adding contacts | List and search | Edit and view |
|---|---|---|
| ![add](screenshots/add_contact.png) | ![list](screenshots/list_and_search.png) | ![edit](screenshots/edit_and_view.png) |

## Known Limitations

- Names are treated as unique keys and are case sensitive, so "ravi" and "Ravi" are two different contacts.
- Only a console interface is available.
- The JSON file is plain text and is not encrypted.

## Future Improvements

- A graphical interface
- Import and export of contacts as CSV
- Support for more than one phone number per contact
