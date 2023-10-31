from fastapi import FastAPI

class Counter:
    def __init__(self, count) -> None:
        self.counter = count

    def increment(self):
        self.counter = self.counter + 1



counter = Counter(5)
app = FastAPI()


@app.get("/api/count")
async def get_count():
    return {"count": counter.counter}

@app.post("/api/count")
async def update_count():
    counter.increment()
    return {"count": counter.counter}


