
from gggg import *

a = Assignment(21, 10)
s = State(a)

horizontal_rule()

s.reject_if_missing_contributors()
s.reject_if_starter_contributors()

s.reject_unless_files_exist(['Book.hpp',
                             'Book.cpp',
                             'BookDatabase.hpp',
                             'BookDatabase.cpp',
                             'Checkout.hpp',
                             'Checkout.cpp'])

s.reject_if_file_unchanged('Book.cpp',
                           '953ed73434f4cae54b9161b48da2f25a2622522198a655c00de571bb596b16df')

s.reject_unless_command_succeeds(['make', 'clean', 'test'])

s.string_removed_test('TO-DO comments removed', 3, 'TO-DO', ['Book.cpp', 'BookDatabase.hpp', 'BookDatabase.cpp', 'Checkout.cpp'])

s.gtest_run('BookDatabase_test')
s.gtest_suite_test('BookDatabaseSize', 2)
s.gtest_suite_test('BookDatabaseFind', 4)
s.gtest_run('Checkout_test')
s.gtest_suite_test('CheckoutTestShopForBooks', 3)
s.gtest_suite_test('CheckoutTestSwitchCarts', 3)
s.gtest_suite_test('CheckoutTestMoveBooksToCheckout', 3)
s.gtest_suite_test('CheckoutTestDoCheckout', 3)

s.summarize()
