import pytest
import requests

@pytest.fixture
def update_result_todb(request):
        print('In update_result_toDB')
        def _fin():
                try:
                    print(request.node.rep_call.passed)
                    if(request.node.rep_call.passed):
                        print('Result updated to DB successfully')
                    else:
                        print('test failed')
                                                                     
                except:
                       print ('exception raised')
        request.addfinalizer(_fin)
        return _fin

def test_failure(update_result_todb):
    print('test_failure')
    assert 1 == 0
def test_success(update_result_todb):
    print('test_success')
    assert 0 == 0