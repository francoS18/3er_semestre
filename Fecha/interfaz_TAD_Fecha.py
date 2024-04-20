from TAD import Fecha

fecha1 = Fecha(4,2,2021)
fecha2 = Fecha(5,12,2001)

print(fecha1.getDay())

print(fecha1.getMonth())

print(fecha1.monthName())

print(fecha1.getYear())

print(fecha1.numDays(fecha2))

print(fecha1.isLeapYear())

print(fecha1.compareTo(fecha2))

print(fecha1.__str__())