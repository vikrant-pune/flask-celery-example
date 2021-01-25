import time

from celery import Celery, signature

app = Celery('tasks', broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')
#
# @app.task
# def add(x, y):
#     return x + y


@app.task(track_started = True)
def hello(a, b):
    time.sleep(1)
    # self.update_state(state="PROGRESS", meta={'progress': 50})
    time.sleep(1)
    # self.update_state(state="PROGRESS", meta={'progress': 90})
    time.sleep(1)
    return 'hello world: %i' % (a/b)

@app.task(name="task.completion")
def on_raw_message(task_id):
    print ("Is this call back ---" )
    print(task_id)
    # print(body)

@app.task(name="task.error")
def on_raw_message(task_id):
    print ("Is this error back -- ")
    print(task_id)

if __name__ == '__main__':
    # add.delay(4, 4)
    a, b = 1, 1
    completTask = signature('task.completion')
    errorTask = signature('task.error')

    r = hello.apply_async(args=(a, b), link=completTask, error_callback=errorTask)

    # r.get(on_message=on_raw_message)
    print ("I'm done")
    # print(r.get(on_message=on_raw_message, propagate=False))

