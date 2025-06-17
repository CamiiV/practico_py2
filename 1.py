import datetime
def calcular_edad(fecha_nacimiento):
  """
  Calcula la edad de una persona a partir de su fecha de nacimiento.

  Args:
    fecha_nacimiento: La fecha de nacimiento de la persona, en formato `YYYY-MM-DD`.

  Returns:
    La edad de la persona, en años.
  """

  # Convertimos la fecha de nacimiento a un objeto `datetime`.
  fecha_nacimiento_dt = datetime.datetime.strptime(fecha_nacimiento, "%Y-%m-%d")

  # Obtenemos la fecha actual.
  fecha_actual = datetime.datetime.now()

  # Calculamos la diferencia entre las dos fechas.
  diferencia_fechas = fecha_actual - fecha_nacimiento_dt

  # Obtenemos la edad en años.
  edad = diferencia_fechas.days / 365.2425

  # Devolvemos la edad.
  return edad
a= input()
b= calcular_edad(a)
print(b)