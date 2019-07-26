# pytestfixture
fixture samples with test result used in teardown in pytest


With request.node.rep_call.passed/ request.node.rep_call.failed we will be able to use the result/status of the test code in the tear down.



Access test case(marks) information in Fixture:

Code in this file gives the idea to use test markers in the teardown or setup of the fixture. When we need to use the test case ID or the nubmer of steps or other static information related to any test case will be accessible.

code
fixture: 
marks = request.node.own_markers
                        mark_names = [m.args for m in marks]
                        print(marks)
                        testID = mark_names[2][0]  # 123 - it takes the test case marks as arguments in bottom to top approach
                        step = mark_names[2][1]


Access test case(result/status) infromation in Fixture:

request.node.rep_call.passed and request.node.rep_call.failed
