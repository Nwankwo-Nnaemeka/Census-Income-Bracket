### SERVING YOUR MODEL USING DOCKER
Having your server code in the main.py, and you want to try it locally (given that you have the required dependencies installed) you can spin up the server by using the command `uvicorn main:app --reload` while on the same directory as the `main.py` file . **However dockerizing it will be the best choice as it will help serve your code with all its dependencies**.
Base on the `FastAPI` [Documentation](https://fastapi.tiangolo.com/deployment/docker/)  on how to deploy with Docker. This should result in a directory structure that looks like this:
```
..
└── no-batch
    ├── app/
    │   ├── main.py (server code)
    │   └── model.pkl (serialized classifier)
    ├── requirements.txt (Python dependencies)
    ├── income-examples/ (wine examples to test the server)
    ├── README.md (this file)
    └── Dockerfile
```
### BUILD AND RUN IMAGE
After getting your DockerFile ready with everything you need. You can build the image by running this command:
```bash
docker build -t incomepred:no-bacth . 
```
Now that the image has been successfully built it is time to run a container out of it. You can do so by using the following command:
```bash 
docker run --rm -p 80:80 incomepred:no-batch
```
FastAPI has a built-in client for you to interact with the server. You can use it by visiting [localhost:80/docs](http://localhost:80/docs). But You can make a request to the server by sending `POST` requests to the server and every request should contain the data in `JSON` format. You can also use `curl` and send the data directly with the request like this (notice that you need to open a new terminal window for this as the one you originally used to spin up the server is logging info and is not usable until you stop it):

```bash
curl -X POST http://localhost:80/predict \
    -d @./income-examples/1.json \
    -H "Content-Type: application/json"
```