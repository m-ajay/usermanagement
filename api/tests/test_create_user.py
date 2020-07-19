from rest_framework import test, status

from users.models import User


class TestCreateUser(test.APITestCase):

    def setUp(self) -> None:
        super(TestCreateUser, self).setUp()
        self.api_client = test.APIClient()

    def test_it_creates_user(self):
        response = self.api_client.post(
            '/api/users/',
            data=self._build_payload(),
            format='json',
        )

        user = User.objects.filter(email='john.doe@gmail.com').first()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(user)
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    def test_when_email_already_exists_it_throws_bad_request_error(self):
        User.objects.create(
            email='john.doe@gmail.com',
            first_name='Bob',
            last_name='Duster',
        )
        response = self.api_client.post(
            '/api/users/',
            data=self._build_payload(),
            format='json',
        )

        users = User.objects.filter(email='john.doe@gmail.com')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(users.count(), 1)

    def _build_payload(self):
        return {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@gmail.com',
        }
