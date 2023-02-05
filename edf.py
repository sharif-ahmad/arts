import queue

# Earliest Deadline First
class EDF:

    def __init__(self, env):
        self.stopped = False
        self.sim_env = env
        self.q = queue.PriorityQueue()
        self.running_task = None
        self.completed_tasks = []

    def add_task(self, t):
        self.q.put((t.deadline(), t))

    def run(self):
        while self.should_terminate() is False:
            try:
                (_, top_task) = self.q.get_nowait()
                if self.running_task is None:
                    self.running_task = top_task
                elif top_task.deadline() < self.running_task.deadline():
                    self.add_task(self.running_task)
                    self.running_task = top_task
                else:
                    self.add_task(top_task)
            except queue.Empty:
                pass

            if self.running_task is not None:
                print("executing task {} at {}".format(self.running_task.name, self.sim_env.now))
                self.running_task.execute_for(1, self.sim_env.now)
                if self.running_task.is_completed():
                    self.completed_tasks.append(self.running_task)
                    self.running_task = None

            yield self.sim_env.timeout(1)

    def should_terminate(self):
        return self.stopped or (self.running_task is None and self.q.empty())

    def stop(self):
        self.stopped = True

    def show_report(self):
        total_tat, total_wt = 0, 0
        for t in self.completed_tasks:
            print("process #{}: at({}) bt({}) ct({}) fr({}) rt({}) tat({}) wt({})".format(
                t.name, t.at, t.bt, t.ct, t.fr, t.response_time(), t.turn_around_time(), t.waiting_time()
            ))

            total_wt += t.waiting_time()
            total_tat += t.turn_around_time()

        avg_wt = total_wt / len(self.completed_tasks)
        avg_tat = total_tat / len(self.completed_tasks)

        print("average waiting time: {}\naverage turn around time:{}".format(avg_wt, avg_tat))

