class Fecha:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def getDay(self):
        return self.day
    
    def getMonth(self):
        return self.month
    
    def monthName(self):

        months = {
            1: 'Enero',
            2: 'Febrero',
            3: 'Marzo',
            4: 'Abril',
            5: 'Mayo',
            6: 'Junio',
            7: 'Julio',
            8: 'Agosto',
            9: 'Septiembre',
            10: 'Octubre',
            11: 'Noviembre',
            12:'Diciembre '
        }

        if self.month == 1:
            return months[1]
        elif self.month == 2:
            return months[2]
        elif self.month == 3:
            return months[3]
        elif self.month == 4:
            return months[4]
        elif self.month == 5:
            return months[5]
        elif self.month == 6:
            return months[6]
        elif self.month == 7:
            return months[7]
        elif self.month == 8:
            return months[8]
        elif self.month == 9:
            return months[9]
        elif self.month == 10:
            return months[10]
        elif self.month == 11:
            return months[11]
        elif self.month == 12:
            return months[12]
        else:
            return 'Se debe ingresar un mes valido'

    def getYear(self):
        return self.year
    
    def  numDays(self, otherDate):

        # Fecha 1
        diasXmes =  [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
        diasXmesBisiesto = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
        if self.isLeapYear() == True:
            diasAnteriores = sum(diasXmes[:self.month -1])
            diasXano = (self.year - 1) * 366
            totalDias = diasAnteriores + self.day + diasXano
        else:
            diasAnteriores = sum(diasXmesBisiesto[:self.month -1])
            diasXano = (self.year - 1) * 365
            totalDias = diasAnteriores + self.day + diasXano
        
        # Fecha 2
        if otherDate.isLeapYear() == True:
            diasAnterioresOther = sum(diasXmesBisiesto[:otherDate.month - 1])
            diasXanoOther = (otherDate.year - 1) * 366
            totalDiasOther = diasAnterioresOther + otherDate.day + diasXanoOther
        else:
            diasAnterioresOther = sum(diasXmes[:otherDate.month - 1])
            diasXanoOther = (otherDate.year - 1) * 365
            totalDiasOther = diasAnterioresOther + otherDate.day + diasXanoOther

        # Verificacion de resultado positivo
        total = totalDias - totalDiasOther
        if total < 0 :
             return total * (-1)
        else: 
            return total

    def isLeapYear(self):

        # Calculos Para comprobar años biciestos
        if self.getYear() % 4 == 0:
            if  self.getYear() % 100 == 0:
                if self.getYear() % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
        
    def compareTo(self,otherDate):

        # Comparar 2 fechas para conocer cual es mayor
        if self.getYear == otherDate.getYear() and self.getMonth == otherDate.getMonth() and self.day == otherDate.getDay():
            return 0
        elif self.year > otherDate.getYear():
            return 1
        elif self.year < otherDate.getYear():
            return -1
        elif self.year == otherDate.getYear():
            if self.month > otherDate.getYear():
                return 1
            elif self.month < otherDate.getMonth():
                return -1
            elif self.month == otherDate.getMonth():
                if self.day > otherDate.getDay():
                    return 1
                elif self.day < otherDate.getDay():
                    return -1

    def __str__(self):
        
        # Devuelve la fecha en formato DD/MM/AAAA
        return f'{self.day:02d}/{self.month:02d}/{self.year:04d}'
