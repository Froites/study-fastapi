from http import HTTPStatus


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'Joao',
            'email': 'Joao@gmail.com',
            'password': 'secret',
        },
    )

    # Verificar se o usuário foi criado com sucesso
    assert response.status_code == HTTPStatus.CREATED

    # Validar User Public
    assert response.json() == {
        'username': 'Joao',
        'email': 'Joao@gmail.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'Joao',
                'email': 'Joao@gmail.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'Joao2',
            'email': 'Joao2@gmail.com',
            'password': 'secret',
        },
    )

    assert response.json() == {
        'username': 'Joao2',
        'email': 'Joao2@gmail.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted!'}
