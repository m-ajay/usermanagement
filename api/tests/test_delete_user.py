from rest_framework import test, status

from users.models import User


class TestDeleteUser(test.APITestCase):

    def setUp(self) -> None:
        super(TestDeleteUser, self).setUp()
        self.api_client = test.APIClient()

    def test_it_deletes_user(self):
        user = User.objects.create(
            email='john.doe@gmail.com',
            first_name='Bob',
            last_name='Duster',
        )

        response = self.api_client.delete(
            f'/api/users/{user.id}/',
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertIsNone(User.objects.filter(id=user.id).first())

    def test_when_user_id_doesnt_exists_throws_not_found_error(self):
        User.objects.create(
            email='john.doe@gmail.com',
            first_name='Bob',
            last_name='Duster',
        )
        response = self.api_client.delete(
            f'/api/users/-1/',
            format='json',
        )

        users = User.objects.filter(email='john.doe@gmail.com')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(users.count(), 1)
