"""Your migration message

Revision ID: d9c4628b0cf5
Revises: 
Create Date: 2025-01-06 03:24:07.514811

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9c4628b0cf5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('testObj',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_testObj_id'), 'testObj', ['id'], unique=False)
    op.create_index(op.f('ix_testObj_title'), 'testObj', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_testObj_title'), table_name='testObj')
    op.drop_index(op.f('ix_testObj_id'), table_name='testObj')
    op.drop_table('testObj')
    # ### end Alembic commands ###
