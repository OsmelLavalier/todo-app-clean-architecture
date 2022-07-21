"""intial tables

Revision ID: 90996766a4e6
Revises:
Create Date: 2022-07-21 20:48:37.326156

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "90996766a4e6"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        table_name="todo",
        column_name="state",
        type_=mysql.VARCHAR(255),
        existing_type=mysql.TINYINT(unsigned=True),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "todo",
        sa.Column(
            "id", mysql.INTEGER(unsigned=True), autoincrement=True, nullable=False
        ),
        sa.Column(
            "created_at",
            mysql.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column("name", mysql.VARCHAR(length=255), nullable=False),
        sa.Column("data", mysql.VARCHAR(length=255), nullable=False),
        sa.Column(
            "user_id", mysql.INTEGER(unsigned=True), autoincrement=False, nullable=False
        ),
        sa.Column(
            "state",
            mysql.TINYINT(unsigned=True),
            server_default=sa.text("'0'"),
            autoincrement=False,
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], name="fk_todo_user_id"),
        sa.PrimaryKeyConstraint("id"),
        mysql_collate="utf8mb4_0900_ai_ci",
        mysql_default_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.create_table(
        "user",
        sa.Column(
            "id", mysql.INTEGER(unsigned=True), autoincrement=True, nullable=False
        ),
        sa.Column("username", mysql.VARCHAR(length=255), nullable=False),
        sa.Column("password", mysql.VARCHAR(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        mysql_collate="utf8mb4_0900_ai_ci",
        mysql_default_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.create_index("_user_username_uc_", "user", ["username"], unique=False)
    # ### end Alembic commands ###