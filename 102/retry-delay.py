import httpx
from prefect import flow, task



@task(retries=4, retry_delay_seconds=0.1,persist_result=True,log_prints=True)
def fetch_cat_fact():
    cat_fact = httpx.get("https://f3-vyx5c2hfpq-ue.a.run.app/")
    # an endpoint I built that fails sporadically
    if cat_fact.status_code >= 400:
        raise Exception()
    print(cat_fact.text)
    return 1
@flow(log_prints=True)
def fetch():
    fetch_cat_fact()


if __name__ == "__main__":
    fetch()
