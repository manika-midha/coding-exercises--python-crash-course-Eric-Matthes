from functools import reduce

employees = [{
    'name': 'Jane',
    'salary': 90000,
    'job_title': 'developer'
}, {
    'name': 'Bill',
    'salary': 50000,
    'job_title': 'writer'
}, {
    'name': 'Kathy',
    'salary': 120000,
    'job_title': 'executive'
}, {
    'name': 'Anna',
    'salary': 100000,
    'job_title': 'developer'
}, {
    'name': 'Dennis',
    'salary': 95000,
    'job_title': 'developer'
}, {
    'name': 'Albert',
    'salary': 70000,
    'job_title': 'marketing specialist'
}]
#using map, filter and reduce
def is_developer(employee):
    """get employees who are developers """
    return employee['job_title'] == 'developer'

def is_not_developer(employee):
    """get employees who are not developers """
    return employee['job_title'] != 'developer'

developers = list(filter(is_developer,employees))
non_developers = list(filter(is_not_developer,employees))


def get_salary(employee):
    """get salary of employee """ 
    return employee['salary']

developer_salaries = list(map(get_salary,developers))
non_developer_salaries = list(map(get_salary,non_developers))


def get_sum(acc,x):
    """get sum of salaries """
    return acc+x

total_developer_salaries = reduce(get_sum,developer_salaries)
total_non_developer_salaries = reduce(get_sum,non_developer_salaries)

avg_developer_salary = total_developer_salaries/len(developer_salaries)
print(f'average dev salary : {avg_developer_salary}')
avg_non_developer_salary = total_non_developer_salaries/len(non_developer_salaries)
print(f'average non-dev salary : {avg_non_developer_salary}')

#same function as above using list comprehension instead of map and filter
developers = [employee for employee in employees if employee['job_title']=='developer']
non_developers = [employee for employee in employees if employee['job_title']!='developer']

developer_salaries = [employee['salary'] for employee in developers]
non_developer_salaries = [employee['salary'] for employee in non_developers]

def get_sum(acc,x):
    return acc+x

total_developer_salaries = reduce(get_sum,developer_salaries)
#print(total_developer_salaries)
total_non_developer_salaries = reduce(get_sum,non_developer_salaries)

avg_developer_salary = total_developer_salaries/len(developer_salaries)
print(f'average dev salary : {avg_developer_salary}')
avg_non_developer_salary = total_non_developer_salaries/len(non_developer_salaries)
print(f'average non-dev salary : {avg_non_developer_salary}')