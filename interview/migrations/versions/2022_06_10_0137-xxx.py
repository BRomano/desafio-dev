"""stores

Revision ID: 695a74afbced
Revises: 61352d344a3c
Create Date: 2022-04-17 01:37:33.290446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61352d344a3d'
down_revision = '695a74afbced'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE USER 'spm-user'@'%' IDENTIFIED BY 'spm-password'")


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###
