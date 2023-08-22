# Water Jug Riddle

To build the image run:
```bash
docker build -t water-jug-riddle-image .
```

To execute the app run:
```bash
docker run -d --name water-jug-riddle-container -p 5000:5000 -v ./app:/code water-jug-riddle-image
```