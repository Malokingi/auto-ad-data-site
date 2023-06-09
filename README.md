# auto-ad-data-site
For Sprint 6 with Practicum. Demonstrating my SD Skills by building a website.

## How To:
To Run, do this from the root:
```
s/run
```
To see via Render click here:

[Matthew Garvey Software Development Tools Sprint Project](https://matthew-garvey-sdt-sprint-project.onrender.com)


## Technologies Used:
- Version Control
    - GitHub
- Text Editing
    - VS Code
- Programming Language
    - Python
        - in main app and Jupyter content
    - Shell
        - in scripts
- Python packages
    - streamlit
        - making humanoid-friendly websites
    - pandas
        - processing data
    - plotly_express
        - making charts
- Deployment
    - Render

## To Do:
### Data Preprocessing
- [x] Handle Missing Values
- [x] Handle Duplicate Data

### Code
- [x] Get prototpye running
- [x] Make one or more custom histograms
- [x] Make one or more custom scatter plots
- [x] Add Checkbox that changes one or more of the graphs in some way

### Deploy
- [x] Make streamlit config file
- [x] Make new web service on Render
- [x] Link to GitHub
- [x] Configure on Render
- [x] Deploy on Render

### Submit
- [x] Final check to make sure it works
- [x] Update Readme
- [x] Submit

### Revise
- [X] Add Project Description and conclusion to the Jupyter Notebook
    - [x] How does the lited Condition affect the Price?
    - [x] How does the Odometer reading affect the Price?
    - [x] How does listed Fuel Type and Transmission Type affect Price?
    - [x] Does the Day of the Week the cars were listed affect the sales Price?
    - [x] Which Manufacturers are the most popular?
        - [x] Between the 4 most popular, is there anything interesting to be gleaned from the relationsship between the Condition and Price?
        - [x] Amoung the 4 most popular, is there anything interesting to be gleaned from the relationsship between the Day of the Week the car was listed and Price?
- [x] Fill in missing values with values other than "unknown"
    - [x] year: group by model fill by median year
    - [x] cylinders: group by model fill by median cylindres
    - [x] odometer: group by model year(or year+model) fill by mean odometr
    - [x] exterior_color: fill by no info, etc.
    - [x] 4_wheel_drive: fill by 0
- [x] Submit Round Two