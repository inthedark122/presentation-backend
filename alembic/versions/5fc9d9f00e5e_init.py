"""Init

Revision ID: 5fc9d9f00e5e
Revises: 
Create Date: 2018-03-08 14:17:12.971485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fc9d9f00e5e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_engine1():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('content_project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('content_slide',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.Text(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['content_project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade_engine1():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('content_slide')
    op.drop_table('content_project')
    # ### end Alembic commands ###

