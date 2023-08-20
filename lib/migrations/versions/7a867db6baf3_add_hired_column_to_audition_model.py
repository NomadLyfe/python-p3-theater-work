"""Add hired column to Audition Model

Revision ID: 7a867db6baf3
Revises: 10d167943fc9
Create Date: 2023-08-20 11:59:00.998881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a867db6baf3'
down_revision = '10d167943fc9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('auditions', sa.Column('hired', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('auditions', 'hired')
    # ### end Alembic commands ###