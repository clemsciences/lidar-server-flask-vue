# Visualization tool for processed LiDAR data

It is assumed python 3.6 with pip 3.6 are installed as well as Node JS with NPM.

Procedure to install the tool:
```bash
$ cd lidar-server-flask-vue
$ pip install -r requirements
$ cd flaskvue/frontend
$ npm install
$ npm run start
```

Tested on Python 3.6.

The first aim is to bind: 
* a low level code https://github.com/gobgob/rplidar_a3,
* a high level code https://github.com/gobgob/lidar-processor,
* this project for visualization.

The second aim is: 
* to be generic enough to be compatible with other LiDAR devices ,
* to have a clear and precise protocol to visualize outputs of several methods for displaying forms, tracking, etc.

## High-level code

It processes data sent by low-level:
* directly, if there is a direct connection,
* indirectly, if this is the web interface which resends data.

It can display real-time measures as well as recorded measures.

It can locate, map, predict, smooth, filter trajectories.

### Location

Input: list of points whose coordinates are in LiDAR basis.

Output: list of points/groups of points in the map coordinates.

### Mapping

Input: list of points whose coordinates are in LiDAR coordinates.

Output: list of points whose coordinates are in a fix basis.

### Filtering, prediction, smoothing

Input: list of points whose coordinates are in LiDAR coordinates.

Output: filtered, smoothed or predicted coordinates according to a model which depends on how the robot moves, the quality of the LiDAR, environment and measure rate. 

## Web interface

- handles connections,
- displays points in polar or cartesian coordinates
- displays groups of points


### Web interface components

#### Connection to low-level

* Fields: IP address, port
* Buttons: connect, disconnect

#### Connection to high-level

* Fields: IP address, port
* Buttons: connect, disconnect

#### Visualisation configuration

* Fields: number of updates per second

#### Coordinates

* Fields: polar or cartesian

#### Background

* Showing a map
* Showing the environment of the robot
