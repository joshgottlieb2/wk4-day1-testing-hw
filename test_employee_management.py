from employee_management import Role, Employee, Manager, Supervisor, Post
import unittest

class TestEmployee(unittest.TestCase):
    
    def test_employee_init(self):
      
        employee = Employee(first_name='Test', last_name='Testy')
        self.assertIn(employee, employee.all_)
        

    def test_create_post(self):
        emp = Employee(first_name='Sample', last_name='Samply')
        emp.create_post()
        self.assertTrue(emp.posts)

class TestManager(unittest.TestCase):

    def test_add_employee(self):
        manager1 = Manager(first_name='Buddy', last_name='Budinski')
        emp = Employee(first_name='Sample', last_name='Samply')
        manager1.add_employee(emp)
        self.assertIn(emp, manager1.employees)

    def test_remove_employee(self):
        self.assertRaises(Exception)

class TestPost(unittest.TestCase):

    def test_post_init(self):
        p = Post('hey', 'supers@codingtemple.com')
        self.assertIn(p, p.all_)


if __name__ == '__main__':
    unittest.main()