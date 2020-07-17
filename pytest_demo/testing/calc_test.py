import pytest,sys,allure
sys.path.append("..")

from pycode.calc import Calculator


class TestCalc:

    # setup_class、teardown 是类级别的
    def setup_class(self):
        print("在整个类前执行setup_class")
        self.calc = Calculator()

    def teardown_class(self):
        print("在整个类后执行teardown_class")

    # setup、teardown是方法级别的
    def setup(self):
        print("测试用例执行前执行setup")
        self.calc = Calculator()

    def teardown(self):
        print("测试用例执行后执行teardown")

    @pytest.mark.parametrize("a,b,c",[
        (1,1,2),
        (0.1,0.1,0.2),
        (-1,-1,-2),
        (100,100,200)
    ])
    def test_add(self,a,b,c):
        allure.attach("这是一个加法测试用例", name="文本类型",attachment_type=allure.attachment_type.TEXT)
        allure.attach("<body>HTML</body>", name="HTML类型", attachment_type = allure.attachment_type.HTML)
        assert c == self.calc.add(a,b)

    def test_div(self):
        allure.attach("/Users/xyq/Documents/Study/pytest_demo/testing/Python_notes.png", name='截图',attachment_type=allure.attachment_type.PNG)
        allure.attach("/Users/xyq/Documents/Study/pytest_demo/testing/video.mp4", name='视频',attachment_type=allure.attachment_type.MP4)
        assert 2 == self.calc.div(4,2)