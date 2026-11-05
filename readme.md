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
* NB this will only exist for a while after end of course

Recordings available here
* https://learn.neueda.com/course/482357
* Sign up with any email/password
* Course Reg Code: HGUWTO
* These will only be available for a few days after the end of course

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
> design patterns - following proven good practices
  https://refactoring.guru/design-patterns/python
  https://www.geeksforgeeks.org/python/python-design-patterns/
  https://blog.ahmadwkhan.com/design-patterns-in-python-the-complete-reference
  https://python-patterns.guide/
  
> Constructor, Decorator and Factory pattern
> Abstract base class, class encapsulation, inheritance, private and protected members
> Facade, Command
> Proxy pattern: many ways to implement
> Facade and Command are similar: command lets us manage a queue of commands
> All patterns are just repeating what worked
> anti-patterns: when things go wrong and you do it again!
> Polymorphism and monkey-patching
> after lunch review exercise (show what you built)
> immediate Python
> redirection and context
* we will need Jupyter Notebooks later in the week

### Tuesday
* how to access the course recordings
>tectural patterns: inheritance, composition...
> stat reminder: `__str__`, `__repr__` and `__slots__`
> archieful pattern
> timing (as a performance metric)
> functional design: use map, filter, reduce as performant functional operations
> concurrency and parallel code
> the GIL
  see https://realpython.com/python-gil/
  from 3.14 (Oct 7 2025) we can avoid the GIL
  see https://www.pythoncheatsheet.org/blog/python-3-14-breaking-free-from-gil
> thread functions and thread classes
> after lunch review exercise
> can we kill threads which have hung or other problems....
  we never kill threads (there is no mechanism in Python)
  we manage threads e.g. https://www.geeksforgeeks.org/python/python-different-ways-to-kill-a-thread/
> thread locks/rlocks/semaphores
> semaphore concurrent depends on the capabilities of the asset being accessed

### Wednesday
> create a thread-divvy version for Weds
> custom thread decorator to make methods thread safe
> range generators and comprehension: really good for performance
> a word about venv see https://python.land/virtual-environments/virtualenv
> daemon threads, thread events
> the 'with' operator
* asyncio (Python 3.7 or better)
  see https://docs.python.org/3/library/asyncio-task.html#coroutines
* multiprocessing
* why use asyncio, threads or a processes
  see https://medium.com/@Gayathri_krish/threading-vs-multiprocessing-vs-asyncio-in-python-which-one-should-you-use-7a3b7649d004
  and https://www.krython.com/tutorial/python/threading-vs-multiprocessing-vs-asyncio
* Memory, performance and timing
* New profiling features in 3.15 (and retirement of old profile tools)
* profiling with @profile, cProfile and the new profiling tools in 3.15
  * python -m cProfile -o prof_out <filename>
  * then examine hte prof_out results
* after lunch review exercise
* prepare for Thursday  
* observables and subscribers
* RxPY https://rxpy.readthedocs.io/en/latest/index.html
       https://rxmarbles.com/

### Thursday
> options for Jupyter Notebooks:
  - use Anaconda (NB it is likely you cannot use the free Anaconda within Ericsson)
  - pip install notebook (see https://jupyter.org/install)
  - pip install jupyter (or pip3 install...) (or python -m pip3 install ...)
  - just use existing VSCode (or similar)
  - use cloud (e.g. colab https://colab.research.google.com/ or https://jupyter.org/try)
  - or just write normal python modules
  - to invoke Jupyter:
    - jupyter notebook
    - python -m jupyter notebook
* Python for Data Analysis
  see
  https://realpython.com/tutorials/data-science/
  https://www.kaggle.com/learn
  https://pll.harvard.edu/course/introduction-data-science-python
 
  we will need:
  - Jupyter notebooks
  - numpy
  - pandas
> using Jupyter notebooks
   Data sources (csv, xlsx, text, db, url...)
   you can 'pip install jupyter' then start it with 'python -m notebook'
   then you will also need to pip install numpy and pandas
> numpy and data structures: the arange and array 
> pandas: Series and DataFrame
* NaN, creating stuctures, analysis (stats)
* data cleansing and preparation
* descriptive actionable  statistics
* handling files and remote data
* data vizualisation with matplotlib
* after lunch review exercise
* resolve date issue
* cleaning data: NaN
* merge data from several sources
* security
* statistical analysis and correlation
  REMEMBER: correlation does NOT prove CAUSATION
  https://www.tylervigen.com/spurious-correlations

### Friday
* review of microservices and concurrency (this impacts on thread semaphores)
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
