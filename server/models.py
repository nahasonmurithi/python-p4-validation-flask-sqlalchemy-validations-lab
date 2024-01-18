from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators 
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("no name entered")
        if Author.query.filter(Author.name == name).first():
            raise ValueError('that name is taken')
        if len(name) < 5 or len(name) > 20:
            raise ValueError('name should be more that 5 char and less that 20 char')
        return name

    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if len(phone_number) !=10:
            raise ValueError('Phone number should be 10 digits')
        return phone_number

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'
# Author phone numbers are exactly ten digits


class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators
    @validates('title')
    def validate_title(self, key, title):
        if not title:
            raise ValueError('title of post should be included!')
        return title
    
    
    @validates('content')
    def validate_content(self, key, content):
        if len(content) < 250:
            raise ValueError('Content that should be more than 250 characters')
        return content

    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) > 250:
            raise ValueError('Summary characters chould not exceed 250, its too long bru!')
        return summary
    
    @validates("category")
    def validate_category(self, key, category):
        if category not in ["Fiction", "Non-Fiction"]:
            raise ValueError("Category must be in Fiction or Non-Fiction")
        return category
    
    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'

# All authors have a name
# No two authors have the same name
# All posts have a title
    # Post content is at least 250 characters long


# Post summary is a maximum of 250 characters
# Post category is either Fiction or Non-Fiction. This step requires an inclusion validator, which was not outlined in the lesson. You'll need to refer to the SQLAlchemy guideLinks to an external site. to look up how to use it.