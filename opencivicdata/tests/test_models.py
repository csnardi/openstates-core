import pytest
from ..models import (Jurisdiction, JurisdictionSession, Division,
                      Organization, OrganizationIdentifier, OrganizationName,
                      OrganizationContactDetail, OrganizationSource,
                      Person, PersonIdentifier, PersonName, PersonContactDetail, PersonLink,
                      PersonSource,
                      Post, PostContactDetail, PostLinks,
                      Membership, MembershipContactDetail, MembershipLink)


def test_division_subtypes_from_id():

    # simplest case
    assert Division.subtypes_from_id('ocd-division/country:us') == ({'country': 'us'}, 1)

    # ocd-divison part is optional
    assert Division.subtypes_from_id('country:us/state:ak/county:wild') == (
        {'country': 'us', 'subtype1': 'state', 'subid1': 'ak', 'subtype2': 'county',
         'subid2': 'wild'}, 3)

    # country is not optional
    with pytest.raises(ValueError):
        Division.subtypes_from_id('state:nc/city:raleigh')


@pytest.mark.django_db
def test_division_create():
    division_id = 'ocd-division/country:us/state:ak/county:wild'
    d = Division.objects.create(id=division_id, display_name='Wild County')
    assert d.country == 'us'
    assert d.subtype1 == 'state'
    assert d.subid1 == 'ak'
    assert d.subtype2 == 'county'
    assert d.subid2 == 'wild'
    assert division_id in str(d)


@pytest.mark.django_db
def test_division_children_of():
    us = Division.objects.create('ocd-division/country:us', display_name='US')
    ak = Division.objects.create('ocd-division/country:us/state:ak', display_name='Alaska')
    wild = Division.objects.create('ocd-division/country:us/state:ak/county:wild',
                                   display_name='Wild')
    mild = Division.objects.create('ocd-division/country:us/state:ak/county:mild',
                                   display_name='Mild')
    wild_a = Division.objects.create('ocd-division/country:us/state:ak/county:wild/place:a',
                                     display_name='A')
    wild_b = Division.objects.create('ocd-division/country:us/state:ak/county:wild/place:b',
                                     display_name='B')
    school = Division.objects.create('ocd-division/country:us/state:ak/county:wild/school:a',
                                     display_name='A')
    mild_a = Division.objects.create('ocd-division/country:us/state:ak/county:mild/place:a',
                                     display_name='A')
    mild_a = Division.objects.create('ocd-division/country:us/state:ak/county:mild/place:a/x:y',
                                     display_name='A')

    # simplest ==
    assert Division.objects.children_of('ocd-division/country:us')[0].id == ak.id

    # 3 divisions within wild county
    assert (Division.objects.children_of('ocd-division/country:us/state:ak/county:wild').count() ==
            3)

    # only one school in wild county
    assert Division.objects.children_of('ocd-division/country:us/state:ak/county:wild',
                                        subtype='school').count() == 1

    # 6 divisions beneath alaska up to 2 levels
    assert Division.objects.children_of('ocd-division/country:us/state:ak', depth=2).count() == 6

    # 7 divisions beneath alaska up to 3 levels
    assert Division.objects.children_of('ocd-division/country:us/state:ak', depth=3).count() == 7
