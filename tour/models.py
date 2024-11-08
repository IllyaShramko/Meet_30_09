from main.settings import DATABASE
class Ticket(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer(), primary_key = True)

    title = DATABASE.Column(DATABASE.String(25), nullable = False)
    date = DATABASE.Column(DATABASE.Integer(), nullable = False)
    Country = DATABASE.Column(DATABASE.String(50), nullable = False)
    price = DATABASE.Column(DATABASE.Integer(), nullable = False)
    descriprion = DATABASE.Column(DATABASE.String(50), nullable = False)
    
    def __repr__(self) -> str:
        return f"Title: {self.title}, Id: {self.id}"