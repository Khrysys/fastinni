from datetime import datetime, timedelta
from os import getenv
from typing import Optional, Any
from jwt import decode, encode, ExpiredSignatureError
from sqlmodel import SQLModel, Field, Session, select
from . import engine

class User(SQLModel, table=True): # type: ignore
    # -----------------------------------------------------
    # --------- LEVEL ONE REQUIREMENTS
    # -----------------------------------------------------
    
    # These are at level 1 requirements of a User (forced)
    # Some of these are specified as Optional, however this is due to the way Pydantic data models form constructors. 
    # When they are not Optional, it is required to specify the value when creating the object, however 
    # This would override things that are automatically filled by the database or things that would require 
    # future user input but are not required for user operation.
    # This is how Users are organized in the database
    # This is the most important field, as the internal server uses IDs to check ownership and table checks
    id: Optional[int] = Field(default=None, primary_key=True, unique=True)
    # This is a toggle on if someone not on your friends list goes to your profile, if anything besides
    # the User ID and tag are shown
    public_profile: Optional[bool] = Field(default=True)
    # The user tag is what is primarily used for API requests. They should be unique, utf-8 encoded, all-lowercase,
    # easily memorizable strings since they are how pretty much everything happens. Friend lists link to tags instead of IDs
    # Its alias is username so it should be identifiable from both columns
    tag: str = Field(alias="username", unique=True)
    
    # -----------------------------------------------------
    # --------- LEVEL TWO REQUIREMENTS
    # -----------------------------------------------------
    # These are at level 2 requirement, (highly recommended but not required).
    # Three of these has a boolean toggle if it is publicly shown on your profile (phone, email, address)
    # This toggle has no effect if the main public_profile is false.
    # You can use many different ways of storing a phone number, here a string is used to give the potential for
    # Extensions and other country codes.
    phone: Optional[str] = Field(default=None, unique=True)
    public_phone: Optional[bool] = Field(default=False)
    # Your email is a level 2 requirement and not a level 3 requirement since if your email is not linked, someone else could use it
    # to access your Google Data through the OAuth scopes.
    email: Optional[str] = Field(default=None, unique=True)
    public_email: Optional[bool] = Field(default=None)
    # Your address is here mostly as an example. Nothing really needs it, but it could be useful in a site that involves purchases
    # to calculate sales tax. This is not unique, as multiple people in the same house may use this site.
    address: Optional[str] = Field(default=None)
    public_address: Optional[bool] = Field(default=None)
    
    # The password hash is only at a level 2 requirement due to OAuth scopes potentially being used instead.
    # This is a hex code representing the password.
    # We also don't want this to be unique, counterintuitively, since the password is salted on a per-user basis, 
    # setting the password to being unique would be a strong clue-in to a hash collision. 
    # Attackers should not be able to know anything about this aside from it exists.
    # We could simply throw a 400 and make the user restart since the hash would change, 
    # but that seems a bit excessive when scaling.
    password_hash: Optional[str] = Field(default=None)
    # The profile image is exactly what it seems like. When this is None, it signals to load the default
    # image from /img/default_profile.png
    profile_image: Optional[str] = Field(default=None)
    
    # -----------------------------------------------------
    # --------- LEVEL THREE REQUIREMENTS
    # -----------------------------------------------------
    # Level three is effectively just for OAuth scopes (potentially useful but should have no detriment if not found)
    # These ensure that login is proper and not cracked.
    google_id: Optional[str] = Field(default=None, unique=True)
    
    # -----------------------------------------------------
    # --------- LEVEL FOUR REQUIREMENTS
    # -----------------------------------------------------
    # Level four is for cosmetic settings (completely optional)
    theme: Optional[str] = Field(default="dark")

    

    def get_own_data(self):
        # Here we can load all of the data since there are no access restrictions since we are accessing ourselves
        return self.model_dump(exclude="password_hash"), 200 # type: ignore
    
    def get_public_data(self):
        if not self.public_profile:
            return {
                "id": self.id,
                "profile_image": self.profile_image,
                "tag": self.tag
            }
        else:
            return {
                "id": self.id,
                "profile_image": self.profile_image,
                "tag": self.tag,
                "phone" : self.phone if self.public_phone else None,
                "email":  self.email if self.public_email else None,
                "address": self.address if self.public_address else None,
                "profile_image": self.profile_image,
            }
        
    def create_login_jwt(self):
        secret = getenv("LOGIN_SECRET", "")

        data = {
            "id": self.id,
            "tag": self.tag,
            "password_hash": self.password_hash,
            "exp": datetime.utcnow() + timedelta(days=90),
            "nbf": datetime.utcnow()
        }

        return encode(data, secret, "HS256")
        
    @staticmethod
    def validate_jwt(jwt: str) -> bool | Any:
        secret = getenv("LOGIN_SECRET", "")
        try:
            data = decode(jwt, secret)
            id = data['id']
            tag = data['tag']
            password_hash = data['password_hash']
        except:
            return False

        
        with Session(engine) as session:
            statement = select(User).where(User.id==id).where(User.tag==tag).where(User.password_hash==password_hash)
            result = session.exec(statement)
            user = result.one_or_none()

            if user is not None: 
                return user
            return False