class Motor:
    def __init__(self, serie_motor, hp):
        self.__serie_motor = serie_motor
        self.__hp = hp
        self.__km_parcursi = 0


class MotorElectric:
    def __init__(self, serie_motor_e, hp_e, consum_electric):
        super().__init__(serie_motor_e, hp_e)
        self.consum_electric = consum_electric


class MotorBenzina:
    def __init__(self, serie_motor, hp, consum_benzina):
        super().__init__(serie_motor, hp)
        self.consum_benzina = consum_benzina


class MotorHibrid(MotorElectric, MotorBenzina):
    def __init__(self, serie_motor, hp, consum_benzina, serie_motor_e, hp_e, consum_electric ):
        MotorElectric.__init__(serie_motor_e, hp_e, consum_electric)
        MotorBenzina.__init__(serie_motor, hp, consum_benzina)


power_horse = MotorHibrid('123123', 150, 5, '612312', 60, '5')


