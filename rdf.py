# requires rdflib==7.0.0
import csv
import json
from urllib.parse import urlparse
from rdf_wrapper import RdfGraph

import rdflib
import sparql_queries

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


def dump_simplified_ttl():
    with open("simplified_ttl.ttl", "wb") as file:
        g.serialize(file, format="turtle", encoding="utf-8")

def dump_json_ld():
    with open("pizza_ontology.json", "wb") as file:
        g.serialize(file, format="json-ld", encoding="utf-8")


def format_graph_response(response: rdflib.query.Result) -> list[dict[str, str]]:
    json_response = json.loads(response.serialize(format="json").decode())
    print(json_response)
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


def run_some_queries():
    print(json.dumps(format_graph_response(g.query(sparql_queries.is_spicy_pizza)), indent=4))
    print(json.dumps(format_graph_response(g.query(sparql_queries.has_caloric_content)), indent=4))
    print(json.dumps(format_graph_response(g.query(sparql_queries.all_toppings)), indent=4))


if __name__ == "__main__":
    # dump_triples(log=True)
    # dump_simplified_ttl()
    dump_json_ld()
    # run_some_queries()
    # rdf_graph = RdfGraph("pizza_ontology.ttl")
    # print(rdf_graph.get_schema)
