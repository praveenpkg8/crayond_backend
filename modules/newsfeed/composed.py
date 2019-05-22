import os
import string
import random
import logging

from typing import Dict, List
from PIL import Image
from flask import request
from werkzeug.utils import secure_filename

from models import Content
from util.exceptions import FileNotFoundException, FileNotSelectedException
from util.helpers import Dictnote

UPLOAD_FOLDER = '/Users/longclaw/Development/crayon-webapp/src/assets/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

logger = logging.getLogger(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def random_string(string_length=10) -> str:
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def file_upload():
    if 'file' not in request.files:
        raise FileNotFoundException("File not Found")
    file = request.files['file']
    data = request.form['description']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        raise FileNotSelectedException("No selected file")

    if file and allowed_file(file.filename):
        filename = secure_filename(random_string() + ".jpg")
        path = UPLOAD_FOLDER
        content = Content(filename, path, data)
        Content.add_content(content)
        image_file = Image.open(file)
        image_file.save(os.path.join(path, filename), quality=30)
        # file.save(os.path.join(path, filename))


def onboard_like():
    feeds = extract_feeds()

    pass


def extract_feeds() -> List:
    all_feeds = Content.get_all_feeds()
    if all_feeds is not None:
        data = []
        for feed in all_feeds:
            final_note = Dictnote(
                id=feed.id,
                image_name=feed.image_name,
                image_path=feed.image_path,
                description=feed.description,
                like_count=feed.like_count,
                created_on=str(feed.created_on)
            )
            data.append(final_note)
        return data
    else:
        raise FileNotFoundException("File not Found")


def extract_pages(pages) -> List:
    if pages is not None:
        data = []
        for page in pages.items:
            page_note = Dictnote(
                id=page.id,
                image_name=page.image_name,
                image_path=page.image_path,
                description=page.description,
                like_count=page.like_count,
                created_on=str(page.created_on),
                is_active=page.is_active
            )
            data.append(page_note)
        return data
    else:
        raise FileNotFoundException("File not Found")


def extract_page_num(pages) -> List:
    num = 1
    data = []
    for page_num in pages.iter_pages():
        if page_num:
            data.append(num)
        else:
            data.append("...")
        num += 1

    return data


def get_page():
    page_num = request.args.get('page', 1, type=int)
    pages = Content.paginate_files(page_num)
    page = extract_pages(pages)
    number = extract_page_num(pages)
    return page, number


def push_like():
    feed = request.get_json()
    id = feed['id']
    count = Content.update_like(id)
    return count

def like_count():
    like = request.get_json()
    id = like['id']
    count = Content.get_like(id)
    return count



