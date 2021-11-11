class Washing:
    def wash(self):
        return "Washing..."

    def methods_processing(self):
        return self.wash()


class Rinsing:
    def rinse(self):
        return "Rinsing..."

    def methods_processing(self):
        return self.rinse()


class Spinning:
    def spin(self):
        return "Spinning..."

    def methods_processing(self):
        return self.spin()


class WashingMachine:
    def __init__(self, subsystem1: Washing = Washing(), subsystem2: Rinsing = Rinsing() , subsystem3: Spinning = Spinning()) -> None:
        self._subsystem1 = subsystem1 or Washing()
        self._subsystem2 = subsystem2 or Rinsing()
        self._subsystem3 = subsystem3 or Spinning()
        self.operation()

    def startWashing(self):
        self.operation()

    def operation(self) -> str:
        results = []
        results.append(self._subsystem1.methods_processing())
        results.append(self._subsystem2.methods_processing())
        results.append(self._subsystem3.methods_processing())
        print("\n".join(results))


washingMachine = WashingMachine()
washingMachine.startWashing()
