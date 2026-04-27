from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
    
class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Member(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)

    def __repr__(self):
        return '<Member {}>'.format(self.email)
    
class Book(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
    author: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
    total_copies: so.Mapped[int] = so.mapped_column()
    available_copies: so.Mapped[int] = so.mapped_column()

    __table_args__ = (sa.UniqueConstraint('title', 'author', name='unique_book_title_author'),)

    def __repr__(self):
        return '<Book {} by {}>'.format(self.title, self.author)