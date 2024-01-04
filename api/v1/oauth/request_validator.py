from typing import Optional
from oauthlib.oauth2 import RequestValidator as rv
from sqlmodel import Session, select

from ...db import engine, AccessClient, User, AuthorizationToken

class RequestValidator(rv):
    # Ordered roughly in order of appearance in the authorization grant flow

    # Pre- and post-authorization.

    def validate_client_id(self, client_id, request, *args, **kwargs):
        # Simple validity check, does client exist? Not banned?
        with Session(engine) as session: 
            statement = select(AccessClient).where(AccessClient.client_id==client_id)
            result = session.exec(statement)

            if result.one_or_none() is not None:
                return True
            return False

    def validate_redirect_uri(self, client_id, redirect_uri, request, *args, **kwargs):
        # Is the client allowed to use the supplied redirect_uri? i.e. has
        # the client previously registered this EXACT redirect uri.
        with Session(engine) as session:
            statement = select(AccessClient).where(AccessClient.client_id==client_id)
            result = session.exec(statement)

            if result.one_or_none() is not None:
                return redirect_uri in result.one_or_none().redirect_uris # type: ignore
            return False

    def get_default_redirect_uri(self, client_id, request, *args, **kwargs):
        # The redirect used if none has been supplied.
        # Prefer your clients to pre register a redirect uri rather than
        # supplying one on each authorization request.
        with Session(engine) as session:
            statement = select(AccessClient).where(AccessClient.client_id==client_id)
            result = session.exec(statement)

            client: Optional[AccessClient] = result.one_or_none()

            return client.default_redirect_uri # type: ignore

    def validate_scopes(self, client_id, scopes, _, request, *args, **kwargs):
        # Is the client allowed to access the requested scopes?
        with Session(engine) as session:
            statement = select(AccessClient).where(AccessClient.client_id==client_id)
            result = session.exec(statement)

            client: Optional[AccessClient] = result.one_or_none()

            for scope in scopes:
                if scope not in client.scopes: # type: ignore
                    return False
                
            return True

    def get_default_scopes(self, client_id, request, *args, **kwargs):
        # Scopes a client will authorize for if none are supplied in the
        # authorization request.
        with Session(engine) as session:
            statement = select(AccessClient).where(AccessClient.client_id==client_id)
            result = session.exec(statement)

            client: Optional[AccessClient] = result.one_or_none()

            return client.default_scopes # type: ignore


    def validate_response_type(self, client_id, response_type, _, request, *args, **kwargs):
        # Clients should only be allowed to use one type of response type, the
        # one associated with their one allowed grant type.
        # In this case it must be "code".
        with Session(engine) as session:
            statement = select(AccessClient).where(AccessClient.client_id==client_id)
            result = session.exec(statement) 

            client: Optional[AccessClient] = result.one_or_none()

            return client.response_type is response_type # type: ignore

    # Post-authorization

    def save_authorization_code(self, client_id, code, request, *args, **kwargs):
        # Remember to associate it with request.scopes, request.redirect_uri
        # request.client and request.user (the last is passed in
        # post_authorization credentials, i.e. { 'user': request.user}.
        with Session(engine) as session:
            statement = select(AccessClient).where(AccessClient.client_id==client_id)
            result = session.exec(statement) 

            client: Optional[AccessClient] = result.one_or_none()

            token = AuthorizationToken(client_id=client.client_id, user_id=client.user_id, )

    # Token request

    def client_authentication_required(self, request, *args, **kwargs):
        # Check if the client provided authentication information that needs to
        # be validated, e.g. HTTP Basic auth
        pass

    def authenticate_client(self, request, *args, **kwargs):
        # Whichever authentication method suits you, HTTP Basic might work
        pass

    def authenticate_client_id(self, client_id, request, *args, **kwargs):
        # The client_id must match an existing public (non-confidential) client
        pass

    def validate_code(self, client_id, code, client, request, *args, **kwargs):
        # Validate the code belongs to the client. Add associated scopes
        # and user to request.scopes and request.user.
        pass

    def confirm_redirect_uri(self, client_id, code, redirect_uri, client, request, *args, **kwargs):
        # You did save the redirect uri with the authorization code right?
        pass

    def validate_grant_type(self, client_id, grant_type, client, request, *args, **kwargs):
        # Clients should only be allowed to use one type of grant.
        # In this case, it must be "authorization_code" or "refresh_token"
        pass

    def save_bearer_token(self, token, request, *args, **kwargs):
        # Remember to associate it with request.scopes, request.user and
        # request.client. The two former will be set when you validate
        # the authorization code. Don't forget to save both the
        # access_token and the refresh_token and set expiration for the
        # access_token to now + expires_in seconds.
        pass

    def invalidate_authorization_code(self, client_id, code, request, *args, **kwargs):
        # Authorization codes are use once, invalidate it when a Bearer token
        # has been acquired.
        pass

    # Protected resource request

    def validate_bearer_token(self, token, scopes, request):
        # Remember to check expiration and scope membership
        pass

    # Token refresh request

    def get_original_scopes(self, refresh_token, request, *args, **kwargs):
        # Obtain the token associated with the given refresh_token and
        # return its scopes, these will be passed on to the refreshed
        # access token if the client did not specify a scope during the
        # request.
        pass