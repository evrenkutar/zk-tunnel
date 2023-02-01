
zktunnel.py
============
Access zookeeper via ssh tunnel to consume and produce messages from your local machine

Requirements
------------
You need python3 in order to use zktunnel.py

* python3
* pip3

**Note:** for AWS mode: you need to tag your ec2 zookeeper instances with Name=zookeeper

see https://aws.amazon.com/premiumsupport/knowledge-center/ec2-resource-tags/

Install
-------

```bash
$ git clone https://github.com/evrenkutar/zk-tunnel
$ make
```

Usage
-----

`zktunnel.py` supports two ways of passing the remote zookeeper/kafka and optionally schema registry IPs:

* automatic retrival by ec2 resource tags (Name=zookeeper/kafka)

```bash
$ zktunnel aws ec2-user@awsjumphost
```

* manual passing your remote zookeeper and optionally schema registry IPs

```bash
$ zktunnel manual ec2-user@awsjumphost 10.11.85.128,10.11.82.30,10.11.83.9
```
afterwards you have to provide your root password in order to create the interfaces

    zookeeper  on 10.11.85.128    port  2181
    zookeeper  on 10.11.82.30     port  2181
    zookeeper  on 10.11.83.9      port  2181
     * adding interface, user password might be needed
    Password:
    connecting to jump host
    Last login: Wed Mar  4 08:19:59 2020 from 203.44.116.49

       __|  __|_  )
       _|  (     /   Amazon Linux AMI
      ___|\___|___|

    [ec2-user@ip-10-11-85-128 ~]$

On a second screen just do whatever you want, e.g. list all topics.

```bash
$ kafka-topics --zookeeper 10.11.85.128:2181 --list
```
