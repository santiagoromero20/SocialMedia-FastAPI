"""create posts table

Revision ID: 6cd57811fa46
Revises: 
Create Date: 2022-10-31 15:48:41.157972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cd57811fa46'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False,
                    primary_key=True), sa.Column("title", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table("posts")
    pass
