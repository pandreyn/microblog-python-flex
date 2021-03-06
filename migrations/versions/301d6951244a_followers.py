"""followers

Revision ID: 301d6951244a
Revises: 2b1dbac24b45
Create Date: 2018-02-15 13:44:50.614341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '301d6951244a'
down_revision = '2b1dbac24b45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
