import requests
from time import perf_counter

SITE = "https://thispersondoesnotexist.com"
IMAGES_QTY = 50


def fetch_images(folder_path: str) -> None:
    for img_number in range(IMAGES_QTY):
        response = requests.get(SITE)
        extension = response.headers["content-type"].split("/")[-1]
        with open(f"{folder_path}/{img_number}.{extension}", "wb") as file:
            file.write(response.content)


if __name__ == "__main__":
    print("Please wait...")
    start = perf_counter("./images")
    fetch_images()
    end = perf_counter()
    print(f"Finished in {(end - start):.02f} seconds")
