"""empty message

Revision ID: 5244e613828a
Revises: f20af7574337
Create Date: 2025-05-30 12:03:08.172260

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5244e613828a'
down_revision = 'f20af7574337'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('users_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password_hash', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key', postgresql_include=[], postgresql_nulls_not_distinct=False),
    sa.UniqueConstraint('username', name='users_username_key', postgresql_include=[], postgresql_nulls_not_distinct=False),
    postgresql_ignore_search_path=False
    )
    op.create_table('tasks',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='tasks_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='tasks_pkey')
    )
    # ### end Alembic commands ###
