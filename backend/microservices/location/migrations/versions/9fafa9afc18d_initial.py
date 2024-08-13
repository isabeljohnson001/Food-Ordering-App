"""initial

Revision ID: 9fafa9afc18d
Revises: 
Create Date: 2024-07-31 21:16:21.794914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fafa9afc18d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('driver_location',
    sa.Column('driver_id', sa.String(), nullable=False),
    sa.Column('latitude', sa.Float(precision=32), nullable=False),
    sa.Column('longitude', sa.Float(precision=32), nullable=False),
    sa.Column('accuracy', sa.Float(precision=32), nullable=True),
    sa.Column('speed', sa.Float(precision=32), nullable=True),
    sa.Column('bearing', sa.Float(precision=32), nullable=True),
    sa.Column('timestamp', sa.DateTime(timezone=True), nullable=False),
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('driver_location')
    # ### end Alembic commands ###
