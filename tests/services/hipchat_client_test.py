# -*-coding: UTF-8 -*-
from application.services import hipchat_client


def test_should_return_room_members_in_a_public_room(config):
    members = hipchat_client.get_room_members("3377850")
    assert members == ["virginie", "AliBELKADY", "AlaeddineBOUATTOUR", "Rom1", 
        "HadrienMensPellen", "Yohann", "CelineDanglet", "Leticia", 
        u"MatthieuLeMée", "Theo", "FabienHiegel", "pierrealain"]

def test_should_return_room_members_in_a_private_room(config):
    members = hipchat_client.get_room_members("2247343")
    assert members == ['AliBELKADY', 'HadrienMensPellen', 'FabienHiegel', 'CelineDanglet', 'pierrealain']


def test_should_return_empty_list_for_an_invalid_room_number(config):
    members = hipchat_client.get_room_members("-1")
    assert members == []
