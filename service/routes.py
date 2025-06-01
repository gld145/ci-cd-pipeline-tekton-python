"""
Account Service

This microservice handles the lifecycle of Accounts
"""

# pylint: disable=unused-import
from flask import jsonify, request, make_response, abort, url_for  # noqa: F401
from service.models import Account
from service.common import status  # HTTP Status Codes
from . import app  # Import Flask application


############################################################
# Health Endpoint
############################################################
@app.route("/health")
def health():
    """Health Status"""
    return jsonify(dict(status="OK")), status.HTTP_200_OK


######################################################################
# GET INDEX
######################################################################


######################################################################
# CREATE A NEW ACCOUNT
######################################################################
@app.route("/accounts", methods=["POST"])
def create_accounts():
    """
    This endpoint will create an Account based on the posted request body
    """
    app.logger.info("Request to create an Account")
    check_content_type("application/json")

    account = Account()
    account.deserialize(request.get_json())
    account.create()

    message = account.serialize()

    # Placeholder until get_account is implemented
    location_url = "/"
    # Replace with:
    # url_for("get_account", account_id=account.id, _external=True)

    return make_response(
        jsonify(message),
        status.HTTP_201_CREATED,
        {"Location": location_url}
    )


######################################################################
# LIST ALL ACCOUNTS
######################################################################
# ... place your code here to LIST accounts ...


######################################################################
# READ AN ACCOUNT
######################################################################
# ... place your code here to READ an account ...


######################################################################
# UPDATE AN EXISTING ACCOUNT
######################################################################
# ... place your code here to UPDATE an account ...


######################################################################
# DELETE AN ACCOUNT
######################################################################
# ... place your code here to DELETE an account ...


######################################################################
#  U T I L I T Y   F U N C T I O N S
######################################################################
def check_content_type(media_type):
    """Checks that the media type is correct"""
    content_type = request.headers.get("Content-Type")
    if content_type and content_type == media_type:
        return
    app.logger.error("Invalid Content-Type: %s", content_type)
    abort(
        status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        f"Content-Type must be {media_type}"
    )
