CS 488/588 – Applied Data Science with Python
==================================================================

| `University of Idaho <https://www.uidaho.edu>`_ - `Department of Computer Science <https://www.uidaho.edu/engr/departments/cs>`_
| Instructor: `Alex Vakanski <https://www.webpages.uidaho.edu/vakanski/index.html>`_ (vakanski@uidaho.edu)
| Teaching Assistant: Longze Li (li8975@vandals.uidaho.edu)
| Semester: Fall 2024 (August 19 – December 13)
| *Course website*: https://fall-2024-applied-data-science-with-python.readthedocs.io/en/latest/
| *GitHub repository*: https://www.github.com/avakanski/Fall-2024-Applied-Data-Science-with-Python/blob/main/README.md

Course Syllabus
~~~~~~~~~~~~~~~~~~~~~
`View Syllabus <_static/CS_488_588-Applied_Data_Science_with_Python-Syllabus.pdf>`_

Course Description
~~~~~~~~~~~~~~~~~~~~~
| The course introduces students to Python tools and libraries that are commonly used by organizations for managing the various phases in the life cycle of data science projects. The content is divided into four main themes. The first theme reviews the fundamentals of Python programming. The second theme focuses on data engineering and explores Python tools for data collection, exploration, and visualization. The next theme covers model engineering and includes topics related to model design, selection, and evaluation for image processing, natural language processing, and time series analysis. The last theme introduces Data Science Operations (DSOps) and encompasses techniques for model serving, performance monitoring, diagnosis, and reproducibility of data science projects deployed in production. Throughout the course, students will gain hands-on experience with various Python libraries for data science workflow management. Additional work is required for graduate credit.


Textbooks
~~~~~~~~~~~~
There are no required textbooks for this course.

Learning Outcomes
~~~~~~~~~~~~~~~~~~~

Upon the completion of the course, the students should demonstrate the ability to:

1.	Attain proficiency with commonly used Python frameworks for managing the life cycle of data science projects.
2.	Develop pipelines for integrating data from multiple sources, designing predictive models, and deploying the models.
3.	Apply Python tools for data collection, analysis, and visualization, such as NumPy, Pandas, Matplotlib, and Seaborn, to real-world datasets.
4.	Implement machine learning algorithms for image processing, natural language processing, and time series analysis using Python-based frameworks, such as Scikit-Learn, Keras, TensorFlow, and PyTorch.
5.	Understand the principles of model selection and evaluation, including hyperparameter tuning, cross-validation, and regularization.  
6.	Understand the primary characteristics of current Python libraries for deployment, continuous integration, and monitoring of data science projects.
7.	Deploy data science projects as web applications using Flask, FastAPI, and Django, and to cloud servers using Microsoft’s Azure platform.

Prerequisites
~~~~~~~~~~~~~~~
The course requires to have basic programming skills in Python. While having knowledge of data science methods would be advantageous, it is not mandatory.

Grading
~~~~~~~~~~~~
Student assessment will be based on 6 homework assignments (worth 60 pts), 3 quizzes (worth 30 marks), and class participation and engagement (worth 10 marks).


Lectures
============

.. toctree::
   :caption: Lecture 1 - Short History of AI

   pdf_link_lecture1

.. toctree::
   :caption: Theme 1 - Python Programming
   :maxdepth: 2

   Lectures/Theme_1-Python_Programming/Lecture_2-Data_Types_in_Python/Lecture_2-Data_Types.ipynb
   Lectures/Theme_1-Python_Programming/Lecture_3-Statements,_Files/Lecture_3-Statements,_Files.ipynb
   Lectures/Theme_1-Python_Programming/Lecture_4-Functions,_Iterators/Lecture_4-Functions,_Iterators.ipynb
   Lectures/Theme_1-Python_Programming/Lecture_5-OOP,_Modules,_Packages/Lecture_5-OOP,_Modules,_Packages.ipynb

.. toctree::
   :caption: Theme 2 - Data Engineering Pipelines
   :maxdepth: 2

   Lectures/Theme_2-Data_Engineering/Lecture_6-NumPy/Lecture_6-NumPy.ipynb
   Lectures/Theme_2-Data_Engineering/Lecture_7-Pandas/Lecture_7-Pandas.ipynb
   Lectures/Theme_2-Data_Engineering/Lecture_8-Matplotlib/Lecture_8-Matplotlib.ipynb
   Lectures/Theme_2-Data_Engineering/Lecture_9-Seaborn/Lecture_9-Seaborn.ipynb
   Lectures/Theme_2-Data_Engineering/Lecture_10-Statistical_Data_Analysis/Lecture_10-Statistical_Data_Analysis.ipynb
   Lectures/Theme_2-Data_Engineering/Lecture_11-SQL/Lecture_11-SQL.ipynb
   Lectures/Theme_2-Data_Engineering/Lecture_12-Data_Exploration/Lecture_12-Data_Exploration_and_Preprocessing.ipynb

.. toctree::
   :caption: Theme 3 - Model Engineering Pipelines
   :maxdepth: 2

   Lectures/Theme_3-Model_Engineering/Lecture_13-Scikit-Learn/Lecture_13-Scikit-Learn.ipynb
   Lectures/Theme_3-Model_Engineering/Lecture_14-Ensemble_Methods/Lecture_14-Ensemble_Methods.ipynb
   Lectures/Theme_3-Model_Engineering/Lecture_15-ANNs/Lecture_15-ANNs.ipynb
   Lectures/Theme_3-Model_Engineering/Lecture_16-ConvNets/Lecture_16-ConvNets.ipynb
   Lectures/Theme_3-Model_Engineering/Lecture_17-Model_Selection/Lecture_17-Model_Selection.ipynb
   Lectures/Theme_3-Model_Engineering/Lecture_18-NNs_with_PyTorch/Lecture_18-NNs_with_PyTorch.ipynb
   Lectures/Theme_3-Model_Engineering/Lecture_19-Natural_Language_Processing/Lecture_19-NLP.ipynb
   Lectures/Theme_3-Model_Engineering/Lecture_20-Transformer_Networks/Lecture_20-Transformer_Networks.ipynb
   Lectures/Theme_3-Model_Engineering/Lecture_21-NLP_with_Hugging_Face/Lecture_21-NLP_with_Hugging_Face.ipynb
   Lectures/Theme_3-Model_Engineering/Lecture_22-LLMs/Lecture_22-LLMs.ipynb

.. toctree::
   :caption: Theme 4 - Model Deployment Pipelines
   :maxdepth: 2

   Lectures/Theme_4-Model_Deployment/Lecture_23-DSOps/Lecture_23-DSOps.pdf
   Lectures/Theme_4-Model_Deployment/Lecture_24-Deploying_to_Web/Lecture_24-Deploying_to_Web.ipynb

.. toctree::
   :caption: Tutorials
   :maxdepth: 2

   Lectures/Tutorials/Tutorial_1-Jupyter_Notebooks/Tutorial_1-Jupyter_Notebooks.ipynb
   Lectures/Tutorials/Tutorial_2-Terminal_and_Command_Line/Tutorial_2-Terminal_and_Command_Line.ipynb
   Lectures/Tutorials/Tutorial_3-VS_Code/Tutorial_3-VS_Code.ipynb
   Lectures/Tutorials/Tutorial_4-Virtual_Environments/Tutorial_4-Virtual_Environments.ipynb
   Lectures/Tutorials/Tutorial_5-Web_Scraping/Tutorial_5-Web_Scraping.ipynb
   Lectures/Tutorials/Tutorial_6-Google_Colab/Tutorial_6-Google_Colab.ipynb
   Lectures/Tutorials/Tutorial_7-Image_Processing/Tutorial_7-Image_Processing.ipynb
   Lectures/Tutorials/Tutorial_8-TensorFlow/Tutorial_8-TensorFlow.ipynb
   Lectures/Tutorials/Tutorial_9-PyTorch/Tutorial_9-PyTorch.ipynb
   Lectures/Tutorials/Tutorial_10-Bash/Tutorial_10-Bash.ipynb
   Lectures/Tutorials/Tutorial_11-GitHub/Tutorial_11-GitHub.ipynb
