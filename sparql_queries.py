triples = """
SELECT ?subject ?predicate ?object
WHERE {
    ?subject ?predicate ?object
}
"""

all_toppings = """
PREFIX pizza: <http://www.semanticweb.org/neelabalan/ontologies/2024/2/PizzaOntology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT * WHERE {
    ?topping rdfs:subClassOf pizza:PizzaTopping .
    ?topping rdfs:subClassOf ?restriction .
    ?restriction rdf:type owl:Restriction .
    ?restriction ?p ?o .
}
"""

is_spicy_pizza = """
PREFIX : <http://www.semanticweb.org/neelabalan/ontologies/2024/2/PizzaOntology#>
SELECT ?pizza WHERE {
    ?pizza a :SpicyPizza .
}
"""

has_caloric_content = """
PREFIX : <http://www.semanticweb.org/neelabalan/ontologies/2024/2/PizzaOntology#>

SELECT ?pizza ?caloricContent
WHERE {
    ?pizza a :Pizza ;
            :hasColoricContent ?caloricContent .
}
"""