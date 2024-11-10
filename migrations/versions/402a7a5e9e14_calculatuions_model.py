"""Calculatuions model

Revision ID: 402a7a5e9e14
Revises: cad35a7f5d7d
Create Date: 2024-11-10 19:11:56.143478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '402a7a5e9e14'
down_revision = 'cad35a7f5d7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_data_set', schema=None) as batch_op:
        batch_op.add_column(sa.Column('n_samples', sa.String(length=10), nullable=True))
        batch_op.add_column(sa.Column('n_features', sa.String(length=10), nullable=True))
        batch_op.add_column(sa.Column('applicant', sa.String(length=5), nullable=True))
        batch_op.drop_column('frequency_2')
        batch_op.drop_column('probability_1')
        batch_op.drop_column('probability_2')
        batch_op.drop_column('frequency_1')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_data_set', schema=None) as batch_op:
        batch_op.add_column(sa.Column('frequency_1', sa.VARCHAR(length=10), nullable=True))
        batch_op.add_column(sa.Column('probability_2', sa.VARCHAR(length=5), nullable=True))
        batch_op.add_column(sa.Column('probability_1', sa.VARCHAR(length=5), nullable=True))
        batch_op.add_column(sa.Column('frequency_2', sa.VARCHAR(length=10), nullable=True))
        batch_op.drop_column('applicant')
        batch_op.drop_column('n_features')
        batch_op.drop_column('n_samples')

    # ### end Alembic commands ###