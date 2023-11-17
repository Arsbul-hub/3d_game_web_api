"""empty message

Revision ID: e151984f50e2
Revises: 
Create Date: 2023-09-25 12:12:13.041933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e151984f50e2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('servers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('invite_code', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('servers', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_servers_name'), ['name'], unique=True)

    op.create_table('worlds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path', sa.String(), nullable=True),
    sa.Column('server_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['server_id'], ['servers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('worlds')
    with op.batch_alter_table('servers', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_servers_name'))

    op.drop_table('servers')
    # ### end Alembic commands ###