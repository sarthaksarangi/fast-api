from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from database import get_session
from models import Order, OrderCreate, OrderStatus, OrderUpdate


router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=Order)
def create_order(order: OrderCreate, session: Session = Depends(get_session)):
    db_order = Order(**order.model_dump())
    session.add(db_order)
    session.commit()
    session.refresh(db_order)
    return db_order

@router.get("/", response_model=list[Order])
def list_orders(
    status: OrderStatus | None = Query(default=None, description="Filter by status"),
    created_date: str | None = Query(default=None, description="Filter by creation date"),
    skip: int = Query(0, ge = 0),
    limit: int = Query(20, ge = 1, le=100),
    session: Session = Depends(get_session)
    ):
    query = select(Order)
    if status:
        query = query.where(Order.status == status)

    if created_date:
        start = datetime.combine(created_date, datetime.min.time()) # type: ignore
        end = datetime.combine(created_date, datetime.max.time()) # type: ignore
        query = query.where(Order.created_at >= start, Order.created_at <= end)

    query = query.offset(skip).limit(limit)
    return session.exec(query).all()


