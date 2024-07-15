"""Add RADIUS option to enforce Message-Autenticator attribute

Revision ID: 7d82d8b680a9
Revises: 0d011e94a8e8
Create Date: 2024-07-15 17:25:38.602934

"""

# revision identifiers, used by Alembic.
revision = '7d82d8b680a9'
down_revision = '0d011e94a8e8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    try:
        # ### commands auto generated by Alembic - please adjust! ###
        op.add_column('radiusserver', sa.Column('enforce_ma', sa.Boolean(), nullable=True))
        # ### end Alembic commands ###
    except Exception as exx:
        print("Could not add column 'enforce_ma' in table radiusserver")
        print(exx)

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('radiusserver', 'enforce_ma')
    # ### end Alembic commands ###