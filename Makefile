run_api:
	uvicorn api:app --reload --port ${PORT}
