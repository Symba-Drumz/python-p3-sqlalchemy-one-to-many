"""create game and review tables

Revision ID: 0001_create_game_and_review
Revises: 
Create Date: 2024-06-01 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0001_create_game_and_review'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'games',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('title', sa.String(), nullable=True),
        sa.Column('genre', sa.String(), nullable=True),
        sa.Column('platform', sa.String(), nullable=True),
        sa.Column('price', sa.Integer(), nullable=True),
    )
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('score', sa.Integer(), nullable=True),
        sa.Column('comment', sa.String(), nullable=True),
        sa.Column('game_id', sa.Integer(), sa.ForeignKey('games.id'), nullable=True),
    )

def downgrade() -> None:
    op.drop_table('reviews')
    op.drop_table('games')
