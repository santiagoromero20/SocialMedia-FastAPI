"""add last few columns to posts table

Revision ID: 68420ca38a27
Revises: 9aef936ce853
Create Date: 2022-10-31 16:48:02.230224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68420ca38a27'
down_revision = '9aef936ce853'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    op.add_column("posts",sa.Column("content", sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'content')
    pass
