#Pranav Mishra
#BioCompute Object Creator Minimum Viable Product
import os
import json
import jsons
import sys
import hashlib
from json import JSONEncoder
from pprint import pprint
from datetime import datetime
try:
    import cPickle as pickle
except ModuleNotFoundError:
    import pickle

class BCO():
   def __init__(self, provenance, usability, description, execution, io, object_id, spec_version, etag = "new", parametric = None, error = None, extension = None):
       self.provenance_domain = provenance
       self.usability_domain = usability
       self.extension_domain = extension
       self.description_domain = description
       self.execution_domain = execution
       self.parametric_domain = parametric
       self.io_domain = io
       self.error_domain = error
       self.object_id = object_id
       self.spec_version = spec_version
       self.etag = etag
   def startCall(): 
      pass
   def endCall(): 
      pass

   def default(self, object):
      if isinstance(object, BCO):
         return object.__dict__
      else: 
         return json.JSONEncoder.default(self, object)
       
class provenance_domain():
   def __init__(self, name, version, license, created, modified, contributors, embargo=None, derived_from=None, obsolete_after=None, review=None):
       self.embargo = embargo #object
       self.created = created #string date-time
       self.modified = modified #string date-time
       self.name = name #string 
       self.version = version #string 
       self.derived_from = derived_from #$ref
       self.obsolete_after = obsolete_after #string
       self.license = license #string
       self.review = review #array of reviews 
       self.contributors = contributors #array of contributors
class embargo():
   def __init__(self, start_time, end_time):
       self.start_time = start_time #string
       self.end_time = end_time #string
class review():
   def __init__(self, reviewer, status, date=None, reviewer_comment=None):
       self.reviewer = reviewer #$ref
       self.status = status #string from statuses
       self.reviewer_comment = reviewer_comment #string
       self.date = date #string date-time
class status():
   def __init__(self, status):
      statuses = ["unreviewed", "in-review", "approved", "rejected", "suspended"]
      self.status = status #string
class reviewer():
   def __init__(self, name, email=None, contribution=None, orcid=None, affiliation=None):
       self.name = name #string
       self.affiliation = affiliation #string
       self.email = email #string
       self.orcid = orcid #string
       self.contribution = contribution #array of contributions
class contributor():
   def __init__(self, name, contribution, affiliation=None, email=None, orcid=None):
       self.name = name #string
       self.affiliation = affiliation #string 
       self.email = email #string 
       self.orcid = orcid #string
       self.contribution = contribution #string
class contribution():
   def __init__(self, contribution):
       contributions = ["authoredBy", "contributedBy", "createdAt", "createdBy", "createdWith", "curatedBy", "derivedFrom", "importedBy", "importedFrom", "providedBy", "retrievedBy", "retrievedFrom", "sourceAccessedBy"]
       self.contribution = contribution #string

class description_domain():
   def __init__(self, keywords, pipeline_steps, xref=None, platform=None):
      self.keywords = keywords #array of strings
      self.xref = xref #array of xrefs
      self.platform = platform #array of strings
      self.pipeline_steps = pipeline_steps #array of pipeline step objects
# class keyword():
#    def __init__(self, keyword): 
#       self.keyword = keyword
class xref():
   def __init__(self, namespace, name, ids, access_time):
      self.namespace = namespace #string 
      self.name = name #string
      self.ids = ids #array of ids
      self.access_time = date #string
# class platform():
#    def __init__(self, platform):
#       self.platform = platform
class pipeline_step():
   def __init__(self, step_number, name, description, input_list, output_list, version=None, prerequisite=None):
      self.step_number = step_number #integer 
      self.name = name #string
      self.description = description #string
      self.version = version #string
      self.prerequisite = prerequisite #array of prerequisite objects
      self.input_list = input_list #array of uris, composed of uris ($ref)
      self.output_list = output_list #carray of uris, composed of uris ($ref)
class prerequisite():
   def __init__(self, name, uri = None):
      self.uri = uri #$ref, NOT uri object ($ref)
      self.name = name #string
class uri(): 
   def __init__(self, uri, filename=None, sha1_checksum=None, access_time=None):
      self.filename = filename
      self.uri = uri
      self.sha1_checksum = sha1_checksum
      self.access_time = access_time
# class input(): #item in input_list 
#    def __init__(self, filename=None, uri=None, sha1_checksum=None, access_time=None):
#       self.filename = filename
#       self.uri = uri
#       self.sha1_checksum = sha1_checksum
#       self.access_time = access_time
# class output(): #item in output_list 
#    def __init__(self, filename=None, uri=None, sha1_checksum=None, access_time=None):
#       self.filename = filename
#       self.uri = uri
#       self.sha1_checksum = sha1_checksum 
#       self.access_time = access_time

class execution_domain():
   def __init__(self, environment_variables, script_driver, software_prerequisites, external_data_endpoints, script):
      self.environment_variables = environment_variables #object
      self.script = script #array of uris to script objects
      self.script_driver = script_driver #string
      self.software_prerequisites = software_prerequisites #array of software prerequisite objects
      self.external_data_endpoints = external_data_endpoints
class environment_variable():   
   def __init__(self, key, value):
      self.key = key #string
      self.value = value #string
class environment_varibles():
   def __init__(self, environment_variables):
      self.environment_variables = environment_variables
class script_item():
   def __init__(self, uri):
      self.uri = uri 
class software_prerequisite():
   def __init__(self, version, name, uri):
      self.uri = uri #NOT uri object ($ref) 
      self.version = version #string
      self.name = name #string
class external_data_endpoint():
   def __init__(self, name, url):
      self.name = name #string
      self.url = url #string

class io_domain():
   def __init__(self, input_subdomain, output_subdomain):
      self.input_subdomain = input_subdomain #array of inputs
      self.output_subdomain = output_subdomain #array of outputs
class input_subdomain_item:
   def __init__(self, uri):
      self.uri = uri 
class output_subdomain_item:
   def __init__(self, uri, mediatype):
      self.uri = uri #NOT uri object ($ref)
      self.mediatype = mediatype #string
      
class error_domain():
   def __init__(self, empirical, algorithmic):
      self.empirical_error = empirical #object  
      self.algorithmic_error = algorithmic #object
# class empirical_error():
#    def __init__(self, empirical_error):
#       self.empirical_error = empirical_error #string
# class algorithmic_error():
#    def __init__(self, algorithmic_error):  
#       self.algorithmic_error = algorithmic_error #string

# class extension_domain():
#    def __init__(self, extension_schema):
#       self.extension_schema = extension_schema

class usability_domain():
   def __init__(self, use):
      self.use = use #string

# class parametric_domain():
#    def __init__(self, parameters):
#        self.parameters= parameters #array
class parameter:
   def __init__(self, param, value, step):
      self.param = param #string 
      self.value = value #string 
      self.step = step #string 

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def remove_nulls(d):
    return {k: v for k, v in d.items() if v is not None}

def main():
#    data = {}
#    with open('blank_bco.json') as json_file: #testing 
#       data = json.load(json_file)
      #print(data)
   #insert code below 
   
   #take output of script command
   #for finding steps, split by "|"    
   
   #metadata
   print(color.CYAN + "Welcome to the BioCompute Command Line Tool. With this tool, you can automate some parts of BCO creation and work on creating a BCO directly from the command line. \nIf you make a mistake while creating your BCO, you can always edit that field in the output json file that represents your BCO.\n" + color.END)
   input_filename = r'' + input("Enter name of desired input file (Output of script command/typescript): ")
   data = ""
   try:
      with open(input_filename, 'r') as file: 
         data = file.read()
   except FileNotFoundError:
      print(color.RED + "error: input file not found. please restart this tool with correct input file." + color.END)
      sys.exit()
   index_of_first_newline = 0
   for x in range(0, len(data)):
      if data[x] == "\n":
         index_of_first_newline = x
         break
   data = data[index_of_first_newline+1:]
   index_of_start = 0
   for x in range(0, len(data)):
       if data[x] == "$" or data[x] == "#": #user or root
          index_of_start = x
          break        
   data = data[int(index_of_start+1): int(data.index('\n'))]
   print("\nPipeline: " + data)
#    print("\n")
   confirmation = input("Confirm pipeline (y or n): ")
   if confirmation.lower() == "n":
      data = input("Enter the correct pipeline: ")
      
   pipeline = data.split("|")
   for x in range(0, len(pipeline)):
      pipeline[x] = pipeline[x].lstrip()
      pipeline[x] = pipeline[x].rstrip()
   
   output_filename = input("Enter name of desired output file (e.g. example_bco.json): ")
   
   print(color.BOLD + "\nMetadata Information\n" + color.END)
   
   object_id = input("Enter unique BCO Object ID (e.g. https://portal.aws.biochemistry.gwu.edu/bco/BCO_00026662). Ensure the id part ('00026662') is not in use : ")
   
   etag = "new" 
   etag_input = input("Enter etag value (default is 'new') For default, enter nothing.: ")
   if etag_input.strip() != etag.strip() and etag_input.strip() !=  "":
      etag = etag_input
      
   spec_version = "https://w3id.org/ieee/ieee-2791-schema/"
   spec_version_input = input("Enter version of specification for this IEEE-2791 object (BCO) (Default is: https://w3id.org/ieee/ieee-2791-schema/) For default, enter nothing.: ")
   if spec_version_input.strip() != spec_version.strip() and spec_version_input.strip() != "":
      spec_version = spec_version_input
#    print("\n")
   
   #provenance
   print("\n" + color.BOLD + "Provenance Domain Information\n" + color.END)
   name = input("Enter name of BioCompute Object: ")
   now = datetime.now()
   created = now.strftime("%m/%d/%Y-%H:%M:%S")
   modified = now.strftime("%m/%d/%Y-%H:%M:%S")
   license = input("Enter a license if this BCO is not exclusively for personal use: ")
   version = "1.0"
   version_input = input("Following semantic versioning, enter a name for this BCO (default is 1.0). For default, enter nothing.: ")
   if version_input.strip().lower() != version.strip().lower() and version_input.strip().lower() != "":
      version = version_input
   
   add_contributor = "y"
   contributions = ["authoredBy", "contributedBy", "createdAt", "createdBy", "createdWith", "curatedBy", "derivedFrom", "importedBy", "importedFrom", "providedBy", "retrievedBy", "retrievedFrom", "sourceAccessedBy"] 
   contributors = []
   while(add_contributor.lower().strip() == "y"):
      contributor_name = input("Enter name of contributor: ")
      print("Contribution Types: ", " ".join(contributions)) 
      contribution_input = input("Enter contribution type: ").strip()
      contribution = []
      contribution.append(contribution_input)
      contributors.append(contributor(name = contributor_name, contribution = contribution))
      add_contributor = input("Add another contributor? y/n: ")
   provenance = provenance_domain(name = name, version = version, license = license, created = created, modified = modified, contributors = contributors)
#    print("\n")   
   
   #usability
   print("\n" + color.BOLD + "Usability Domain Information \n" + color.END)
   use = input("What is the purpose of this computational workflow/analysis?: ")
#    usability = usability_domain(use)
   usability = []
   usability.append(use)
   
   #execution 
   print(color.BOLD + "\nExecution Domain Information" + color.END)
   print("Enter script uris in the following format: 'uri1 uri2 uri3 uri4'")
   script_input = input("\nEnter the uris for the script objects used to perform computations: ")
   script = []
   script_list = script_input.lstrip().rstrip().split(" ")
   for x in script_list:
      script.append(script_item(uri(uri=x)))
   script_driver = "shell"
   script_driver_input = input("\nEnter script driver, the type of executable to perform commands in script in order to run the pipeline (Default is shell) Enter nothing for default.: ")
   if script_driver_input.lower().strip() != script_driver.lower().strip() and script_driver_input.lower().strip() != "":
      script_driver = script_driver_input
   software_prerequisites = []
   add_software_prerequisite = "y"
   print("\nSoftware prerequisites are necessary prerequisites such as libraries and tool versions that are needed to run the script to produce this BCO.\nThey have a name, version, and uri.\n")
   while(add_software_prerequisite.lower().strip() == "y"):
      sp_name = input("Enter software prerequisite name: ")
      sp_version = input("Enter software prerequisite version: ")
      sp_uri = input("Enter software prerequisite uri: ")
      software_prerequisites.append(software_prerequisite(version = sp_version, name = sp_name, uri = uri(uri=sp_uri)))
      add_software_prerequisite = input("Add another software prerequisite? y/n: ")
   external_data_endpoints = []
   add_external_data_endpoints = "y"
   print("\nExternal data endpoints are requirements for network protocol endpoints used by a pipeline.\nThey have a name and a url.\n")
   while(add_external_data_endpoints.strip().lower() == "y"):
      ede_name = input("Enter external data endpoint name: ")
      ede_url = input("Enter external data endpoint url: ")
      external_data_endpoints.append(external_data_endpoint(name = ede_name, url = ede_url))
      add_external_data_endpoints = input("Add another external data endpoint? y/n: ")
   add_environment_variable = "y"
   print("\nEnter environment variables in 'key value' format \n")
   environment_variables = []
   while(add_environment_variable.strip().lower() == "y"):
      key_value_pair = input("Enter environmental parameters that are useful to configure the execution environment on the target platform: ").lstrip().rstrip()
      try:
         env_variable = environment_variable(key_value_pair.split(" ")[0], key_value_pair.split(" ")[1])
         environment_variables.append(env_variable)
      except:
         print("There was an error with your input. Please try again.")
      add_environment_variable = input("Add another environment variable? y/n: ") 
   execution = execution_domain(environment_variables = environment_variables, script_driver = script_driver, software_prerequisites = software_prerequisites, external_data_endpoints = external_data_endpoints, script = script)
   
   #description
   print("\n" + color.BOLD + "Description Domain Information \n" + color.END)
   print("Format to enter keywords in: 'keywordA keywordB keywordC keywordD'")
   keywords_input = input("Enter biology research keywords in the specified format to aid in search-ability and description of this object: ").lstrip().rstrip()# .split(" ")
   keywords = []
   keywords.append(keywords_input)
   pipeline_steps = []
   input_list_description_domain = []
   output_list_description_domain = []
   step_number = 1
   input_list_master = []
   output_list_master = []
   while(step_number != len(pipeline) + 1): #step number cannot exceed number of steps 
      print("Current step number: {}".format(step_number))
      name = pipeline[step_number-1].split(" ")[0]
      print("Name of tool: {}".format(name))
      name_input = input("If name of tool is not correct, enter correct name. Else, enter nothing.: ")
      if name_input.lower().strip() != name.lower().strip() and name_input.lower().strip() != "":
         name = name_input
      description = input("Enter purpose of the tool: ")
      # version = input("Enter version of the tool: ")
      print("\nEnter input file uris in the following format: 'uri1 uri2 uri3 uri4'\n")
      input_list_temp = input("Enter input file uris if this step uses input files: ").lstrip().rstrip().split(" ")
      for x in range(len(input_list_temp)):
          input_list_temp[x] = uri(uri=input_list_temp[x])
      print("\nEnter output file uris in the following format: 'uri1 uri2 uri3 uri4'\n")
      output_list_temp = input("Enter output file uris if this step outputs to files: ").lstrip().rstrip().split(" ")
      for x in range(len(output_list_temp)):
         output_list_temp[x] = uri(uri=output_list_temp[x])
      print()
      pipeline_steps.append(pipeline_step(step_number=step_number, name=name, description=description, input_list= input_list_temp, output_list = output_list_temp))
      if step_number == 1:
         for x in input_list_temp:
            if x.uri!= "":
               input_list_master.append(x)
      if step_number == len(pipeline):
         for x in output_list_temp:
            if x.uri != "":
               output_list_master.append(x)
         
      step_number += 1  
   description = description_domain(keywords = keywords, pipeline_steps = pipeline_steps)

   #IO 
   print(color.BOLD + "Input Output (IO) Domain Information \n" + color.END)
   inputs = []
   for x in input_list_master:
       inputs.append(input_subdomain_item(uri=x))
         
   print("Current input list: ")
   for x in inputs:
      print(x.uri.uri)
   add_input = input("Do you want to add additional input files? y/n: ")
   while(add_input.strip().lower() == "y"):
      input_file_uri = input("Enter input file uri: ")
      inputs.append(input_subdomain_item(uri = uri(uri=input_file_uri)))
      add_input = input("Add an input file? y/n: ")
         
   print("Current output list: ")
   for x in output_list_master:
      print(x.uri)
   print()
   outputs = []
   for output in output_list_master: 
      print(output.uri)
      output_mediatype = input("Enter output file mediatype for this output file: ")
      outputs.append(output_subdomain_item(uri=output, mediatype=output_mediatype))
   add_output = input("Do you want to add additional output files? y/n: ")
   while(add_output.strip().lower() == "y"):
      output = input("Enter output file uri: ")
      output_mediatype = input("Enter output file mediatype: ")
      outputs.append(output_subdomain_item(uri=uri(uri=output), mediatype=output_mediatype))
      add_output = input("Add an output file? y/n: ")
   io = io_domain(inputs, outputs) 
      
   #parametric
   print(color.BOLD + "\nParametric Domain Information \n" + color.END)
   print("This represents the list of NON-default parameters customizing the computational flow which can affect the output of the calculations.\nThese fields can be custom to each kind of analysis and are tied to a particular pipeline implementation.")
   print("Parameters are composed of a param (specific variable for computational workflow), a value (non-default param value), and a step (specific step in workflow relevant to param and value)")
   parameters = []
   option_index = -1
   partial_string = ""
   param = ""
   value = ""
   step = ""
   edit_parameter = ""
   add_parameter = ""
   delete_parameter = ""
   for x in range(0, len(pipeline)):
      print()
      partial_string = ""
      param = ""
      value = ""
      step = ""
      edit_parameter = ""
      add_parameter = ""
      delete_parameter = ""
      if " -" in pipeline[x]:
         option_index = pipeline[x].index(" -") 
         partial_string = pipeline[x][option_index+1:]
         param = pipeline[x].split(" ")[0]
         value = partial_string[0: partial_string.index(" ")]
         step = str(x+1)

      print("Current step number: {}".format(str(x+1)))
      print()
      print("param: ", param)
      print("value: ", value)
      print("step: ", step)
      print("Current pipeline info: {}".format(pipeline[x]))
      if param == "" and value == "" and step == "":
         add_parameter = input("No parameter has been found. Is there a non-default parameter you wish to add? y/n: ")  
         if add_parameter.strip().lower() == "y":
            param = input("Enter param: ")
            value = input("Enter value: ")
            step = input("Enter step: ")          
            parameters.append(parameter(param=param, value=value, step=step))    
            continue        
         else:
            continue 
             
      delete_parameter = input("Would you like to delete the current parameter? (Note: you can edit parameter in the next step) y/n: ")
      if delete_parameter.lower().strip() == "y":
         param = ""
         value = ""
         step = ""
         continue 
      edit_parameter = input("Would you like to edit the current parameter? y/n: ")
      if edit_parameter.strip().lower() == "y":
         param = input("Enter param: ")
         value = input("Enter value: ")
         step = input("Enter step: ")
         parameters.append(parameter(param=param, value=value, step=step))
      
      parameters.append(parameter(param=param, value=value, step=step))
         
   parametric = parameters# parametric_domain(parameters)   
   
   #Error 
   print(color.BOLD + "\nError Domain Information \n" + color.END)
   emp_error = ""
   alg_error = ""
   empirical_error = {}
   algorithmic_error = {}
   add_error_domain = input("This domain is optional. Would you like to add an error domain? y/n: ")
   add_emp_error = ""
   add_alg_error = ""
   if add_error_domain.strip().lower() == "y":
      print("\nEmpirical error is defined as empirically determined values such as limits of detectability, false positives, false negatives, statistical confidence of outcomes, etc.\nThis can be measured by running the algorithm on multiple data samples of the usability domain or through the use of carefully designed in-silico data.\n") 
      add_emp_error = input("Would you like to add an empirical error subdomain for this BCO? y/n: ")
      while(add_emp_error.strip().lower() == "y"):
         print("An example of an input would be: 'false_negative_alignment_hits <0.0010'")
         emp_error = input("Enter an empirical error 'key value' pair for this BCO: ")
         try:
            empirical_error[emp_error.split(" ")[0]] = emp_error.split(" ")[1]
         except:
            print("Error with input. Please retry or press 'n' at the next command.")
         add_emp_error = input("Would you like to add another empirical error 'key value' pair for this BCO? y/n: ")
      print("\nAlgorithmic error is defined as descriptive of errors that originate by fuzziness of the algorithms, driven by stochastic processes, in dynamically parallelized multi-threaded executions, or in machine learning methodologies where the state of the machine can affect the outcome.\n")
      add_alg_error = input("Would you like to add an algorithmic error subdomain for this BCO? y/n: ")
      while(add_alg_error.strip().lower() == "y"):
         print("An example of an input would be: 'algorithm description' or 'algorithm json_schema_uri' where the json_schema_uri would be uri for algorithm description.")
         alg_error = input("Enter an algorithmic error description for this BCO: ")
         try:
            algorithmic_error[alg_error.split(" ")[0]] = alg_error.split(" ")[1]
         except:
            print("Error with input. Please retry or press 'n' at the next command.")
         add_alg_error = input("Would you like to add another algorithmic error 'algorithm description' or 'algorithm json_schema_uri' pair for this BCO? y/n: ")         
      
   error = error_domain(empirical=empirical_error, algorithmic=algorithmic_error)
   
   #Extension
   print(color.BOLD + "\nExtension Domain Information \n" + color.END)
   extension = []
   add_extension_domain = input("This domain is optional. Would you like to add an extension domain? y/n: ")
   if add_extension_domain.strip().lower() == "y":
      while add_extension_domain.strip().lower() == "y":
         extension.append(input("Enter a uri that points to an extension json schema: ").lstrip().rstrip())
         add_extension_domain = input("Would you like to add another extension json schema? y/n: ")
   
   
                
   output_bco = BCO(provenance = provenance, usability = usability, description = description, execution = execution, io = io, object_id = object_id, spec_version = spec_version, etag = etag, parametric = parametric, error=error, extension=extension)
   print(color.BOLD + "\nBCO Information" + color.END)
   print(color.CYAN + "You can edit the output .json file if you made a mistake or would like to edit any fields in your BioCompute Object." + color.END)
   print(color.GREEN + "BCO created" + color.END)
   
   try:
      print(color.GREEN + "{}".format(output_bco) + color.END) 
      print(color.GREEN + "BCO printed" + color.END)
   except:
      print(color.RED + "error occured with printing"+ color.END) 
#    try:
#       with open(output_filename + ".pkl", 'wb') as output_pickle_file:
#          pickle.dump(output_bco, output_pickle_file, pickle.HIGHEST_PROTOCOL)
#          print(color.GREEN + "BCO saved to .pkl file" + color.END) 
#    except:
#       print(color.RED + "error with saving BCO to .pkl file" + color.END)
   
#    with open(output_filename + ".pkl", 'rb') input_pickle_file: #to open saved pkl file 
#       loaded_bco = pickle.load(input_pickle_file)
   new_data = ""
   with open(output_filename, 'w') as json_output:
       try:
          new_data = jsons.dumps(output_bco)
          res = json.loads(new_data, object_hook=remove_nulls)
          json.dump(res, json_output)
          print(color.GREEN + "BCO saved in .json format" + color.END) # CORRECT
       except:
         print(color.RED + "error with saving BCO to .json file" + color.END)

#       try: 
#          json_string = BCOEncoder().encode(output_bco)
#          json_output.write(json_string)
#          json_output.close()
      # json_output.write(json.dumps(output_bco))
#       json_output.write(jsons.dumps(output_bco)) # CORRECT
#       except:
#    new_data = ""
#    with open(output_filename, 'r') as json_input:
#       new_data = json.loads(json_input, object_hook=remove_nulls)
#    with open(output_filename, 'w') as json_output:
#       json_output.truncate(0)
#       json_output.write(new_data) 
      # print(color.RED + "error occured with outputting as a json file" + color.END)
if __name__ == "__main__":
   main()

      