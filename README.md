This is a solution for a programming assignment.

To solve the task I used the following set of technologies:
* Python
    * flask
    * pandas
* docker

I've chosen this stack to make my solution concise and easy to read.
While there certainly are better solutions available for bigger datasets and more mature applications, I believe this stack is a good starting point as it allows for fast prototyping.


## How to run

Run the web application on the local machine

```
pip3 install -r requirements.txt
python data_engineering_prj/app.py
```

Now you can open the project in the browser:

```
localhost:5003/
```

Or you can access it from the command line:

```
curl -F 'input_csv=@tests/data.csv' http://localhost:5003/process
```

run tests:

1. ensure you have pytest installed
```
pip3 install pytest
```
2. run
```
pytest tests/
```


## How to deploy

On your local machine

Build docker image

```
docker build -t data_engineering_prj .
docker tag data_engineering_prj  paulatraveler/data_engineering_prj
docker login
docker push paulatraveler/data_engineering_prj
```

Assuming you have docker installed and an http server configured on your server, just use:

```
docker pull paulatraveler/data_engineering_prj
docker run -p 5003:5003 data_engineering_prj
```

If you want to expose the service on another port, then just replace the first 5003 with the port of your choice.
