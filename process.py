import tomllib, json
import os
from collections import defaultdict

from pprint import pprint


tree = lambda: defaultdict(tree)
skip_for_tag_policy = ['required', 'target_id']


this_dir = os.path.dirname(__file__)
with open(os.path.join(this_dir, 'sample-schema.toml'), 'rb') as f:
  schema = tomllib.load(f)

flattened = [ policy | { "tag_key": { "@@assign": tag['key'] } } for tag in schema['tag'] for policy in tag['policy'] ]
by_target = tree()

for policy in flattened:
  target_id = policy['target_id']
  target_id.sort()

  key = policy["tag_key"]["@@assign"]

  by_target[tuple(target_id)]["tags"][key] = ({ k: v for k, v in policy.items() if k not in skip_for_tag_policy })

for target, policy in by_target.items():
  print(f"Policy for targets {target}")
  print(json.dumps(policy, indent=2))
