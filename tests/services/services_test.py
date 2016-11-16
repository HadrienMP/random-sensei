from application.services import build_message
from application.services.argument_extractor import Arguments
from application import app

MESSAGE_SERVICE = 'application.services.random_senseis_message'


def test_should_return_manual_when_manual_is_true_in_arguments(mocker):
    # SETUP
    arguments = Arguments()
    arguments.manual = True
    mocker.patch(MESSAGE_SERVICE)
    
    # TEST
    message = build_message(room='test', arguments=arguments)
    
    # ASSERT
    assert message == app.config['MANUAL']


def test_should_delegate_message_building_to_sensei_message_service_otherwise(mocker):
    # SETUP
    arguments = Arguments()
    arguments.manual = False
    mock_message_service = mocker.patch(MESSAGE_SERVICE)
    
    # TEST
    message = build_message(room='test', arguments=arguments)
    
    # ASSERT
    assert message != app.config['MANUAL']
    assert mock_message_service.called