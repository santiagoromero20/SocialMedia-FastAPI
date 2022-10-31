"""add content column to posts table

Revision ID: 693c07e16307
Revises: 6cd57811fa46
Create Date: 2022-10-31 16:13:47.941061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '693c07e16307'
down_revision = '6cd57811fa46'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.column("content", sa.String(), nullable=False))
    pass

def downgrade():
    op.drop_column("posts", "content")
    pass
