from fast_studies.models.models import User
from sqlalchemy import select


def test_create_user(session):
    user = User(
        username='Joao',
        email='joao@gmail.com',
        password='teste123',
    )
    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'joao@gmail.com'))

    assert result.username == 'Joao'
