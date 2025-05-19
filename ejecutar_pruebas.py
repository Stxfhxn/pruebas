from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def iniciar_navegador():
    driver = webdriver.Chrome()
    return driver

def abrir_pagina(driver, url):
    driver.get(url)

def realizar_operacion(driver, num1, num2, operador):
    num1_input = driver.find_element(By.NAME, "num1")
    num2_input = driver.find_element(By.NAME, "num2")
    operator_select = driver.find_element(By.NAME, "operator")
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")

    num1_input.clear()
    num2_input.clear()
    num1_input.send_keys(str(num1))
    num2_input.send_keys(str(num2))

    # Selección del operador usando teclas (simula flechas hacia abajo)
    operator_select.click()
    for _ in range(operador):
        operator_select.send_keys(Keys.DOWN)

    time.sleep(0.5)  # esperar a que el valor se seleccione
    submit_button.click()
    time.sleep(2)  # Esperar a que se muestre el resultado

def obtener_resultado(driver):
    result_element = driver.find_element(By.XPATH, "//p")
    return result_element.text.strip()

def cerrar_navegador(driver):
    driver.quit()

def probar_operacion(driver, num1, num2, operador, resultado_esperado):
    realizar_operacion(driver, num1, num2, operador)
    resultado_obtenido = obtener_resultado(driver)

    if operador == 0:
        accion = "más"
    elif operador == 1:
        accion = "menos"
    elif operador == 2:
        accion = "por"
    elif operador == 3:
        accion = "entre"
    else:
        accion = "desconocido"

    print(f"\nOperación: {num1} {accion} {num2}")
    print("Resultado esperado:", resultado_esperado)
    print("Resultado obtenido:", resultado_obtenido)

    if str(resultado_esperado) == resultado_obtenido:
        print("✅ ¡Prueba exitosa!")
    else:
        print("❌ ¡Prueba fallida!")

def ejecutar_pruebas():
    driver = iniciar_navegador()
    abrir_pagina(driver, "http://localhost:5000")

    # Pruebas de suma
    probar_operacion(driver, 10, 5, 0, '15.0')
    probar_operacion(driver, 20, 30, 0, '50.0')

    # Pruebas de resta
    probar_operacion(driver, 10, 5, 1, '5.0')
    probar_operacion(driver, 50, 30, 1, '20.0')

    # Pruebas de multiplicación
    probar_operacion(driver, 5, 5, 2, '25.0')
    probar_operacion(driver, 6, 7, 2, '42.0')

    # Pruebas de división
    probar_operacion(driver, 100, 5, 3, '20.0')
    probar_operacion(driver, 50, 2, 3, '25.0')

    cerrar_navegador(driver)

# Ejecutar pruebas
if __name__ == "__main__":
    ejecutar_pruebas()
