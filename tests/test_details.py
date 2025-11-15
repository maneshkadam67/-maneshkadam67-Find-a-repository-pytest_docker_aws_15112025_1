import pytest

class TestDetails:
    a=10
    b=20
    def test_add(self):
        print(f"addition of {self.a} and {self.b} is {self.a+self.b}")

    def test_subtraction(self):
        print(f"subtraction of {self.a} and {self.b} is {self.a-self.b}")

    def test_mult(self):
        print(f"product of {self.a} and {self.b} is {self.a*self.b}")

    def test_div(self):
        print(f"div of {self.a} and {self.b} is {self.a%self.b}")

    def test_div1(self):
        print(f"div1 of {self.a} and {self.b} is {self.a/self.b}")

    def test_floor_div2(self):
        print(f"floor div2 of {self.a} and {self.b} is {self.a//self.b}")


