@echo off
call conda activate microrender
black ..\microrender
isort ..\microrender
nbqa black ..
nbqa isort ..
call conda deactivate