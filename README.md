```

conda create -p dvenv python=3.8 -y


```
```
mkdir dvc
cd dvc
code .
conda create -p venv python=3.8 -y
git init
touch .gitignore
touch README.md
pip install -r requirements.txt
dvc init
dvc repro  #when yaml created staging defined with dependencies
dvc dag
dvc add <file name> #for only single file
git add <file_names> && git commit -m "file added successfully
dvc remote add myremote <any_remote_location>
dvc push
```
