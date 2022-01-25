from collections import namedtuple
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

from pydantic import BaseModel


@dataclass
class ModelData:
    total_views_in_session: int
    time_in_minutes_in_session: int
    products_viewed_in_session: int
    user_bought_to_total_sessions_ratio: float


class UserEvent(BaseModel):
    session_id: int
    user_id: int
    product_id: int
    purchase_id: Optional[int] = None
    timestamp: str = datetime.now().isoformat()
    event_type: str = "VIEW_PRODUCT"
    offered_discount: int = 0


DataToModel = namedtuple("DataToModel", [
    'total_views',
    'time_in_minutes',
    'unique_products',
    'user_bought_to_total_sessions_ratio'
])
