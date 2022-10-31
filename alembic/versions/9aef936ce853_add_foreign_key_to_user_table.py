"""add foreign-key to user table

Revision ID: 9aef936ce853
Revises: de04add865e8
Create Date: 2022-10-31 16:38:20.019388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9aef936ce853'
down_revision = 'de04add865e8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users", local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraints("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
