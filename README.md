## Background

GCP Deployment Manager is an infrastructure deployment service that automates the creation and management of Google Cloud Platform resources.



>“Toil is the kind of work tied to running a production service that tends to be manual, repetitive, automatable, tactical, devoid of enduring value, and that scales linearly as a service grows.”

Source: [Site Reliability Engineering, O’Reilly (Chapter 5)](https://landing.google.com/sre/book/chapters/eliminating-toil.html)

### Features
- Powerful: Specify all the resources needed for your application in a declarative yaml format and allow reuse of common deployment patterns.
- Declarative: A declarative approach allows the user to specify what the configuration should be and let the system figure out the steps to take.
- Repeatable: Configuration files which define the resources, the process of creating those resources can be repeated over and over with consistent results.
- Tenmplate-driven: Create “building block” abstractions over sets of resources that are typically deployed together. Parameterize Jinja2 templates to allow them to be reused by changing input values. 

## Scenario

This sample code will demonstrate using Google Cloud Deployment Manager to automate the deployment of a GlusterFS cluster with an easily configurable number of nodes, exporting a single replicated volume (number of replicas is also parameterized).

### Build/Configuration Steps

#### All nodes:

- Create “brick” devices as persistent disks (PD-SSD)
- Create GCE instances
- Attach brick devices to instances
- Create filesystem on brick device
- Install GlusterFS packages

#### “Master” node:

- Probe cluster peers
- Create Gluster replicated volume
- Start Gluster replicated volume

## Pre-requisites

- GCloud SDK (alternatively can use Cloud Shell)
- GCP project

## Usage

### Preview deployment

~~~bash
$ gcloud deployment-manager deployments create <name> --config=gluster.yaml --preview   
~~~

### Deploy previewed deployment

~~~bash
$ gcloud deployment-manager deployments update <name> --config=gluster.yaml   
~~~






