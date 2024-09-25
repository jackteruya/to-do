from datetime import date

from sqlalchemy import BOOLEAN, Date, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from src.infra.database.config import Base


class ToDo(Base):
    """To Do Model"""

    __tablename__ = "todo"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(128))
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    completed: Mapped[str] = mapped_column(BOOLEAN, default=False)
    start_date: Mapped[date] = mapped_column(Date, nullable=True)
    end_date: Mapped[date] = mapped_column(Date, nullable=True)
    create_at: Mapped[date] = mapped_column(DateTime, default=func.now())
    update_at: Mapped[date] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )

    def __repr__(self):
        return f"ToDo: [id={self.id}, title={self.title}]"
