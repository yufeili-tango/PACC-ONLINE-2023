from prefect import flow, task
import pandas as pd


@task(persist_result=True)
def my_task():
    df = pd.DataFrame(dict(a=[2, 3], b=[4, 5]))
    print("111111111111111111")
    return 111111111111


@flow()
def my_flow():
    res = my_task()


my_flow()
