from fastapi import FastAPI


app = FastAPI(title="TaxGPT Backend")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "TaxGPT backend"}
