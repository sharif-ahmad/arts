class Task:

    def __init__(self, name, at, bt):
        self.ct = 0
        self.et = 0
        self.fr = 0
        self.name = name
        self.at = at
        self.bt = bt

    def execute_for(self, d, now):
        if self.fr == 0:
            self.fr = now
        self.et += d
        if self.remaining_time() == 0:
            self.ct = now + d

    def remaining_time(self):
        return self.bt - self.et

    def turn_around_time(self):
        return self.ct - self.at
        
    def waiting_time(self):
        return self.turn_around_time() - self.bt

    def response_time(self):
        return self.fr - self.at

    def is_completed(self):
        return self.remaining_time() == 0


class DeadlinedTask(Task):

    def __init__(self, name, at, bt, dl):
        super(DeadlinedTask, self).__init__(name, at, bt)
        self.dl = dl


class FixedDeadlinedTask(DeadlinedTask):

    def __init__(self, name, at, bt, dl):
        super(FixedDeadlinedTask, self).__init__(name, at, bt, dl)

    def __lt__(self, other):
        return self.dl < other.dl

    def deadline(self):
        return self.dl


class DynamicDeadlinedTask(DeadlinedTask):

    def __init__(self, name, at, bt, dl):
        super().__init__(self, name, at, bt, dl)

    def deadline(self):
        return self.at + self.dl
