import pytest

from teams.models import Team, Person
from teams.serializers import PersonSerializer


@pytest.fixture
def team():
    return Team.objects.create(name="Test Team")


@pytest.mark.django_db
def test_create_person_success(team):
    """
    Test of successful user creation
    """
    data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'team': team.id,
    }
    serializer = PersonSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    person = serializer.save()
    assert person.first_name == 'John'
    assert person.last_name == 'Doe'
    assert person.email == 'john.doe@example.com'


@pytest.mark.django_db
def test_invalid_person_name_with_numbers(team):
    """
    Name validation test with numbers
    """
    data = {
        'first_name': 'John123',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'team': team.id,
    }
    serializer = PersonSerializer(data=data)
    assert not serializer.is_valid()
    assert 'first_name' in serializer.errors


@pytest.mark.django_db
def test_unique_email_validation(team):
    """
    `Email uniqueness test
    """
    Person.objects.create(first_name="Jane", last_name="Doe", email="john.doe@example.com", team=team)
    data = {
        'first_name': 'John',
        'last_name': 'Smith',
        'email': 'john.doe@example.com',
        'team': team.id,
    }
    serializer = PersonSerializer(data=data)
    assert not serializer.is_valid()
    assert 'email' in serializer.errors
