from __future__ import annotations
import hashlib
import typing
import sqlalchemy as sa
from typing import List
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import (
    DeclarativeBase,
    mapped_column,
    relationship,
    sessionmaker,
    Mapped,
)
from src.utils.helper import init_dest_engine


class Base(DeclarativeBase):
    pass


class Campaigns(Base):
    __tablename__ = "campaigns"

    campaign_id : Mapped[int] = mapped_column(primary_key=True)
    name        : Mapped[str] = mapped_column(sa.String)
    campaign_type: Mapped[str] = mapped_column(sa.String)
    start_date  : Mapped[str] = mapped_column(sa.String(30))
    
    campitems_camp: Mapped[List['CampaignItems']] = relationship(back_populates='camp_campitems')


class CampaignItems(Base):
    __tablename__ = "campaign_items"

    campaign_item_id: Mapped[int] = mapped_column(primary_key=True)
    campaign_id     : Mapped[int] = mapped_column(ForeignKey("campaigns.campaign_id"))
    campaign_type   : Mapped[str] = mapped_column(sa.String)
    campaign_item   : Mapped[str] = mapped_column(sa.String)

    camp_campitems: Mapped['Campaigns'] = relationship(back_populates='campitems_camp')

class Products(Base):
    __tablename__ = "products"

    product_id  : Mapped[int] = mapped_column(primary_key=True)
    name        : Mapped[str] = mapped_column(sa.String)
    price       : Mapped[int] = mapped_column(sa.Float)
    description : Mapped[str] = mapped_column(sa.String)
    category_id : Mapped[int] = mapped_column(ForeignKey('categories.category_id'))
    image_url   : Mapped[str] = mapped_column(sa.String)

    categories_product  : Mapped['Categories'] = relationship(back_populates='product_category')
    tags_product        : Mapped[List['Tags']] = relationship(back_populates='product_tags')
    cartitems_products  : Mapped[List['CartItems']] = relationship(back_populates='products_cartitems')


class Categories(Base):
    __tablename__ = "categories"

    category_id : Mapped[int] = mapped_column(primary_key=True)
    name        : Mapped[str] = mapped_column(sa.String)
    
    product_category: Mapped[List['Products']] = relationship(back_populates='categories_product')

class Tags(Base):
    __tablename__ = "tags"

    tag_id      : Mapped[str] = mapped_column(primary_key=True)
    tag         : Mapped[str] = mapped_column(sa.String)
    product_id  : Mapped[int] = mapped_column(ForeignKey('products.product_id'))
    
    
    product_tags: Mapped['Products'] = relationship(back_populates='tags_product')


class Customers(Base):
    __tablename__ = "customers"

    cust_id     : Mapped[int] = mapped_column(primary_key=True)
    name        : Mapped[str] = mapped_column(sa.String)
    phone       : Mapped[str] = mapped_column(sa.String(30))
    address     : Mapped[str] = mapped_column(sa.String)
    city        : Mapped[str] = mapped_column(sa.String(30))
    province    : Mapped[str] = mapped_column(sa.String(30))
    
    cart_customer  : Mapped[List['Carts']] = relationship(back_populates='customer_cart')
    

class Carts(Base):
    __tablename__ = "carts"

    cart_id     : Mapped[int] = mapped_column(primary_key=True)
    cust_id     : Mapped[int] = mapped_column(ForeignKey('customers.cust_id'))
    trx_date    : Mapped[str] = mapped_column(sa.String)
    
    customer_cart  : Mapped['Customers'] = relationship(back_populates='cart_customer')
    cartitems_carts  : Mapped[List['CartItems']] = relationship(back_populates='carts_cartitems')


class CartItems(Base):
    __tablename__ = "cart_items"

    cart_item_id: Mapped[int] = mapped_column(primary_key=True)
    cart_id     : Mapped[int] = mapped_column(ForeignKey('carts.cart_id'))
    product_id  : Mapped[int] = mapped_column(ForeignKey('products.product_id'))
    order_amt   : Mapped[int] = mapped_column(sa.Integer)
    
    carts_cartitems  : Mapped['Carts'] = relationship(back_populates='cartitems_carts')
    products_cartitems: Mapped['Products'] = relationship(back_populates='cartitems_products')


conn = init_dest_engine()
Base.metadata.create_all(conn)