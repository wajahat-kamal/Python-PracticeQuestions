# Library Book Issue Tracker

books = [
    {"name": "Python Basics", "status": "issued"},
    {"name": "JavaScript Guide", "status": "available"},
    {"name": "Data Structures", "status": "issued"},
    {"name": "React Handbook", "status": "issued"},
    {"name": "Node.js Essentials", "status": "available"}
]

def issue_tracker(books):
    issued_books = 0;

    for book in books:
        if book["status"] == "issued":
            issued_books += 1;

    status = "Limit Reached" if issued_books >= 3 else ""

    return f"Total Books: {len(books)} \nIssued Books: {issued_books} \nAvaliabe Books: {len(books) - issued_books} \n{status}"

print(issue_tracker(books))