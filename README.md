# Research-Project-Locational-Impact-on-Health-Habits-Amongst-Demographics

**Description:**

This project does a deep data analysis of how the demographics of different populations affect their health habits and obesity rates. Additionally, it assesses how regional location may play a key role in impacting the weights attributed to those factors. My goal with this project is to find ways that we can help contribute to a healthier lifestyle given the circumstances of different populations. In finding the demographics that hold stronger tendencies towards unhealthy habits, we can find ways to adjust their lifestyle to help those groups manage their risk.

***The main deliverable in this repository is:*** main_notebook.ipynb



**Research Question:**

"What demographics hold higher tendencies towards better/worse health habits thus creating patterns in obesity and overweight population? How does regional location affect those tendencies?"

***Preview Video:*** https://youtu.be/NoZ4hVgrupA?si=uI5IK21JSk21ytBm 


**Data:**

Data was sourced from the following: 

https://data.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-Behavioral/hn4x-zwk7/about_data

*Dataset included in repository*

Prior to processing, both empty and 'total' rows were removed as well as any rows where the value being reported was left unanswered. Additionally, I seperate data from 3 different main questions (health status, health activity, and diet) into 3 tables to isolate this information in analysis. This process occurs in Cell 3 (see /Code/3_Cleaning.py), but later a grand table of all information in a unified format fo each 1 demographic per row per health group is compiled in Cell 7 (see /Code/7_ProfileTable.py).

***To Reproduce:*** Please see requirements.txt in the repository

***This project was created in Google Colab. On opening the main_notebook.ipynb file (the actual research project), the entire file may be limited to github's constraints and therefore be cut off incomplete. Please see the provided google colab link at the top of the file, or located here (https://colab.research.google.com/drive/1_MvnGbE2lS_kGWlSLqMAHxMUnFBJuSQO?usp=sharing) to view the project. Additionally, I have provided the individual code cells used in the project in the "Code" folder in the repository. The py files are numbered in the order in which they should be ran. Please note, if you choose to run the code yourself, you must download and save the data and update the "raw = pd.read_csv([your_save_location])" line at the top of Cell 3.***

**Key Dependencies:**
* Python v 3.12.13
* adjustText: 1.3.0
* matplotlib: 3.10.0
* numpy: 2.0.2
* pandas: 2.2.2
* plotly: 5.24.1
* scikit-learn: 1.6.1
* seaborn: 0.13.2


**Repository Structure:**
* Code
    * [Individual Python Code blocks for notebook]
* data.csv.zip
* main_notebook.ipynb
* Project_Checkpoints
    * checkpoint_1.ipynb
    * checkpoint_2.ipynb
    * preliminary_checkpoint.ipynb
* README.md
* Requirements.txt

**Results:**

Regarding outcomes, I found that income has a very high impact on a populations tendency to partake in health activities, particularly higher income populations leading more healthy lifestyles and lower having the opposite, with middle class earners swapping roles here as potential stressers comes into consideration. This point is then driven further by looking at these habits through a scope of urbanicity, showing that lower income earners tend to have healthier habits as they move to more rural areas rather than urban.
