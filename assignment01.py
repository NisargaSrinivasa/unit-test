#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Input
n = 2


# In[2]:


import unittest


# In[3]:


def is_prime(n):
    pass


# DO NOT TOUCH THE BELOW CODE


# In[4]:


class TestIsPrime(unittest.TestCase):

    def test_01(self):
        self.assertEqual(is_prime(3), True)

    def test_02(self):
        self.assertEqual(is_prime(12), False)

    def test_03(self):
        self.assertEqual(is_prime(33), False)




# In[5]:


if __name__ == '__main__':
    unittest.main(verbosity=2)


# In[ ]:




