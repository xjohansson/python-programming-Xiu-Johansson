from vector import Vector
import unittest

#v1=Vector(1,1)
# print(v1)


class TestVector(unittest.TestCase):
    def setUp(self)-> None:  # 在每个测试方法执行前被调用
         self.x,self.y=1,2

    def create_2D_vector(self) -> "Vector":   
         return Vector( self.x,self.y)

     # testing starts here -all tests must start with the word test.    
     
     #test creating vectors 测试创建矩阵向量
    def test_create_2D_vector(self) -> None:
          v=self.create_2D_vector()
          self.assertEqual(v.numbers,(self.x,self.y))

    def test_create_5D_vector(self):
          v=Vector(1,2,3,4,5)
          self.assertEqual(v.numbers,(1,2,3,4,5)) # 判断两个值是否相等

    def test_empty_vector(self):
         with self.assertRAISERS(ValueError): # 检测异常
             v=Vector()

    def test_create_invalid_vector(self):
        with self.assertRAISES(TypeError):
            v=Vector("1","Two")         


  #test_eq_ ==
    def test_2_vector_equal(self):
         v1=self.create_2D_vector()
         v2=Vector(1,2)
         self.assertEqual(v1,v2) ## 判断两个值v1 and v2是否相等

    def test_2_vector_not_equal(self):
         v1=self.create_2D_vector()
         v2=Vector(-1,2)
         self.assertEqual(v1,v2)



     

if_name_=="_main_":
     unittest.main()         

