import requests
import pytest

@pytest.fixture(scope ="function")
def  update_database(request):
        print('I am in update_database')
        print('testID' + testID)
        print('request'+ str(request))
        def _fin():
                try:
                        print(request.node.own_markers)   
                        marks = request.node.own_markers
                        mark_names = [m.args for m in marks]
                        print(marks)
                        testID = mark_names[2][0]  # 123 - it takes the test case marks as arguments in bottom to top approach
                        step = mark_names[2][1]  #9
                        print(testID)
                        print(str(step))
                        if(request.node.rep_call.passed):
                           print('test case success and update db with test case id and steps '+ testID + str(step))
                        else:
                            print('test case failed- no db udpate is required')
                    except:
                       print ('exception raised')
                       print('Failed to update TCDB: An exception occurred: {}'.format(error)) 
        request.addfinalizer(_fin)
        return _fin

class Test_getapi:   

   @pytest.mark.getapi('123' , 9)
   @pytest.mark.priority('1')
   @pytest.mark.google
   def test_get_api(self, update_tcdb):
      "GET request to url returns a 200"    
      url = 'http://google.com'
      resp = requests.get(url)
      log.info("GET request to url returns a 200" )
      assert resp.status_code == 200
      assert resp.reason == 'OK'
      try:
         print('I am in test case')
                   
      except:
         print ('exception in test case') 