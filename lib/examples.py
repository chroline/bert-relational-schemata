from lib.formatting import convert_conceptnet_uri
from lib.relations import USED_RELATIONS
import pandas as pd
from lib.json import read_from_json_file

inputs = pd.DataFrame(read_from_json_file("inputs"))

inputs.head()


taxonomic_relations, mereological_relations, functional_relations = USED_RELATIONS[
    0:3], USED_RELATIONS[3:6], USED_RELATIONS[6:9]


examples = []

for relation in taxonomic_relations:
    for row in inputs[relation]:
        examples.append((convert_conceptnet_uri(
            row[0]), convert_conceptnet_uri(row[1]), "taxonomic"))

for relation in mereological_relations:
    for row in inputs[relation]:
        examples.append((convert_conceptnet_uri(
            row[0]), convert_conceptnet_uri(row[1]), "mereological"))

for relation in functional_relations:
    for row in inputs[relation]:
        examples.append((convert_conceptnet_uri(
            row[0]), convert_conceptnet_uri(row[1]), "functional"))

examples_df = pd.DataFrame(
    examples, columns=["concept1", "concept2", "relation"])
