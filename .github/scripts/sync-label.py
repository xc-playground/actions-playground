import sys
import yaml

label_file = './.github/labels.yaml'

if len(sys.argv) != 4 and len(sys.argv) != 5:
    print('  Usage:', sys.argv[0], '<action> <name> <color> [<description>]')
    sys.exit(1)

action = sys.argv[1]
name = sys.argv[2]
color = sys.argv[3]
description = None

if len(sys.argv) == 5:
    description = sys.argv[4]

with open(label_file, 'r') as file:
    labels: list = yaml.safe_load(file)
    if(action == 'created'):
      labels.append({'name': name, 'color': color,
                              'description': description})
    elif action == 'deleted' or action == 'edited':  
      for label in labels:
          if label['name'] == name:
              if action == 'deleted':
                  labels.remove(label)
              else:
                  index = labels.index(label)
                  labels[index] = (
                      {'name': name, 'color': color, 'description': description})
              break
    file.close()

with open(label_file, 'w') as file:
    yaml.safe_dump(labels, file)
    file.close()
