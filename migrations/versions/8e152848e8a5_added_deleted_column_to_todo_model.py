"""Added deleted column to Todo model.

Revision ID: 8e152848e8a5
Revises: 3ea33eee1690
Create Date: 2024-03-28 16:28:42.239554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e152848e8a5'
down_revision = '3ea33eee1690'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('deleted', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.drop_column('deleted')

    # ### end Alembic commands ###
