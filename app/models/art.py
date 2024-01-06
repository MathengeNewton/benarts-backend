from flask_login import UserMixin
from app.extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from sqlalchemy import func, desc, not_
from sqlalchemy.orm import relationship, joinedload


class Categories(UserMixin, db.Model):
    __tablename__ = 'categories'
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    name = db.Column(db.String(64))
    description = db.Column(db.String(128), nullable=True)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, server_default=func.now())
    updated_at = db.Column(db.Date)


    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    @classmethod
    def get_category_by_id(cls, category_id):
        return cls.query.get(category_id)
    
    @classmethod
    def delete_category_and_art(cls, category_id):
        category = cls.query.get(category_id)
        if category:
            db.session.delete(category)
            db.session.commit()
            


class Art(UserMixin, db.Model):
    __tablename__ = 'art'
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(128), nullable=True)
    price = db.Column(db.Integer)
    url = db.Column(db.String(128), nullable=False)
    category_id = db.Column(UUID(as_uuid=True))
    sold = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, server_default=func.now())
    updated_at = db.Column(db.Date, nullable=True)
    categories = relationship('Categories', foreign_keys='Art.category_id', primaryjoin="Art.category_id == Categories.id")

    def __init__(self, name, description, created_at):
        self.name = name
        self.description = description
        self.created_at = created_at
    
    @classmethod
    def get_available_art(cls):
        subquery = db.session.query(Reservations.art_id).distinct()
        return (
            cls.query
            .options(joinedload('categories'))
            .outerjoin(Categories, cls.category_id == Categories.id)
            .add_columns(Categories.name)
            .filter(cls.sold.is_(False))
            .filter(not_(cls.id.in_(subquery)))
            .order_by(cls.created_at.desc())
            .all()
        )
    
    @classmethod
    def get_sold_art(cls):
        return cls.query.filter_by(sold=False).all()
    
class Reservations(UserMixin, db.Model):
    __tablename__ = 'reservations'
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    buyer_name = db.Column(db.String(64))
    buyer_email = db.Column(db.String(64))
    buyer_phone = db.Column(db.String(64))
    art_id = db.Column(UUID(as_uuid=True))
    price = db.Column(db.Integer)
    narration = db.Column(db.String(500))
    status = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, server_default=func.now())
    updated_at = db.Column(db.Date, nullable=True)
    art = relationship('Art', foreign_keys='Reservations.art_id', primaryjoin="Reservations.art_id == Art.id") 

    def __init__(self, buyer_name, buyer_email, buyer_phone, art_id, price, narration):
        self.buyer_name = buyer_name
        self.buyer_email = buyer_email
        self.buyer_phone = buyer_phone
        self.art_id = art_id
        self.price = price
        self.narration = narration
    
    @classmethod
    def get_pending_reservations(cls):
        return cls.query.filter_by(status=False).all()

    @classmethod
    def get_reservation_by_phone(cls, phone_number):
        return (
            cls.query
            .filter_by(buyer_phone=phone_number)
            .filter_by(status=False)
            .order_by(desc(cls.created_at))
            .first()
        )
        
class CustomOrders(UserMixin, db.Model):
    __tablename__ = 'custom_orders'
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    buyer_name = db.Column(db.String(64))
    buyer_email = db.Column(db.String(64))
    buyer_phone = db.Column(db.String(64))
    price = db.Column(db.Integer, default=0)
    narration = db.Column(db.String(500))
    photo_url = db.Column(db.String(128))
    status = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, server_default=func.now())
    updated_at = db.Column(db.Date, nullable=True)

    def __init__(self, buyer_name, buyer_email, buyer_phone, photo_url, price, narration):
        self.buyer_name = buyer_name
        self.buyer_email = buyer_email
        self.buyer_phone = buyer_phone
        self.photo_url = photo_url
        self.price = price
        self.narration = narration
    
    @classmethod
    def get_pending_orders(cls):
        return cls.query.filter_by(status=False).all()

    @classmethod
    def get_pending_order_by_phone(cls, phone_number):
        return (
            cls.query
            .filter_by(buyer_phone=phone_number)
            .filter_by(status=False)
            .order_by(desc(cls.created_at))
        )