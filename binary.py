import json
parameters = []
open_parameters_file = open('parameters_file.json')
load_parameters = json.load(open_parameters_file)
for par in load_parameters["pars"]:
    parameters.append(par)
open_parameters_file.close()
binary = {}
for parameter_number in range(20):
    binary.update({f'parameter{parameter_number}': []})
for parameter_number in range(20):
    for record_number in range(len(parameters)):
        binary[f'parameter{parameter_number}'].append([record_number, parameters[record_number][parameter_number], parameters[record_number][20]])
ordered_binary = {}
max = 20000
for parameter_number in range(20):
    ordered_binary.update({f'parameter{parameter_number}': []})
for parameter_number in range(20):
    for counter in range (max):
        for record_number in range(len(parameters)):
            if binary[f'parameter{parameter_number}'][record_number][1] == counter:
                ordered_binary[f'parameter{parameter_number}'].append(binary[f'parameter{parameter_number}'][record_number])
            else:
                continue
dump_parameters = json.dumps(ordered_binary)
open_parameters_file = open("ordered.json", "a")
open_parameters_file.write(dump_parameters)
open_parameters_file.close()