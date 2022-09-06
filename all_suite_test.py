import unittest

from unittest.loader import makeSuite

from test_cases.adding_a_player import TestDashboardPageAddingPlayer
from test_cases.changing_language import TestDashboardPage
from test_cases.sign_out import TestDashboardPagesignout
from test_cases.framework import Test
from test_cases.login_in_the_system import TestLoginPage



def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(Test))
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestDashboardPagesignout))
   test_suite.addTest(makeSuite(TestDashboardPage))
   test_suite.addTest(makeSuite(TestDashboardPageAddingPlayer))
   return test_suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())