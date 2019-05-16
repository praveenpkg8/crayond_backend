import uuid
from models import database


class Content(database.Model):

    __tablename__ = 'content'

    id = database.Column(database.String(128), unique=True, primary_key=True, default=lambda: uuid.uuid4().hex)
    image_name = database.Column(database.String(128))
    image_path = database.Column(database.String(512))
    description = database.Column(database.String(144))

    def __init__(self, image_name, image_path, description):
        self.image_name = image_name
        self.image_path = image_path
        self.description = description

    @staticmethod
    def add_content(content: object):
        database.session.add(content)
        database.session.commit()

    @staticmethod
    def get_all_feeds():
        feeds = Content.query.all()
        return feeds









