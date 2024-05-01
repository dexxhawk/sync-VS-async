import asyncio
import aiohttp
import aiofiles
from time import perf_counter

SITE = "https://thispersondoesnotexist.com"
IMAGES_QTY = 50


async def fetch_image(folder_path: str, img_number: int) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(SITE) as response:
            extension = response.headers["content-type"].split("/")[-1]
            async with aiofiles.open(
                f"{folder_path}/{img_number}.{extension}", "wb"
            ) as file:
                async for chunk in response.content.iter_chunked(64 * 1024):
                    await file.write(chunk)


async def fetch_images(folder_path: str) -> None:
    tasks = []
    for img_number in range(IMAGES_QTY):
        tasks.append(asyncio.create_task(fetch_image(folder_path, img_number)))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    print("Please wait...")
    start = perf_counter()
    asyncio.run(fetch_images("./images/"))
    end = perf_counter()
    print(f"Finished in {(end - start):.02f} seconds")
