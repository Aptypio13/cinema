class Film:
    def __init__(self, id, title, rating, description =""):
        self.id = id
        self.title=title
        self.rating=rating
        self.description=description

    def __str__(self):
        return f"{self.title} with {self.rating} about {self.description}"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "rating": self.rating,
            "description": self.description # Format date
        }

    def to_json(self):
        return {
            "title": self.title,
            "rating": self.rating,
            "description": self.description
        }