from config.config import turtle_folder, jsonld_folder
from wrapperR import wrapperv2


def execute(x, minPts, eps):
    print(locals())
    result = wrapperv2.core(locals(), "dbscan")
    result.dbscan()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def execute_post(x, minpts, eps):
    result = wrapperv2.core(locals(), "dbscan")
    result.dbscan()
    file = result.parameter.getOutput()
    with open(file) as pmml:
        return pmml.read()


def download(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/dbscan.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/dbscan.jsonld") as file:
            return file.read()


def download_post(file_format):
    if 'turtle' in file_format:
        with open(turtle_folder + "/dbscan.ttl") as file:
            return file.read()
    else:
        with open(jsonld_folder + "/dbscan.jsonld") as file:
            return file.read()
