import httpx  # requests capability, but can work with async
from prefect import flow, task,serve


@task
def fetch_weather(lat: float, lon: float):
    base_url = "https://api.open-meteo.com/v1/forecast/"
    weather = httpx.get(
        base_url,
        params=dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    most_recent_temp = float(weather.json()["hourly"]["temperature_2m"][0])
    return most_recent_temp


@task
def save_weather(temp: float):
    with open("weather.csv", "w+") as w:
        w.write(str(temp))
    return "Successfully wrote temp"


@flow
def pipeline(lat: float, lon: float):
    temp = fetch_weather(lat, lon)
    result = save_weather(temp)
    return result

@flow
def test():
    return True

if __name__ == "__main__":
    pipeline(38.9, -77.0)
    pipeline_deploy=pipeline.to_deployment(name="weather_pipeline_deployment")
    test_deploy=test.to_deployment(name="test_deployment")
    serve(pipeline_deploy,test_deploy)