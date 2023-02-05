import srtf
import task
import simpy

env = simpy.Environment()
srft = srtf.SRTF(env)

dm = srft.DM(env)
edf = srft.EDF(env)


def main():
    # env.process(srtf_add_tasks(env))
    # env.process(srtf_schedule(env))

    # env.process(dm_add_tasks(env))
    # env.process(dm_schedule(env))

    # env.process(edf_add_tasks(env))
    # env.process(edf_schedule(env))
    env.run()


def srtf_add_tasks(env):
    srft.add_task(task.Task(1, env.now, 20))
    yield env.timeout(15)
    srft.add_task(task.Task(2, env.now, 25))
    yield env.timeout(15)
    srft.add_task(task.Task(3, env.now, 10))
    yield env.timeout(13)
    srft.add_task(task.Task(4, env.now, 15))
    yield env.timeout(0)

def dm_add_task(env):
    # TODO: implementation
    pass


def edf_add_task(env):
    # TODO: implement
    pass

def srtf_schedule(_):
    for e in srft.run():
        yield e
    srft.show_report()


def dm_schedule(_):
    for e in dm.run():
        yield e
    dm.show_report()


def edf_schedule(_):
    for e in edf.run():
        yield e
    edf.show_report()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
