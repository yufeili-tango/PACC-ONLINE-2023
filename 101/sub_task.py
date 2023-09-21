from prefect import flow, task

@task(retries=4)
def my_first_task(msg):
    print(f"Hello, {msg}")

@task(retries=4)
def my_second_task(msg):
    my_first_task.fn(msg)

@flow
def my_flow():
    my_second_task("Trillian")

if __name__ == "__main__":
    my_flow()