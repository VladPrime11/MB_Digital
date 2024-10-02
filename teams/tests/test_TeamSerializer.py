import pytest

from teams.models import Team, Person
from teams.serializers import TeamSerializer


@pytest.mark.django_db
def test_create_team_success():
    """
    A test of successful team building
    """
    data = {'name': 'Marketing'}
    serializer = TeamSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    team = serializer.save()
    assert team.name == 'Marketing'

@pytest.mark.django_db
def test_unique_team_name_validation():
    """
    Team name uniqueness test
    """
    Team.objects.create(name="Development")
    data = {'name': 'Development'}
    serializer = TeamSerializer(data=data)
    assert not serializer.is_valid()
    assert 'name' in serializer.errors

@pytest.mark.django_db
def test_team_members_field():
    """
    Test field members for the command
    """
    team = Team.objects.create(name="Development")
    Person.objects.create(first_name="John", last_name="Doe", email="john.doe@example.com", team=team)
    Person.objects.create(first_name="Jane", last_name="Doe", email="jane.doe@example.com", team=team)

    serializer = TeamSerializer(instance=team)
    data = serializer.data
    assert len(data['members']) == 2
    assert data['members'][0]['first_name'] == 'John'
    assert data['members'][1]['first_name'] == 'Jane'
