import unittest
from project import velocities


class TestConversionMethods(unittest.TestCase):

   def testHagenHorizontal(self):
       #system=str(input("please choose the type of your system 1)HagenHorizontal 2)Hagenvertical 3)AnnulusVertical 4)AnnulusHorizontal :" ))
       d=[12566.263799612203, 9.999915001402478]
       dd1=velocities("HagenHorizontal")[0]
       dd2=velocities("HagenHorizontal")[1]
       self.assertEqual(dd1, d[0])
       self.assertEqual(dd2, d[1])
       
def testHagenvertical(self):
       #system=str(input("please choose the type of your system 1)HagenHorizontal 2)Hagenvertical 3)AnnulusVertical 4)AnnulusHorizontal :" ))
       d=[-61574.69261809979, -48.999583506872135]
       dd1=velocities("Hagenvertical")[0]
       dd2=velocities("Hagenvertical")[1]
       self.assertEqual(dd1, d[0])
       self.assertEqual(dd2, d[1])      
       
def AnnulusVertical(self):
       #system=str(input("please choose the type of your system 1)HagenHorizontal 2)Hagenvertical 3)AnnulusVertical 4)AnnulusHorizontal :" ))
       d=[-204746.72015616918, -217.24301733883337]
       dd1=velocities("AnnulusVertical")[0]
       dd2=velocities("AnnulusVertical")[1]
       self.assertEqual(dd1, d[0])
       self.assertEqual(dd2, d[1])         

def AnnulusHorizontal(self):
       #system=str(input("please choose the type of your system 1)HagenHorizontal 2)Hagenvertical 3)AnnulusVertical 4)AnnulusHorizontal :" ))
       d=[1583.1493009067942, 1.679773579593987]
       dd1=velocities("AnnulusHorizontal")[0]
       dd2=velocities("AnnulusHorizontal")[1]
       self.assertEqual(dd1, d[0])
       self.assertEqual(dd2, d[1])       
       
if __name__ == '__main__':
    unittest.main()