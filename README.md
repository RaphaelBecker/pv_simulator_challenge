# pv_simulator_challenge
This is a coding challenge as (senior)-software engineer at mobility house 


## PV Simulator Challenge
In this little challenge, we will request you to build an application which allow us to study the interaction between PV power values generated with a Solar Panel and our building consumption (this last one is measured with a Meter connected to the grid).
PV generator curve
The following picture shows the curve of the power output (in kW) of our PV generator during a normal day. This is the power profile that need to simulate:
Architecture
The next diagram describes the interactions of the PV simulator service and other blocks.
 
METER →(Broker) → PV SIMULATOR →[OUTPUT]
 
### A brief description of the components:
 
 * Meter: This entity produces message to the broker between 0 and 9000 Watts -not kW!- and the cadence of messages produced is one per second. The rest of the implementation is up to you, as long as these two conditions are met. The idea is to simulate readings of the electrical consumption of our building.
 * PV generator: It must listen to the broker for the meter values, generate a simulated PV power value based on our curve and subtract this value to the meter value, outputting the result.
 * Writing to a file: The results of the simulation need to be saved in a .csv file, with the timestamp for the generated value, meter, power value (in kW), PV power value and the subtraction of the powers (meter - PV).
 
#### Objectives
A single run of the simulation should give us the result of the measures taken during a whole day, composed by multiple samples taken every couple of seconds.
Because we want to make multiple runs, the simulation *should not be in real time*. In other words, we want the results of an emulated complete day to be available in a couple of minutes.
A few more requirements
 * Write the solution in Python. If you want to add a component on Rust, you are welcome too, but that’s completely optional.
 * Fell free to use any library and/or framework, except for the broker, which we would like to be RabbitMQ.
 * A README with all the steps to run it.
 * We will test your solution on a Debian based OS.
 * Good practices for software development are always appreciated. Tests, even more.
 * Delivery Date: Around 10 working days.
 * If anything is not defined or clear in this document, then feel free to be creative and define it yourself! Just remember to document it for us.

### RabbitMQ
Fundamentals: https://www.rabbitmq.com/tutorials/amqp-concepts.html
 * Routing key and binding key: Exchange is bound via routing key to a queue
 * Exchange type Topic: Queue receives messages from exchange if routing keys partially match binding key
 * Exchange type Fanout: If a queue is bound to an exchange, it will receive the message regardless of any key
 * Exchange type Header: Allows route messages based on header values

### What I have done
 * Kick start from: https://www.rabbitmq.com/tutorials/tutorial-three-python.html
 * Using a Docker as a dev container, because this app will be tested on a debian based OS
   * Example by: https://jolthgs.wordpress.com/2019/09/25/create-a-debian-container-in-docker-for-development/
     * Open cmd: ```docker pull debian:10-slim``` 
     * List running containers: ```docker ps -a```
     * Stopped because too much effort

### Installations regarding RabbitMQ:
 * RabbitMQ client lib for python: ```pip install pika``` 
 * Docker Container for RabbitMQ installation: ```docker run --rm -it --hostname my_rabbitMQ -p 15672:15672 -p 5672:5672 rabbitmq:3-management```
 * In the browser, the rabbitMQ management can be opened via url: ```http://localhost:15672/#/```

### Setup for a fresh Debian OS:
   * ```docker pull debian:10-slim```
   * ```docker run --name debian-buster-slim -h 10-slim -e LANG=C.UTF-8 -it -p 15672:15672 -p 5672:5672 debian:10-slim /bin/bash -l```
   * ```apt update && apt upgrade --yes```
   * ```apt install git```
   * ```apt install nano```
   * ```mkdir pv_project```
   * ```cd pv_project```
   * ```git clone https://github.com/RaphaelBecker/pv_simulator_challenge.git```
   * ```chmod u+x setup.sh```
 
### Dependency installation on debian OS:
   * find out debian version: ```cat /etc/os-release``` -> debian 10
   * Install python 3.9.7:
     * install dependency packages:
       * ```apt install wget software-properties-common build-essential libnss3-dev zlib1g-dev libgdbm-dev libncurses5-dev   libssl-dev libffi-dev libreadline-dev libsqlite3-dev libbz2-dev```
     * Pull 3.9.7:
       * ```wget https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tgz```
       * ```tar xvf Python-3.9.7.tgz```
       * ```cd Python-3.9.7/```
     * Run configuration command:
       * ```./configure --enable-optimizations```
     * Build:
       * ```make altinstall```
     * Check installation:
       * ```python3.9 --version```
     * Upgrade pip:
       * ```python3.9 -m pip install --upgrade pip```
   * Install RabbitMQ:
   * ```cd ..``` 
   * Install erlang:
     * ```wget https://packages.erlang-solutions.com/erlang/debian/pool/esl-erlang_23.1.5-1~debian~stretch_amd64.deb```
     * ```dpkg -i esl-erlang_23.1.5-1~debian~stretch_amd64.deb```
     * ```apt update```
     * ```apt install erlang erlang-nox```
     * ```apt --fix-broken install```
     * ```add-apt-repository 'deb http://www.rabbitmq.com/debian/ testing main'```
     * ```apt update```
   * Install enable rabbit mq server:
     * ```apt install rabbitmq-server```
     * ```systemctl enable rabbitmq-server```
     * ```systemctl start rabbitmq-server```
     * ```cd ..```
     
   * Finally, Setup application:
     * ```python3.9 -m venv venv```
     * ```source venv/bin/activate```

### Or run setup.sh