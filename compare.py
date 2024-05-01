import asynchronous
import synchronous
import asyncio
from time import perf_counter


if __name__ == "__main__":
    print("Sync version is working, please wait...")
    start = perf_counter()
    synchronous.fetch_images("./images")
    end = perf_counter()
    print(f"Syn version finished in {(end - start):.02f} seconds")

    print()

    print("Async version is working, please wait...")
    start = perf_counter()
    asyncio.run(asynchronous.fetch_images("./images/"))
    end = perf_counter()
    print(f"Async verison finished in {(end - start):.02f} seconds")
