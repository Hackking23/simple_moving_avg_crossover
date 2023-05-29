import moving_avg_crossover as mvc
import unittest
import pandas as pd

df_t1=pd.read_json("test.json")
df_t2=pd.read_json("testd.json")
df_t3=pd.read_json("testc.json")
df_t4=pd.read_json("testh.json")
df_t5=pd.read_json("testl.json")
df_t6=pd.read_json("testo.json")
df_t7=pd.read_json("testv.json")
df_t8=pd.read_json("testi.json")
df_t9=pd.read_json("testall.json")

class TestInput(unittest.TestCase):

    def test_input(self):
        self.assertEqual(mvc.validate_input(df_t1),True)
        
        with self.assertRaisesRegex(TypeError,"following column/columns are not in specified format: datetime"):
            mvc.validate_input(df_t2)
        with self.assertRaisesRegex(TypeError,"following column/columns are not in specified format: close"):
            mvc.validate_input(df_t3)
        with self.assertRaisesRegex(TypeError,"following column/columns are not in specified format: high"):
            mvc.validate_input(df_t4)
        with self.assertRaisesRegex(TypeError,"following column/columns are not in specified format: low"):
            mvc.validate_input(df_t5)
        with self.assertRaisesRegex(TypeError,"following column/columns are not in specified format: open"):
            mvc.validate_input(df_t6)
        with self.assertRaisesRegex(TypeError,"following column/columns are not in specified format: volume"):
            mvc.validate_input(df_t7)
        with self.assertRaisesRegex(TypeError,"following column/columns are not in specified format: instrument"):
            mvc.validate_input(df_t8)
        with self.assertRaisesRegex(TypeError,"following column/columns are not in specified format: datetime,close,high,low,open,volume"):
            mvc.validate_input(df_t9)
        
if __name__=='__main__' :
    unittest.main()