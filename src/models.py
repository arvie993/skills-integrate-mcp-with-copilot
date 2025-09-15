from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import UniqueConstraint


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    role: str = Field(default="student", index=True)

    signups: List["Signup"] = Relationship(back_populates="user")


class Activity(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    description: str
    schedule: str
    capacity: int = Field(default=0)

    signups: List["Signup"] = Relationship(back_populates="activity")


class Signup(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    activity_id: int = Field(foreign_key="activity.id", index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)

    __table_args__ = (UniqueConstraint("user_id", "activity_id", name="uq_signup_user_activity"),)

    user: Optional[User] = Relationship(back_populates="signups")
    activity: Optional[Activity] = Relationship(back_populates="signups")
