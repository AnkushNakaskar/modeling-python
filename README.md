# modeling-python
This project explain about Inheritance,SolidType of python.Service layer,Dao layer in project
<br />
**This project Explain  about object modeleling and inheretance in python,
Service class and DAO layer in pictures**
* Run Flight class
* Key point to remeber here in python ,It is dynamic type language.
    * So when you pass object of another class,It does not know at compile type. But in python 3.6 and above provide solution to this
    * Follow link : https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b
        * Check Flight class( has AirCraft class as input)
            ```
             def function_name(parameter1: type) -> return_type:
            ``` 

* How to run from terminal 
    * execute below cmd from terminal 
    ```python
           export PYTHONPATH=/Users/ankushnakaskar/Office/PersonalProject/PythonBooks/ObjectModelingInPython
     ```
    * Execute below cmd : 
        ```python
              python3 ./bean/fight/Flight.py
        ```
* Below statement in Flight.py 
    * ###### from .AirCraft import AirCraftClass (check this import statement also) -> this specify in same directory(..) mean above directory. 

* You can execute the code like this also in you have "__main__.py file"
    ```python3 ./```