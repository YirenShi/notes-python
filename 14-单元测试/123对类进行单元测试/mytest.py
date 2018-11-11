import  unittest
from person import  Person

class Test(unittest.TestCase):
    def test_init(self):
        p = Person("hanmeimei",20)
        self.assertEqual(p.name,"hanmeimei","属性赋值有误")
    def test_getAge(self):
        p = Person("hanmeimei", 22)
        self.assertEqual(p.getAge(),p.age,"getAge函数有误")
if __name__ =="__main__":
    unittest.main()