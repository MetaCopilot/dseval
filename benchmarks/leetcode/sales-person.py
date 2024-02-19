'''
### Description ###

Table: `SalesPerson`

```
+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| sales_id        | int     |
| name            | varchar |
| salary          | int     |
| commission_rate | int     |
| hire_date       | date    |
+-----------------+---------+
sales_id is the primary key (column with unique values) for this table.
Each row of this table indicates the name and the ID of a salesperson alongside their salary, commission rate, and hire date.
```

Table: `Company`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| com_id      | int     |
| name        | varchar |
| city        | varchar |
+-------------+---------+
com_id is the primary key (column with unique values) for this table.
Each row of this table indicates the name and the ID of a company and the city in which the company is located.
```

Table: `Orders`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| order_date  | date |
| com_id      | int  |
| sales_id    | int  |
| amount      | int  |
+-------------+------+
order_id is the primary key (column with unique values) for this table.
com_id is a foreign key (reference column) to com_id from the Company table.
sales_id is a foreign key (reference column) to sales_id from the SalesPerson table.
Each row of this table contains information about one order. This includes the ID of the company, the ID of the salesperson, the date of the order, and the amount paid.
```

Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name **"RED"**.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

```
**Input:** 
SalesPerson table:
+----------+------+--------+-----------------+------------+
| sales_id | name | salary | commission_rate | hire_date  |
+----------+------+--------+-----------------+------------+
| 1        | John | 100000 | 6               | 4/1/2006   |
| 2        | Amy  | 12000  | 5               | 5/1/2010   |
| 3        | Mark | 65000  | 12              | 12/25/2008 |
| 4        | Pam  | 25000  | 25              | 1/1/2005   |
| 5        | Alex | 5000   | 10              | 2/3/2007   |
+----------+------+--------+-----------------+------------+
Company table:
+--------+--------+----------+
| com_id | name   | city     |
+--------+--------+----------+
| 1      | RED    | Boston   |
| 2      | ORANGE | New York |
| 3      | YELLOW | Boston   |
| 4      | GREEN  | Austin   |
+--------+--------+----------+
Orders table:
+----------+------------+--------+----------+--------+
| order_id | order_date | com_id | sales_id | amount |
+----------+------------+--------+----------+--------+
| 1        | 1/1/2014   | 3      | 4        | 10000  |
| 2        | 2/1/2014   | 4      | 5        | 5000   |
| 3        | 3/1/2014   | 1      | 1        | 50000  |
| 4        | 4/1/2014   | 1      | 4        | 25000  |
+----------+------------+--------+----------+--------+
**Output:** 
+------+
| name |
+------+
| Amy  |
| Mark |
| Alex |
+------+
**Explanation:** 
According to orders 3 and 4 in the Orders table, it is easy to tell that only salesperson John and Pam have sales to company RED, so we report all the other names in the table salesperson.
```

### Schema ###

data = [[1, 'John', 100000, 6, '4/1/2006'], [2, 'Amy', 12000, 5, '5/1/2010'], [3, 'Mark', 65000, 12, '12/25/2008'], [4, 'Pam', 25000, 25, '1/1/2005'], [5, 'Alex', 5000, 10, '2/3/2007']]
SalesPerson = pd.DataFrame(data, columns=['sales_id', 'name', 'salary', 'commission_rate', 'hire_date']).astype({'sales_id':'Int64', 'name':'object', 'salary':'Int64', 'commission_rate':'Int64', 'hire_date':'datetime64[ns]'})
data = [[1, 'RED', 'Boston'], [2, 'ORANGE', 'New York'], [3, 'YELLOW', 'Boston'], [4, 'GREEN', 'Austin']]
Company = pd.DataFrame(data, columns=['com_id', 'name', 'city']).astype({'com_id':'Int64', 'name':'object', 'city':'object'})
data = [[1, '1/1/2014', 3, 4, 10000], [2, '2/1/2014', 4, 5, 5000], [3, '3/1/2014', 1, 1, 50000], [4, '4/1/2014', 1, 4, 25000]]
Orders = pd.DataFrame(data, columns=['order_id', 'order_date', 'com_id', 'sales_id', 'amount']).astype({'order_id':'Int64', 'order_date':'datetime64[ns]', 'com_id':'Int64', 'sales_id':'Int64', 'amount':'Int64'})

### Code snippet ###

import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
'''

# %%

import pandas as pd

# %%

"""
question: |
  Write a function `def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame`.

  `sales_person` is a DataFrame with the following columns:
  - sales_id: int
  - name: str
  - salary: int
  - commission_rate: int
  - hire_date: datetime
  `sales_person` holds all salespersons. Each record has a unique `sales_id`, name, salary, commission rate, and hire date.

  `company` is a DataFrame with the following columns:
  - com_id: int
  - name: str
  - city: str
  `company` holds all companies. Each record has a unique `com_id`, name, and city.

  `orders` is a DataFrame with the following columns:
  - order_id: int
  - order_date: datetime
  - com_id: int
  - sales_id: int
  - amount: int
  `orders` holds all orders. Each record has a unique `order_id`, order date, `com_id`, `sales_id`, and amount.

  The function should find the names of all the salespersons who did not have any orders related to the company with the name **"RED"**. Return the result table in **any order**.

  The result format is in the following example.

  Example input:
  ```
  sales_person:
  +----------+------+--------+-----------------+------------+
  | sales_id | name | salary | commission_rate | hire_date  |
  +----------+------+--------+-----------------+------------+
  | 1        | John | 100000 | 6               | 4/1/2006   |
  | 2        | Amy  | 12000  | 5               | 5/1/2010   |
  | 3        | Mark | 65000  | 12              | 12/25/2008 |
  | 4        | Pam  | 25000  | 25              | 1/1/2005   |
  | 5        | Alex | 5000   | 10              | 2/3/2007   |
  +----------+------+--------+-----------------+------------+
  company:
  +--------+--------+----------+
  | com_id | name   | city     |
  +--------+--------+----------+
  | 1      | RED    | Boston   |
  | 2      | ORANGE | New York |
  | 3      | YELLOW | Boston   |
  | 4      | GREEN  | Austin   |
  +--------+--------+----------+
  orders:
  +----------+------------+--------+----------+--------+
  | order_id | order_date | com_id | sales_id | amount |
  +----------+------------+--------+----------+--------+
  | 1        | 1/1/2014   | 3      | 4        | 10000  |
  | 2        | 2/1/2014   | 4      | 5        | 5000   |
  | 3        | 3/1/2014   | 1      | 1        | 50000  |
  | 4        | 4/1/2014   | 1      | 4        | 25000  |
  +----------+------------+--------+----------+--------+
  ```

  Example output:
  ```
  +------+
  | name |
  +------+
  | Amy  |
  | Mark |
  | Alex |
  +------+
  ```

  Example explanation:
  According to orders 3 and 4 in the Orders table, it is easy to tell that only salesperson John and Pam have sales to company RED, so we report all the other names in the table salesperson.

validator:
  table_test:
    function_name: sales_person
    input_validator: |
      def _validate(sales_person, company, orders):
        assert sales_person.shape[0] > 0 and company.shape[0] > 0 and orders.shape[0] > 0
        assert sales_person.dtypes.equals(pd.Series({'sales_id': 'int64', 'name': 'object', 'salary': 'int64', 'commission_rate': 'int64', 'hire_date': 'datetime64[ns]'}))
        assert company.dtypes.equals(pd.Series({'com_id': 'int64', 'name': 'object', 'city': 'object'}))
        assert orders.dtypes.equals(pd.Series({'order_id': 'int64', 'order_date': 'datetime64[ns]', 'com_id': 'int64', 'sales_id': 'int64', 'amount': 'int64'}))
        assert sales_person.sales_id.is_unique
        assert sales_person.hire_date.between('2000-01-01', '2099-12-31').all()
        assert company.com_id.is_unique
        assert orders.order_id.is_unique
        assert orders.order_date.between('2000-01-01', '2099-12-31').all()
        assert orders.com_id.isin(company.com_id).all()
        assert orders.sales_id.isin(sales_person.sales_id).all()

    output_checker:
      ignore_order: true

    test_cases:
    - # example
      - "`pd.DataFrame({'sales_id': [1, 2, 3, 4, 5], 'name': ['John', 'Amy', 'Mark', 'Pam', 'Alex'], 'salary': [100000, 12000, 65000, 25000, 5000], 'commission_rate': [6, 5, 12, 25, 10], 'hire_date': pd.to_datetime(['4/1/2006', '5/1/2010', '12/25/2008', '1/1/2005', '2/3/2007'])})`"
      - "`pd.DataFrame({'com_id': [1, 2, 3, 4], 'name': ['RED', 'ORANGE', 'YELLOW', 'GREEN'], 'city': ['Boston', 'New York', 'Boston', 'Austin']})`"
      - "`pd.DataFrame({'order_id': [1, 2, 3, 4], 'order_date': pd.to_datetime(['1/1/2014', '2/1/2014', '3/1/2014', '4/1/2014']), 'com_id': [3, 4, 1, 1], 'sales_id': [4, 5, 1, 4], 'amount': [10000, 5000, 50000, 25000]})`"
    - # corner case: only one salesperson
      - "`pd.DataFrame({'sales_id': [1], 'name': ['John'], 'salary': [100000], 'commission_rate': [6], 'hire_date': pd.to_datetime(['4/1/2006'])})`"
      - "`pd.DataFrame({'com_id': [1], 'name': ['RED'], 'city': ['Boston']})`"
      - "`pd.DataFrame({'order_id': [1], 'order_date': pd.to_datetime(['1/1/2014']), 'com_id': [1], 'sales_id': [1], 'amount': [10000]})`"
    - # corner case: all orders are related to RED
      - "`pd.DataFrame({'sales_id': [1, 2, 3, 4, 5], 'name': ['John', 'Amy', 'Mark', 'Pam', 'Alex'], 'salary': [100000, 12000, 65000, 25000, 5000], 'commission_rate': [6, 5, 12, 25, 10], 'hire_date': pd.to_datetime(['4/1/2006', '5/1/2010', '12/25/2008', '1/1/2005', '2/3/2007'])})`"
      - "`pd.DataFrame({'com_id': [1, 2, 3, 4], 'name': ['RED', 'ORANGE', 'YELLOW', 'GREEN'], 'city': ['Boston', 'New York', 'Boston', 'Austin']})`"
      - "`pd.DataFrame({'order_id': [1, 2, 3, 4], 'order_date': pd.to_datetime(['1/1/2014', '2/1/2014', '3/1/2014', '4/1/2014']), 'com_id': [1, 1, 1, 1], 'sales_id': [1, 2, 3, 4], 'amount': [10000, 5000, 50000, 25000]})`"
    - | # generate random cases
      ```
      def _generate():
        sales_person = pd.DataFrame({'sales_id': np.arange(1, 1001), 'name': [f'name{i}' for i in range(1, 1001)], 'salary': np.random.randint(5000, 100001, 1000), 'commission_rate': np.random.randint(1, 101, 1000), 'hire_date': pd.Series(np.random.choice(pd.date_range('2000-01-01', '2020-12-31'), 1000))})
        company = pd.DataFrame({'com_id': np.arange(1, 101), 'name': [f'name{i}' for i in range(1, 101)], 'city': [f'city{i}' for i in range(1, 101)]})
        orders = pd.DataFrame({'order_id': np.arange(1, 1001), 'order_date': pd.Series(np.random.choice(pd.date_range('2013-01-01', '2013-12-31'), 1000)), 'com_id': np.random.choice(company.com_id, 1000), 'sales_id': np.random.choice(sales_person.sales_id, 1000), 'amount': np.random.randint(1000, 100001, 1000)})
        return sales_person, company, orders
      ```
    # 10 random cases
    - //
    - //
    - //
    - //
    - //
    - //
    - //
    - //
    - //
    - //
"""

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Merge the orders and company dataframes to get the company name for each order
    orders_with_company = orders.merge(company, on="com_id")

    # Filter the orders to only include those related to the company with the name "RED"
    red_orders = orders_with_company[orders_with_company["name"] == "RED"]

    # Find the salespersons who have orders related to the company with the name "RED"
    red_salespersons = set(red_orders["sales_id"])

    # Filter the sales_person dataframe to only include salespersons who did not have any orders related to the company with the name "RED"
    result = sales_person[~sales_person["sales_id"].isin(red_salespersons)]

    # Return the names of the salespersons
    return result[["name"]]
