#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest


# In[2]:


def is_odd(n):
    pass


# In[3]:


class TestIsOdd(unittest.TestCase):

    def test_01(self):
        self.assertEqual(is_odd(3), True)

    def test_02(self):
        self.assertEqual(is_odd(12), False)

    def test_03(self):
        self.assertEqual(is_odd(33), True)


# In[4]:


if __name__ == '__main__':
    unittest.main(verbosity=2)


# In[ ]:




