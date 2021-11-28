# Fitness_Calculator

Fitness_calculator is a python command line application ran in the Code Institute mock terminal on Heroku.

Users can decide if they would like to calculate there BMI, Recommended Daily Calorie Intake and the Breakdown of their recommended Macros amounts. 

## Here is a link to the deployed site:

[Python Terminal by Code Institute](https://fitness-calculator-tool.herokuapp.com/)

---

![heroku-photo.png](Fitness_Calculator%207d866edd07094055929928c20fb2837b/heroku-photo.png)

---

## How to Navigate

---

![Untitled Diagram.jpg](Fitness_Calculator%207d866edd07094055929928c20fb2837b/Untitled_Diagram.jpg)

---

- This a flow chart I made before coding the project to visualise the paths possible through the program.
- There is 3 main paths: BMI, Calories and Macros. It is possible to do any combination of them. If a question has already been asked in a previous section the value will be reused to not delay the user.
- the UI features y/n questions, simple questions to get number values and weight/height etc.
- There is multiple Tables printed to give example answers for those who may be unsure.
    
    ---
    
    ## Example Questions & Responses
    
    ---
    
    ![opening.png](Fitness_Calculator%207d866edd07094055929928c20fb2837b/opening.png)
    
    ---
    
    ![table.png](Fitness_Calculator%207d866edd07094055929928c20fb2837b/table.png)
    

---

![tables2.png](Fitness_Calculator%207d866edd07094055929928c20fb2837b/tables2.png)

---

![question.png](Fitness_Calculator%207d866edd07094055929928c20fb2837b/question.png)

---

![endresult.png](Fitness_Calculator%207d866edd07094055929928c20fb2837b/endresult.png)

---

this is not all the questions and results but it is an example of the method for inputting and receiveing values.

## Testing

---

The project has been manually tested using the following methods. 

- Validated the code with pep8online which didn't return any errors apart from line width being >79 which I have chose to ignore from the beginning.
- Tried multiple types of Inputs to try get an error from the wrong type of input.
- tested for any unexpected errors in local dev environment and heroku deployment.

---

## Bugs

- I Encountered countless bugs specifically with the inputs for questions and the calculations to get the different return values as there is many variables that have to be modified and operated on. Thankfully they have all  been sorted now.
- I had to state some variables as explicit floats as they  were origanially integers and were causing issues in the calculations.

---

## Deployment

This project was deployed using Code Institutes mock terminal for Heroku.

### Steps for deployment:

1. Fork or clone the CI Python Template Repo on GitHub
2. Create a new Heroku app
3. Set the buildpacks to Python And NodeJs in that specific order
4. Link the github repo to the Heroku app
5. ensure your requirments.txt is up to date in the repo.
6. Insert any required config vars in the settings page of the heroku app.
7. click on **Deploy**

---

## Credits

[The Ultimate Guide to Body Recomposition - Jeff Nippard Programs](https://shop.jeffnippard.com/product/the-ultimate-guide-to-body-recomposition/)

Jeff Nippard a Sports Coach who wrote the book The Ultimate Guide to Body Recompostion which inspired a lot of the industry standard formulas for calculating the values in my app.

My mentor for the support throughout my project.
