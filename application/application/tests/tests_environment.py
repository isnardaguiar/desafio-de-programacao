from django.test import TestCase
from django.conf import settings
import os


class EnviromnentTest(TestCase):
    def test_if_dotenv_exists(self):
        target = '.env'
        path = os.path.join(settings.BASE_DIR, target)
        
        self.assertTrue(os.path.exists(path), f'O arquivo {target} não existe')

    def test_if_environment_variables_exists(self):
        db_name = os.getenv('DB_NAME')
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')

        self.assertIsNotNone(db_name, 'O nome do banco de dados não foi informado')
        self.assertIsNotNone(db_user, 'O usuário do banco de dados não foi informado')
        self.assertIsNotNone(db_password, 'A senha do banco de dados não foi informada')
        self.assertIsNotNone(db_host, 'O host do banco de dados não foi informado')
        self.assertIsNotNone(db_port, 'A porta do banco de dados não foi informada')

