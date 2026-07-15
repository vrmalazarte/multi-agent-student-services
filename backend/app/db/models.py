from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


class Thread(Base):
    __tablename__ = "threads"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )


class ThreadItem(Base):
    __tablename__ = "thread_items"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    thread_id: Mapped[int] = mapped_column(
        ForeignKey("threads.id"),
    )

    role: Mapped[str] = mapped_column(
        String(50),
    )

    content: Mapped[str] = mapped_column(
        Text,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )


class AgentRun(Base):
    __tablename__ = "agent_runs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    thread_id: Mapped[int] = mapped_column(
        ForeignKey("threads.id"),
    )

    agent_name: Mapped[str] = mapped_column(
        String(100),
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )


class SupportTicket(Base):
    __tablename__ = "support_tickets"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    thread_id: Mapped[int] = mapped_column(
        ForeignKey("threads.id"),
    )

    issue: Mapped[str] = mapped_column(
        Text,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="open",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )


class MemoryItem(Base):
    __tablename__ = "memory_items"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    thread_id: Mapped[int] = mapped_column(
        ForeignKey("threads.id"),
    )

    key: Mapped[str] = mapped_column(
        String(100),
    )

    value: Mapped[str] = mapped_column(
        Text,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )