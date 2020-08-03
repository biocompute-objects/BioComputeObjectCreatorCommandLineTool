#Pranav Mishra
#BioCompute Object Creator Minimum Viable Product
import os
import json
from json import JSONEncoder
from datetime import datetime

class BCO():
   def __init__(self, provenance, usability, description, execution, io, object_id, spec_version, etag = "new", parametric = None, error = None, extension = None):
       self.provenance = provenance
       self.usability = usability
       self.extension = extension
       self.description = description
       self.execution = execution
       self.parametric = parametric
       self.io = io
       self.error = error
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
   def __init__(self, filename, uri, sha1_checksum, access_time):
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
class script():
   def __init__(self, uri):
      self.uri = uri #NOT uri object ($ref)
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
# class input_subdomain:
#    def __init__(self, inputs):
#       self.inputs = inputs #NOT uri object ($ref)
class output_subdomain_item:
   def __init__(self, output, mediatype):
      self.output = output #NOT uri object ($ref)
      self.mediatype = mediatype #string
      
class error_domain():
   def __init__(self, empirical_error, algorithmic_error):
      self.empirical_error = empirical_error #object  
      self.algorithmic_error = algorithmic_error #object
class empirical_error():
   def __init__(self, description):
      self.description = description #string
class algorithmic_error():
   def __init__(self, description):  
      self.description = description #string

# class extension_domain():
#    def __init__(self, extension_schema):
#       self.extension_schema = extension_schema

class usability_domain():
   def __init__(self, use):
      self.use = use #string

class parametric_domain():
   def __init__(self, parameter):
       self.parameter= parameter #array
class parameter:
   def __init__(self, param, value, step):
      self.param = param #string 
      self.value = value #string 
      self.step = step #string 

def main():
   data = {}
   with open('blank_bco.json') as json_file: #testing 
      data = json.load(json_file)
      #print(data)
   #insert code below 
   
   #take output of script command
   #for finding steps, split by "|"    
   
   #metadata
   print("Welcome to the BioCompute Command Line Tool. With this tool, you can automate some parts of BCO creation and work on creating a BCO directly from the command line. \n If you make a mistake while creating your BCO, you can always edit that field in the output json file that represents your BCO.\n")
   input_filename = r'' + input("Enter name of desired input file (Output of script command/typescript): ")
   with open(input_filename, 'r') as file: 
      data = file.read()
   data = data[int(data.index("$")+1): int(data.index('\n'))]
   print("Pipeline: " + data)
   print("\n")
   confirmation = input("Confirm pipeline (y or n): ")
   if confirmation.lower() == "n":
      data = input("Enter the correct pipeline: ")
      
   pipeline = data.split("|")
   for x in range(0, len(pipeline)):
      pipeline[x] = pipeline[x].lstrip()
      pipeline[x] = pipeline[x].rstrip()
   
   output_filename = input("Enter name of desired output file (e.g. example_bco.json): ")
   
   print("Metadata information\n")
   
   object_id = input("Enter unique BCO Object ID (e.g. https://portal.aws.biochemistry.gwu.edu/bco/BCO_00026662). Ensure the id part ('00026662') is not in use : ")
   
   etag = "new" 
   etag_input = input("Enter etag value (default is 'new') For default, enter nothing.: ")
   if etag_input.strip() != etag.strip() and etag_input.strip() !=  "":
      etag = etag_input
      
   spec_version = "https://w3id.org/ieee/ieee-2791-schema/"
   spec_version_input = input("Enter version of specification for this IEEE-2791 object (BCO) (Default is: https://w3id.org/ieee/ieee-2791-schema/) For default, enter nothing.: ")
   if spec_version_input.strip() != spec_version.strip() and spec_version_input.strip() != "":
      spec_version = spec_version_input
   print("\n")
   
   #provenance
   print("Provenance Domain Information\n")
   name = input("Enter your name: ")
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
      contribution = input("Enter contribution type: ").strip()
      contributors.append(contributor(name = contributor_name, contribution = contribution))
      add_contributor = input("Add another contributor? y/n: ")
   provenance = provenance_domain(name = name, version = version, license = license, created = created, modified = modified, contributors = contributors)
   print("\n")   
   
   #usability
   print("Usability Domain Information \n")
   use = input("What is the purpose of this computational workflow/analysis?: ")
   usability = usability_domain(use)
   
   #execution 
   print("Execution Domain Information \n")
   print("Enter script uris in the following format: uri1 uri2 uri3 uri4 \n")
   scrpt = input("What is/are the uris for the script object used to perform computations?: ")
   scrpt = script(scrpt)
   script_driver = "shell"
   script_driver_input = input("Enter script driver, the type of executable to perform commands in script in order to run the pipeline (Default is shell) Enter nothing for default.: ")
   if script_driver_input.lower().strip() != script_driver.lower().strip() and script_driver_input.lower().strip() != "":
      script_driver = script_driver_input
   software_prerequisites = []
   add_software_prerequisite = "y"
   while(add_software_prerequisite.lower().strip() == "y"):
      sp_name = input("Enter software prerequisite name: ")
      sp_version = input("Enter software prerequisite version: ")
      sp_uri = input("Enter software prerequisite uri: ")
      software_prerequisites.append(software_prerequisite(version = sp_version, name = sp_name, uri = sp_uri))
      add_software_prerequisite = input("Add another software prerequisite? y/n: ")
   external_data_endpoints = []
   add_external_data_endpoints = "y"
   while(add_external_data_endpoints.strip().lower() == "y"):
      ede_name = input("Enter external data endpoint name: ")
      ede_url = input("Enter external data endpoint url: ")
      external_data_endpoints.append(external_data_endpoint(name = ede_name, url = ede_url))
      add_external_data_endpoints = input("Add another external data endpoint? y/n: ")
   add_environment_variable = "y"
   print("Enter environment variables in 'key value' format \n")
   environment_variables = []
   while(add_environment_variable.strip().lower() == "y"):
      key_value_pair = input("Enter environmental parameters that are useful to configure the execution environment on the target platform: ").lstrip().rstrip()
      try:
         env_variable = environment_variable(key_value_pair.split(" ")[0], key_value_pair.split(" ")[1])
         environment_variables.append(env_variable)
      except:
         print("There was an error with your input. Please try again.")
      add_environment_variable = input("Add another environment variable? y/n: ") 
   execution = execution_domain(environment_variables = environment_variables, script_driver = script_driver, software_prerequisites = software_prerequisites, external_data_endpoints = external_data_endpoints, script = scrpt)
   print("\n")
   
   #description
   print("Description Domain Information \n")
   print("Format to enter keywords in: 'keywordA keywordB keywordC keywordD'")
   keywords = input("Enter biology research keywords in the specified format to aid in search-ability and description of this object: ").lstrip().rstrip().split(" ")
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
      print("Enter input file uris in the following format: 'uri1 uri2 uri3 uri4'\n")
      input_list_temp = input("Enter input file uris if this step uses input files: ").lstrip().rstrip().split(" ")
      print("Enter output file uris in the following format: 'uri1 uri2 uri3 uri4'\n")
      output_list_temp = input("Enter output file uris if this step outputs to files: ").lstrip().rstrip().split(" ")
      pipeline_steps.append(pipeline_step(step_number=step_number, name=name, description=description, input_list= input_list_temp, output_list = output_list_temp))
      if step_number == 1:
         for x in input_list_temp:
            if x!= "":
               input_list_master.append(x)
      if step_number == len(pipeline):
         for x in output_list_temp:
            if x != "":
               output_list_master.append(x)
         
      step_number += 1  
   description = description_domain(keywords = keywords, pipeline_steps = pipeline_steps)
   print("\n")
   #IO 
   print("Input Output (IO) Domain Information \n")
   inputs = []
   for x in input_list_master:
       inputs.append(x)
         
   print("Current input list: ", ", ".join(inputs))
   add_input = input("Do you want to add additional input files? y/n: ")
   while(add_input.strip().lower() == "y"):
      input_file_uri = input("Enter input file uri: ")
      inputs.append(input_file_uri)
      add_input = input("Add an input file? y/n: ")
         
   print("Current output list: ", ", ".join(output_list_master))
   outputs = []
   for output in output_list_master: 
      print(output)
      output_mediatype = input("Enter output file mediatype for this output file: ")
      outputs.append(output_subdomain_item(output, output_mediatype))
   add_output = input("Do you want to add additional output files? y/n: ")
   while(add_output.strip().lower() == "y"):
      output = input("Enter output file uri: ")
      output_mediatype = input("Enter output file mediatype: ")
      outputs.append(output_subdomain_item(output, output_mediatype))
      add_output = input("Add an output file? y/n: ")
   io = io_domain(inputs, outputs) 
   print("\n")
   
   #from the orcid get the information (BONUS)
   
   output_bco = BCO(provenance = provenance, usability = usability, description = description, execution = execution, io = io, object_id = object_id, spec_version = spec_version, etag = etag)
   try:
      print(output_bco) 
   except:
      print("error occured with printing") 
   
   with open(output_filename, 'w') as json_output:
#       try: 
      json_string = BCOEncoder().encode(output_bco)
      json_output.write(json_string)
      json_output.close()
#       except:
         # print("error occured with outputting as a json file")
if __name__ == "__main__":
   main()

      