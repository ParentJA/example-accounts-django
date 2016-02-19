# Third-party imports...
from lettuce import step, world

# Django imports...
from django.contrib.auth import get_user_model

User = get_user_model()


@step(r'I create the following users:')
def create_users(step):
    for data in step.hashes:
        User.objects.create_user(**data)


@step(r'I log in as "(.+)" using password "(.+)"')
def log_in_user_with_password(step, username, password):
    world.response = world.client.post('/api/v1/accounts/log_in/', {
        'username': username,
        'password': password
    })


@step(r'I log out')
def log_out_user(step):
    world.response = world.client.post('/api/v1/accounts/log_out/')


@step(r'I sign up using the following data')
def sign_up_user(step):
    world.response = world.client.post('/api/v1/accounts/sign_up/', data=step.hashes.first)
