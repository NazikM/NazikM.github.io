import unittest


class Worker:
    def __init__(self, name, salary=0.0):
        if salary < 0:
            raise ValueError
        self.name = name
        self.salary = salary

    def get_tax_value(self):
        temp_salary = self.salary
        if self.salary <= 1000:
            return 0.0
        tax = 0
        if temp_salary <= 3000:
            tax += 0.1 * (self.salary - 1000)
            return tax
        else:
            tax += 200
            temp_salary -= 3000
        if temp_salary

        elif 1001 <= self.salary <= 3000:
            return 0.1*(self.salary-1000)
        elif 3001 <= self.salary <= 5000:
            return 0.15*(self.salary-3000)
        elif 5001 <= self.salary <= 10000:
            return 0.21*(self.salary-5000)
        elif 10001 <= self.salary <= 20000:
            return 0.30*(self.salary-10000)
        elif 20001 <= self.salary <= 50000:
            return 0.40*(self.salary-20000)
        else:
            return 0.47*(self.salary-50000)


class WorkerTest(unittest.TestCase):
    pass