import json


from flask import Blueprint
from status import Status
from modules.newsfeed.composed import file_upload, extract_feeds, get_page, push_like, like_count
from util.exceptions import FileNotFoundException, FileNotSelectedException
from util.helpers import construct_response_message

nw = Blueprint('newsfeed', __name__, url_prefix='/api')


@nw.route('/newsfeed', methods=['POST'])
def content_upload():
    """
            Endpoint for posting images for newsfeed.

            this post is for uploading images by a particular user in newsfeed/


            ---
            requestBody:
                description: upload image file
                required: true
                content:
                    multipart/form-data:
                        schema:
                            type: object
                            properties:
                                name:
                                    type: string

            responses:
                200:
                    description: File successfully uploaded.
                404:
                    description: File not found
            """
    try:
        file_upload()
        message = construct_response_message(response_message="file successfully uploaded")
        return json.dumps(message), Status.HTTP_202_ACCEPTED

    except FileNotFoundException as e:
        message = construct_response_message(error_message=e.error_message)
        return json.dumps(message), Status.HTTP_404_NOT_FOUND

    except FileNotSelectedException as e:
        message = construct_response_message(error_message=e.error_message)
        return json.dumps(message), Status.HTTP_417_EXPECTATION_FAILED

    pass


@nw.route('/newsfeed', methods=['GET'])
def fetch_all_feeds():
    """
                Endpoint for getting images for newsfeed.

                this post is for getting all images for displaying in newsfeed/


                ---

                responses:
                    200:
                        description: list of feeds.
                    404:
                        description: File not found
                """
    try:
        feeds = extract_feeds()
        message = construct_response_message(feeds=feeds)
        return json.dumps(message), Status.HTTP_200_OK

    except FileNotFoundException as e:
        message = construct_response_message(error_message=e.error_message)
        return json.dumps(message), Status.HTTP_404_NOT_FOUND


@nw.route('/newsfeed/paginate', methods=["GET"])
def pagination():
    """
        Endpoint for fetching the details of a pagination.

        This endpoint must be such that it has to provide params for queryong the page.


        ---
        parameters:
            -   name: Query Params
                in: params
                required: true
                schema:
                    type: string
                description: page number for getting respective page.



        responses:
            200:
                description: Returns the details feed.
            404:
                description: feed page not found

        """
    pages, number = get_page()
    message = construct_response_message(pages=pages,
                                         number=number)
    return json.dumps(message), Status.HTTP_200_OK


@nw.route('/feed/like', methods=['PUT'])
def increase_like():
    """

        Endpoint for increasing like count.

                ---

                requestBody:
                    description: Increasing like
                    required: true
                    content:
                        application/json:
                            schema:
                                type: object
                                properties:
                                    id:
                                        type: string
                                        required: true

                responses:
                    200:
                        description: Returns like count.
        """
    like_count = push_like()
    message = construct_response_message(like_count=like_count)
    return json.dumps(message), Status.HTTP_200_OK


@nw.route('/feed/like-count', methods=['PUT'])
def fetch_like_count():
    """

            Endpoint for increasing like count.

                    ---

                    requestBody:
                        description: Increasing like
                        required: true
                        content:
                            application/json:
                                schema:
                                    type: object
                                    properties:
                                        id:
                                            type: string
                                            required: true

                    responses:
                        200:
                            description: Returns like count.
            """
    like = like_count()
    message = construct_response_message(like=like)
    return json.dumps(message), Status.HTTP_200_OK
