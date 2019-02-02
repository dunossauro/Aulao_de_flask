from unittest import TestCase
from app import create_app, db, User
from flask import url_for


class TestAPI(TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def test_api_user_deve_retornar_um_dicionario_vazio(self):
        entrada = {
            'email': 'foo@bar.com',
            'username': 'foo',
            'password': 'bar'
        }

        response = self.client.post(
            url_for('api.cadastro_usuario'), json=entrada
        )

        # Insere só pra checar ^
        exp = User(email='foo@bar.com', username='foo', password='bar')

        response = self.client.get(
            url_for('api.api_user', email='foo@bar.com')
        )
        self.assertEqual(str(exp), response.json['user'])

    def test_api_user_deve_iserir_usuario_na_base(self):
        entrada = {
            'email': 'foo@bar.com',
            'username': 'foo',
            'password': 'bar'
        }
        saida = User(email='foo@bar.com', username='foo', password='bar')
        response = self.client.post(
            url_for('api.cadastro_usuario'), json=entrada
        )
        resultado = User.query.filter_by(email='foo@bar.com').first()

        self.assertEqual(str(resultado), str(saida))


    def tearDown(self):
        db.drop_all()
