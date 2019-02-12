import allure
class Test_001:

    @allure.step(title="我是test_001_1测试步骤名称")
    def test_001_1(self):
        print("test_001_1----")
        assert True

    @allure.step(title="我是test_001_2测试步骤名称")
    def test_001_2(self):
        print("test_001_2----")
        assert False




