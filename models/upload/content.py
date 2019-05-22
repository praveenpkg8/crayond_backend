import uuid
import datetime
from models import database


class Content(database.Model):

    __tablename__ = 'content'

    id = database.Column(database.String(128), unique=True, primary_key=True, default=lambda: uuid.uuid4().hex)
    image_name = database.Column(database.String(128))
    image_path = database.Column(database.String(512))
    description = database.Column(database.String(144))
    created_on = database.Column(database.DateTime, default=datetime.datetime.utcnow())
    like_count = database.Column(database.Integer)
    is_active = database.Column(database.Boolean())

    def __init__(self, image_name, image_path, description):
        self.image_name = image_name
        self.image_path = image_path
        self.description = description
        self.like_count = 0
        self.is_active = True

    @staticmethod
    def add_content(content: object):
        database.session.add(content)
        database.session.commit()

    @staticmethod
    def get_all_feeds():
        feeds = Content.query.all()
        return feeds

    @staticmethod
    def update_like(id: str):
        feed = Content.query.get(id)
        feed.like_count += 1
        database.session.commit()
        return feed.like_count

    @staticmethod
    def get_like(id: str):
        feed = Content.query.get(id)
        return feed.like_count

    @staticmethod
    def paginate_files(page_num: int):
        files = Content.query.paginate(page=page_num ,per_page=2)
        return files













