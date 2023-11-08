# Python Package Exercise

A little exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

# PyDate in NYC
An easy date generator that gives you activities, meals, desserts, and even pick up lines!

## Installation

## Usage
Once installed, you can call pydate from the command line with the desired function and flags  

### Activity Recommendation: ```activity(indoor, time)```
The activity function has two flags: 
1. `--indoor` specifies if the suggested activity takes place indoors `-indoor True` or outdoors`-indoor False`. 
2. `--time` specifies when the activity takes place. Options for this flag are `morning, afternoon, evening`.

For example, `python pydate_cli.py activity --indoor False --time evening` will suggest an evening outdoor activity.

### Food Recommendation
The food function has three flags:
1. `--cuisine` specifies the type of cuisine the recommended food will fall under.  Options for this flag are `French, Chinese, `.
2. `--price_range` specifies the price range of the meal. Options for this flag are `low, medium, high`.
3. `--meal` specifies the time of day the meal will be eaten. Options for this flag are `breakfast, lunch, dinner`.

### Dessert Recommendation
The dessert function has two flags:
1. `--type` specifies the type of dessert that will be suggested. Options for this flag are `bakery, candy, frozen`.
2. `--price` specifies the price range of the meal. Options for this flag are `low, medium, high`.


### Pick Up Line Recommendation



## To import project into your own code
You can  access the jokes in your own project by importing the pydate package and using the functions _activity(indoor, time)_, _food(cuisine, price_range, meal)_, _dessert(type, price)_ to get a recommendation from the chosen category. 


## Peer Contributions to PyDate
Here are the steps to contribute to this package if you'd like
1. Clone the repository to your local machine [https://github.com/software-students-fall2023/3-python-package-exercise-threepeat]
2. To set up the virtual environment and dependencies:    
  a. If pipenv is not installed, run ```pip install pipenv```           
  b. Run ```pipenv install``` to install package dependencies        
  c. Run ```pipenv shell``` to activate virtual environment
3. To run tests, run ```python3 -m pytest tests/test_file_name.py``` and replace _test_file_name.py_ with the test you want to run     
4. To build package, run ```python3 -m build```


### PyPI Link




### Contributors
Danica Jin - https://github.com/dj9771    
Emma Zheng - https://github.com/emxyz   
Gabriel Park - https://github.com/gmp9469    
Megan Chen - https://github.com/meganchen99
