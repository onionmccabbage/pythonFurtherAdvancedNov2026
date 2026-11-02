## Python Further Advanced

November 2-6 2026

Toby Dussek

* 9:30  start
* 11:00 coffee break until 11:15
* 12:00 lunch until 1:00
* 3:00  tea break break until 3:15
* 4:30  end

All my code will be in this repository
* https://github.com/onionmccabbage/pythonFurtherAdvancedNov2026

### Monday
> welcome
  - introduce yourself
  - existing Python experience
  - application of Python from previous lcourses
  - other related technologies
  - anything particular you want from this course
* we will be installing additional packages as needed
* conventions
  - as will all languages, identifiers can use letters, numbers and underscore (don't start with a number)
  - some conventions: ClassesUsePascalCase, methodsUseCamelCase identifiers_use_snake_case
* design patterns - following proven good practices
  https://refactoring.guru/design-patterns/python
  https://www.geeksforgeeks.org/python/python-design-patterns/
  https://blog.ahmadwkhan.com/design-patterns-in-python-the-complete-reference
  https://python-patterns.guide/
  
> Constructor, Decorator and Factory pattern
> Abstract base class, class encapsulation, inheritance, private and protected members
* Facade, Command and Proxy pattern
* anti-patterns: when things go wrong and you do it again!
* Polymorphism and monkey-patching
* after lunch review exercise (show what you built)
* immediate Python
* redirection and context
* we will need Jupyter Notebooks later in the week

### Tuesday
* how to access the course recordings
* reminder: `__str__`, `__repr__` and `__slots__`
* architectural patterns: inheritance, composition...
* stateful pattern
* functional design
* concurrency and parallel code
* the GIL
  see https://realpython.com/python-gil/
  from 3.14 (Oct 7 2025) we can avoid the GIL
  see https://www.pythoncheatsheet.org/blog/python-3-14-breaking-free-from-gil
* thread functions and thread classes
* after lunch review exercise
* can we kill threads which have hung or other problems....
  we never kill thrreads (there is no mechanism in Python)
  we manage threads e.g. https://www.geeksforgeeks.org/python/python-different-ways-to-kill-a-thread/
* thread locks/rlocks/semaphores
* semaphore quantity depends on the capabilities of the asset being accessed

### Wednesday
* generators and comprehension
* a word about venv see https://python.land/virtual-environments/virtualenv
* daemon threads, thread events
* custom thread decorator to make classes and methods thread safe
* solve the double-locking problem (both decorators)
* the 'with' operator
* asyncio (Python 3.7 or better)
  see https://docs.python.org/3/library/asyncio-task.html#coroutines
* multiprocessing
* why use asyncio, threads or a processes
  see https://medium.com/@Gayathri_krish/threading-vs-multiprocessing-vs-asyncio-in-python-which-one-should-you-use-7a3b7649d004
  and https://www.krython.com/tutorial/python/threading-vs-multiprocessing-vs-asyncio
* Memory, performance and timing
* New profiling features in 3.15 (and retirement of old profile tools)
* profiling with @profile, cProfile and the new profiling tools in 3.15
* after lunch review exercise
* prepare for Thursday  
* observables and subscribers
* RxPY https://rxpy.readthedocs.io/en/latest/index.html
       https://rxmarbles.com/

### Thursday
* options for Jupyter Notebooks:
  - use Anaconda (NB it is likely you cannot use the free Anaconda within Ericsson)
  - pip install notebook (see https://jupyter.org/install)
  - pip install jupyter (or pip3 install...) (or python -m pip3 install ...)
  - just use existing VSCode (or similar)
  - use cloud (e.g. colab https://colab.research.google.com/ or https://jupyter.org/try)
  - or just write NORMAL python modules
* Python for Data Analysis
  see
  https://realpython.com/tutorials/data-science/
  https://www.kaggle.com/learn
  https://pll.harvard.edu/course/introduction-data-science-python
 
  we will need:
  - Jupyter notebooks
  - numpy
  - pandas
  - matplotlib
* using Jupyter notebooks
   Data sources (csv, xlsx, text, db, url...)
   you can 'pip install jupyter' then start it with 'python -m notebook'
   then you will also need to pip install numpy, pandas etc.
* numpy and data structures: the arange and array 
* pandas: Series and DataFrame
* NaN, creating stuctures, analysis (stats)
* data cleansing and preparation
* descriptive actionable  statistics
* handling files and remote data
* data vizualisation with matplotlib
* after lunch review exercise

### Friday
* statistical analysis and correlation
  REMEMBER: correlation does NOT prove CAUSATION
  https://www.tylervigen.com/spurious-correlations
* review of microservices
* multi threading
* asyncio microservices
* we can control the number of concurrent accesses to our microservice....
* resources for numpy, pandas, matplotlib, flask, django
* Flask:
  to run as a debug server: flask --app my_flask.py --debug run
  or else debug=True in the app run declaration
  see https://flask.palletsprojects.com/en/2.3.x/
* after lunch review exercise


- end of course feedback
  - https://easyretro.io/publicboard/NTDqkkm6utgJFD9cdBrdb4sI6n72/57b081b3-524e-4ada-80d2-0d94500bc310
