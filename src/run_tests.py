import unittest
from testDir import *

if __name__ == '__main__':
    testsuite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(testsuite) 



    
