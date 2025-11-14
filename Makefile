.PHONY: run-main1
run-main1:
	poetry run uvicorn main1:app --reload

.PHONY: run-main2
run-main2:
	poetry run uvicorn main2:app --reload

.PHONY: run-main3
run-main3:
	poetry run uvicorn main3:app --reload

.PHONY: run-main4
run-main4:
	poetry run uvicorn main4:app --reload
