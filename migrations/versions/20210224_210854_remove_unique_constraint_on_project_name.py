"""remove unique constraint on project name

Revision ID: 706a8e104643
Revises: 122462fb7deb
Create Date: 2021-02-24 21:08:54.022320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '706a8e104643'
down_revision = '122462fb7deb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('projects_name_key', 'projects', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('projects_name_key', 'projects', ['name'])
    # ### end Alembic commands ###
