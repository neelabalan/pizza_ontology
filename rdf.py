# requires rdflib==7.0.0
import csv
import json
from urllib.parse import urlparse

import rdflib

g = rdflib.Graph()
g.parse("pizza_ontology.ttl", format="turtle")


def extract_value(uri: str) -> str:
    return urlparse(uri).fragment


def dump_triples(log: bool = False, with_uri: bool = False):
    with open("triples.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["subject", "predicate", "object"])
        for subj, pred, obj in g:
            if not extract_value(str(subj)):
                continue
            if not with_uri:
                subj, pred, obj = map(extract_value, ((str(subj), str(pred), str(obj))))
            if log:
                print(f"Subject: {subj}, Predicate: {pred}, Object: {obj}")
            writer.writerow([subj, pred, obj])


def format_graph_response(response: rdflib.query.Result) -> list[dict[str, str]]:
    json_response = json.loads(response.serialize(format="json").decode())
    response = []
    bindings = json_response.get("results", {}).get("bindings")
    if not bindings:
        return []
    for binding in bindings:
        _result = {}
        for key, value in binding.items():
            _result.update({key: value.get("value")})
        response.append(_result)
    return response


if __name__ == "__main__":
    dump_triples(log=True)
