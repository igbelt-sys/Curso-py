import pyautogui as py

py.press("win")
py.write("chrome")
py.press("enter")
# entrando no chrome
py.sleep(1)
py.write("SENAI americana")
py.press("enter")
py.sleep(1)
# pesquisando SENAI americana
# print(py.position())
py.click(x=326, y=514)
py.sleep(1)
# clicando no site
# print(py.position())
py.click(x=1476, y=856)
py.sleep(2)
# clicando na aba de cursos
# print(py.position())
py.click(x=213, y=551)
py.write("python")
py.press("enter")
py.sleep(3)
# clicando na aba de ppesquisa e escrevendo o nome do curso
# print(py.position())
py.click(x=702, y=1004)
py.sleep(2)
py.scroll(-600)
py.sleep(1)
# clicando no curso e scrolando para baixo
# print(py.position())
py.click(x=1400, y=924)
py.sleep(1)
# clicando em fechar a as informacoes do curso
# print(py.position())
py.click(x=219, y=320)
# clicando para voltar ao inicio
# fim do programa