import pytest


@pytest.mark.smoke
def test_exam1():
    print("This is Exam1")


@pytest.mark.smoke
def test_exam2():
    print("This is Exam2")


@pytest.mark.regression
def test_exam3():
    print("This is Exam3")


@pytest.mark.regression
def test_exam4():
    print("This is Exam4")

@pytest.mark.smoke
@pytest.mark.regression
def test_exam5():
    print("This is Exam5")


@pytest.mark.smoke
@pytest.mark.regression
def test_exam6():
    print("This is Exam6")