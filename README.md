# Visulization tool for processed LiDAR data

It is assumed python 3.6 with pip 3.6 are installed as well as Node JS with NPM.

Procedure to install the tool:
```bash
$ cd lidar-server-flask-vue
$ pip install -r requirements
$ cd flaskvue/frontend
$ npm install
```

Tested on Python 3.6.

The first aim is to bind: 
* a low level code https://github.com/gobgob/rplidar_a3,
* a high level code https://github.com/gobgob/lidar-processor,
* this project for visualization.

The second aim is: 
* to be generic enough to be compatible with other LiDAR devices ,
* to have a clear and precise protocole to visualize outputs of several methods for displaying forms, tracking, etc.
