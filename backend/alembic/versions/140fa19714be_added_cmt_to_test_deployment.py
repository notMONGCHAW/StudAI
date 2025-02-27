"""added cmt to test deployment

Revision ID: 140fa19714be
Revises: d9c4628b0cf5
Create Date: 2025-01-06 23:53:27.002831

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '140fa19714be'
down_revision: Union[str, None] = 'd9c4628b0cf5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('testObj', sa.Column('cmt', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('testObj', 'cmt')
    # ### end Alembic commands ###
