"""Calculatuions model

Revision ID: e7c95c5cbc1b
Revises: 402a7a5e9e14
Create Date: 2024-11-10 20:55:08.731501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7c95c5cbc1b'
down_revision = '402a7a5e9e14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_data_set', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.TEXT(),
               type_=sa.Integer(),
               existing_nullable=True)
        batch_op.drop_index('ix_user_data_set_name_of_the_feature')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_data_set', schema=None) as batch_op:
        batch_op.create_index('ix_user_data_set_name_of_the_feature', ['name_of_the_feature'], unique=1)
        batch_op.alter_column('user_id',
               existing_type=sa.Integer(),
               type_=sa.TEXT(),
               existing_nullable=True)

    # ### end Alembic commands ###
