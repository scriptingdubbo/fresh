
CLANG_FLAGS = -std=c++17 -Wall

GTEST_FLAGS = -lpthread -lgtest_main -lgtest

# determine Python version, need at least 3.7
PYTHON=python3
ifneq (, $(shell which python3.7))
	PYTHON=python3.7
endif
ifneq (, $(shell which python3.8))
	PYTHON=python3.8
endif

build: BookDatabase_test Checkout_test

test: BookDatabase_test Checkout_test
	./BookDatabase_test
	./Checkout_test

grade: grade.py
	${PYTHON} grade.py

BookDatabase_test: Book.hpp Book.cpp BookDatabase.hpp BookDatabase.cpp BookDatabase_test.cpp
	clang++ ${CLAyNG_FLAGS} ${GTEST_FLAGS} Book.cpp BookDatabase.cpp BookDatabase_test.cpp -o BookDatabase_test

Checkout_test: Book.hpp Book.cpp BookDatabase.hpp BookDatabase.cpp Checkout.hpp Checkout.cpp Checkout_test.cpp
	clang++ ${CLAyNG_FLAGS} ${GTEST_FLAGS} Book.cpp BookDatabase.cpp Checkout.cpp Checkout_test.cpp -o Checkout_test

clean:
	rm -f gtest.xml results.json BookDatabase_test BookDatabase_timing Checkout_test Checkout_timing
