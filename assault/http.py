import asyncio
import os
import requests
import time

# Make the HTTP request and return the results
def fetch(url):
    started_at = time.monotonic()
    response = requests.get(url)
    request_time = time.monotonic() - started_at
    return {"status_code": response.status_code, "request_time": request_time}


# Function to continue to process work from queue
async def worker(name, queue, results):
    """ A function to make requests from a queue and perform the work then add results to the results list. """
    loop = asyncio.get_event_loop()
    while True:
        url = await queue.get()
        if os.getenv("DEBUG"):
            print(f"{name} - Fetch {url}")
        future_result = loop.run_in_executor(None, fetch, url)
        result = await future_result
        results.append(result)
        queue.task_done()
        

# Divide up the work into batches and collect the final results
async def distribute_work( url, requests, concurrency, results):
    queue = asyncio.Queue()

    # Add an item to the queue for each request we want to make
    for _ in range(requests):
        queue.put_nowait(url)

    tasks = []
    for i in range(concurrency):
        task = asyncio.create_task(worker(f"worker-{i+1}", queue, results))
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

# Entrypoint to making requests
def assault(url, requests, concurrency):
    results = []
    asyncio.run(distribute_work(url, requests, concurrency, results))
    print(results)
