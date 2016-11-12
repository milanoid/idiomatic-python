# idiomatic-python
My study notes for Flask tutorial [videos](https://www.youtube.com/channel/UC8jQsBz_w948kSc7ehMRGmQ) by @jeffknupp

# Ticket System application
Allows user to view a list of existing tickets and create a new ticket.

- start the app: ```python3 app.py```
- access ```http://localhost:5000```

## Endpoints

- `/` list all tickets
- `/ticket` enter ticket
- `/ticket/<int:ticket_id>` view ticket details

## TODO

- [ ] use SQLAlchemy instead raw SQL commands
- [ ] implement `/ticket` and `/ticket/<int:ticket_id>`
- [ ] use css for templates
