nested_json = {
"md":[
{
"A": 46066601,
"B": "Silicon Valley",
"C": [
    {
        "D": 46555002,
        "E": 1,
        "F": [
            {
                "G": 46044403,
                "H": "ep",
                "I": "MP",
                "J": 1

            }]
    }]
},
{
    "A": 56555000,
    "B": "Designated Survivor",
    "C": [
        {
            "D": 5605501,
            "E": 1,
            "F": [
                {
                    "G": 56044402,
                    "H": "ep",
                    "I": "P",
                    "J": 1

                }
            ]
        }
    ]
}]}

# Example Recursion with Json flattening.
# Although this could be done with Python Panda's, FlattenDict Library much more conveniently but
# just an application of concept

from collections import defaultdict

def flatten_dict(json, parent_key = '',seperator = '/'):
    d = defaultdict(list)
    def _flatten_dict(obj, parent_key):
            if isinstance(obj,dict):
                for k, v in obj.items():
                    _flatten_dict(v, parent_key + seperator + k)
            elif isinstance(obj, list):
                for elem in obj:
                    _flatten_dict(elem, parent_key)
            else:
                d[parent_key].append(obj)

    _flatten_dict(json,parent_key)
    return d

dd = flatten_dict(nested_json)
print("Hello")