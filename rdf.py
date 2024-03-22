# requires rdflib==7.0.0
import csv
from urllib.parse import urlparse

import rdflib

g = rdflib.Graph()
g.parse("pizza_ontology.ttl", format="turtle")


def extract_value(uri):
    return urlparse(uri).fragment


def dump_triples(log: bool = False, with_uri: bool = False):
    with open("triples.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["subject", "predicate", "object"])
        for subj, pred, obj in g:
            if not extract_value(str(subj)):
                continue
            if not with_uri:
                subj, pred, obj  = map(extract_value, ((str(subj), str(pred), str(obj))))
            if log:
                print(f"Subject: {subj}, Predicate: {pred}, Object: {obj}")
            writer.writerow([subj, pred, obj])


if __name__ == "__main__":
    dump_triples(log=True)
