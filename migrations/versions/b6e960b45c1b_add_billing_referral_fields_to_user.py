"""Add billing & referral fields to User

Revision ID: b6e960b45c1b
Revises: 
Create Date: 2025-05-04 12:13:14.005911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6e960b45c1b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('stripe_customer_id', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('stripe_subscription_id', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('plan', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('tokens', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('referral_code', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('referred_by_id', sa.Integer(), nullable=True))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
        batch_op.create_unique_constraint(None, ['referral_code'])
        batch_op.create_foreign_key(None, 'user', ['referred_by_id'], ['id'])
        batch_op.drop_column('drive_folder_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('drive_folder_id', sa.VARCHAR(length=300), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
        batch_op.drop_column('referred_by_id')
        batch_op.drop_column('referral_code')
        batch_op.drop_column('tokens')
        batch_op.drop_column('plan')
        batch_op.drop_column('stripe_subscription_id')
        batch_op.drop_column('stripe_customer_id')

    # ### end Alembic commands ###
