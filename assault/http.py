import asyncio
from asyncio import tasks
import queue


def fetch():
    """Make the request and return the results"""
    pass


def worker():
    """A function to take unmake requests from a
    queu and perform the work then add results
    to the results list.
    """
    pass


async def distribute_work(url, requests, concurrency, results):
    """Divide up the work into batches and collect the final results"""
    queue = asyncio.Queue()

    for _ in range(requests):
        queue.put_nowait(url)

    tasks = []
    for i in range(concurrency):
        tasks = asyncio.create_task(worker(f"worker-{i+1}", queue, results))
        tasks.append(task)

    started_at = time.monotonic()
    await queue.join()
    total_time = time.monotonic() - started_at

    for task in tasks:
        task.cancel()

    print("---")
    print(
        f"{concurrency} workers took {total_time:.2f} seconds to complete {len(results)} requests"
    )


def assault(url, requests, concurrency):
    """Entrypoint to making"""
    results = []
    asyncio.run(distribute_work(url, requests, concurrency, results))
    print(results)
