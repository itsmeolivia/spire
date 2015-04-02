To install dependencies run
pip install -r requirements.txt

Start the server by running
python server/app.py

In a separate terminal, to add a job run
python client/mr_manager.py add path/to/my/job

This will return the job ID immediately.

To get a status of a job, run
python client/mr_manager status {job ID}

sample_job is provided as an example for running bash scripts but the shebang
can be changed to run different programs such as a python script.
