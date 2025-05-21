import sys, os, json
if os.path.isdir("./.venv/lib/"):
    sys.path.append('null/site-packages')
def pytest_addoption(parser):
    parser.addoption("--stdin", action="append", default=[],
        help="json with the stdin to pass to test functions")
def pytest_generate_tests(metafunc):
    if 'stdin' in metafunc.fixturenames:
      if hasattr(metafunc,"config"):
          metafunc.parametrize("stdin",metafunc.config.getoption('stdin'))
      elif hasattr(metafunc,"configuration"):
          metafunc.parametrize("stdin",metafunc.configuration.getoption('stdin'))
      else:
          raise Exception("Imposible to retrieve text configuration object")
    if 'app' in metafunc.fixturenames:
        try:
          sys.path.append('.learn/dist')
          import cached_app
          metafunc.parametrize("app",[cached_app.execute_app])
        except SyntaxError:
          metafunc.parametrize("app",[lambda : None])
        except ImportError:
          metafunc.parametrize("app",[cached_app])
        except AttributeError:
          metafunc.parametrize("app",[cached_app])
    if 'configuration' in metafunc.fixturenames:
        metafunc.parametrize("configuration", [json.loads('{"port":3000,"os":"linux","editor":{"mode":"extension","agent":"vscode","version":"5.0"},"dirPath":"./.learn","configPath":"learn.json","outputPath":".learn/dist","publicPath":"/preview","publicUrl":"https://studious-space-acorn-7v54pr9jgrwxcrpgg-3000.app.github.dev","contact":"https://github.com/learnpack/learnpack/issues/new","language":"auto","autoPlay":true,"projectType":"tutorial","grading":"isolated","exercisesPath":"./exercises","webpackTemplate":null,"disableGrading":false,"disabledActions":[],"actions":[],"entries":{"html":"index.html","vanillajs":"index.js","react":"app.jsx","node":"app.js","python3":"app.py","java":"app.java"},"suggestions":{"agent":"vscode"},"warnings":{"agent":null},"slug":"python-beginner-programming-exercises","title":{"us":"Learn Python Interactively (beginner)","es":"Aprende Python Interactivamente (Principiante)"},"intro":"https://www.youtube.com/watch?v=amyDNhZwGJQ","repository":"https://github.com/4GeeksAcademy/python-beginner-programming-exercises","preview":"https://github.com/4GeeksAcademy/python-beginner-programming-exercises/blob/master/.learn/assets/preview.png?raw=true","description":{"us":"Python exercises for beginners, starting from the basics like `Hello World` to more advanced concepts like variables, loops, functions, and data structures. These hands-on challenges guide you step by step through Python programming, offering interactive and auto-graded lessons to build a solid foundation.","es":"Ejercicios de Python para principiantes, comenzando desde lo básico como `Hola Mundo` hasta conceptos más avanzados como variables, bucles, funciones y estructuras de datos. Estos desafíos prácticos te guían paso a paso en la programación con Python, ofreciendo lecciones interactivas y autoevaluadas para construir una base sólida."},"duration":10,"difficulty":"easy","videoSolutions":true,"bugsLink":"https://github.com/learnpack/learnpack/issues/new","graded":true,"technologies":["strings","python-functions","conditionals","variables","condicionales","funciones-de-python"],"telemetry":{"batch":"https://breathecode.herokuapp.com/v1/assignment/me/telemetry?asset_id=145"},"video":{"intro":{"es":"https://www.youtube.com/watch?v=IXNSwnN-YqM","en":"https://www.youtube.com/watch?v=amyDNhZwGJQ"}},"translations":[]}')])
