"""delete cost

Revision ID: 4f9856fa110f
Revises: 07d2a9b9b729
Create Date: 2023-04-03 16:15:54.951183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f9856fa110f'
down_revision = '07d2a9b9b729'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('consumption', 'cost')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('consumption', sa.Column('cost', sa.FLOAT(), nullable=False))
    # ### end Alembic commands ###
