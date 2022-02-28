"""
Filename: data_manager.py

Authors:
    Minseung Kim - msgkim@ucdavis.edu
    Jason Youn - jyoun@ucdavis.edu

Description:
    Python class to manage the dataset.

To-do:
"""
# standard imports
import logging as log
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), './'))

# third party imports
import pandas as pd
import xml.etree.ElementTree as ET

# local imports
from utilities import get_pd_of_statement

"""
class DataManager:
    """
 #   Class for managing the data.
 
    
   # def __init__(self, data_paths, map_file=None, data_rule_file=None, replace_rule_file=None):
  
"""        Class constructor for DataManager. All inputs are optional
        since only name mapping may be used somewhere else.

        Inputs:
            data_paths: (str) Filepath containing data sources.
            map_file: (str, optional) Filepath of name mapping table.
            data_rule_file: (str, optional) Filepath for knowledge inferral.
            replace_rule_file: (str, optional) Filepath for any replacements.
       
       self.data_paths = data_paths
        self.map_file = map_file
        self.data_rule_file = data_rule_file
        self.replace_rule_file = replace_rule_file

    def integrate(self):
       
       Integrate data from multiple sources.

        Returns:
            pd_integrated: (pd.DataFrame) Integrated data.
        
        list_integrated = []
        pd_data_paths = pd.read_csv(self.data_paths, sep='\t')

        # iterate over each dataset and perform name mappipng
        for _, row in pd_data_paths.iterrows():
            source = row['Source']
            path = row['Path']

            log.info('Processing source %s using %s', source, path)
            pd_data = pd.read_csv(path, '\t')

            # drop missing values if there's any
            before = pd_data.shape[0]
            pd_data = pd_data.dropna()
            after = pd_data.shape[0]

            if (before - after) > 0:
                log.warning('Dropping %d missing values.', (before - after))

            log.info('Applying name mapping to data from source %s', source)

            # pd_data = self.name_map_data(pd_data)
            pd_data['Source'] = source
            list_integrated.append(pd_data)

            log.info('Added %d triplets from source %s', pd_data.shape[0], source)

        # concatenate data
        pd_integrated = pd.concat(list_integrated, sort=True)
        log.info('Total of %d triplets integrated.', pd_integrated.shape[0])

        return pd_integrated.reset_index(drop=True)

    def map_name(self, pd_data):
    
        Perform name mapping given data from single source.

        Inputs:
            pd_data: (pd.DataFrame) Data that needs name mapping.

        Returns:
            pd_mapped: (pd.DataFrame) Name mapped data.
     
       if not self.map_file:
            log.info('Mapping file not specified. Skipping name mapping...')
            return pd_data

 
        log.info('Applyg name mapping table...')
"""
        # open name mapping file
        #with open(self.map_file) as file:
         #   next(file)  # skip the header
          #  map_file_content = file.readlines()

        # store dictionary of the name mapping information
        #dict_map = {}
        #for map_line in map_file_content:
         #   key, value = map_line.strip('\n').split('\t')
          #  dict_map[key] = value
           

        #def has_mapping_name(row, dict_map):
         #   row_copy = row.copy()
          #  values = dict_map.values()

            # return original if both subject and object are already using correct name
           # if (row['Subject'] in values) and (row['Object'] in values):
            #    return row

            #if (row['Subject'] in dict_map) and (row['Subject'] not in values):
             #   row_copy['Subject'] = dict_map[row['Subject']]

            #if (row['Object'] in dict_map) and (row['Object'] not in values):
             #   row_copy['Object'] = dict_map[row['Object']]

           # return row_copy

        #pd_mapped = pd_data.apply(has_mapping_name, axis=1, args=(dict_map, ))

        #return pd_mapped
def infer(self, pd_data):
        """
        Apply data rule and infer new data.

        Inputs:
            pd_data: (pd.DataFrame) Data to infer new knowledge from.

        Returns:
            pd_updated: (pd.DataFrame) Data with new inferred data added.
        """
if not self.data_rule_file:
    log.info('Data rule file not specified. Skipping knowledge inferral...')
return pd_data

    data_rules = ET.parse(self.data_rule_file).getroot()
    pd_updated = pd_data.copy()

    log.info('Applying data rule to infer new data using %s', self.data_rule_file)

    
