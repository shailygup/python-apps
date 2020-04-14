""" Get resources for services described in organization """

# Get all the services from the config file 

import yaml, json, boto3, click, os
from botocore.exceptions import UnknownServiceError
from os import path
import logging
import coloredlogs

logger = logging.getLogger(__name__)

# coloredlogs.install(level='INFO')


logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
logging.basicConfig(level=logging.ERROR)

coloredlogs.install(level='INFO', logger=logger)


def load_yaml(path):
    """ Load YAML file """
    with open(path, "r") as stream:
        return yaml.safe_load(stream)


def get_service_info(config):
    """ Get the service name and it's scope """
    temp_dict = {}

    for key, value in config['services'].items():
        service = key
        scope = value['scope']       
        temp_dict.update({service: scope})

    print(temp_dict)
    return temp_dict


def get_tag_data(service, tags, client, new_dir):
    """ Get tagged data """

    tag_dict = {}
    data = {}

    if tags:
        for tag in tags:
            for key, value in tag.items():
                # if "aws_" in key:
                key_without_aws = key.replace('aws_', '')

                if "tag" in key_without_aws:
                    tag_key = key_without_aws.replace("tag_", "")

                    tag_dict = {
                            'Key': f"{tag_key}",
                            'Values': [f"{value}"]
                        }

                    tag_response = client.get_resources(
                        TagFilters=[tag_dict], 
                        TagsPerPage=100,
                    )

                    for v in tag_response['ResourceTagMappingList']:
                        data = {v['ResourceARN']: v['Tags']}
                        with open(f"{new_dir}/{service}.json", "a+") as outfile:
                            json.dump(data, outfile, indent=4)


def catch_all(services, tags, client, new_dir):
    """ Catch all data """

    counter = 0
    values = []
    temp_dict = {}
    # print(services, tags)
    while counter < len(tags):
        
        if tags[counter]:
            for tag in tags[counter]:
                for k,v in tag.items():
                    values.append(v)
            # print(any("MonQA" in tag for tag in tags[counter]))
        
        counter += 1
        
    for s, t in services.items():

        if t is None:
            # Get all keys in an account
            get_all_keys = client.get_tag_keys()

            for key in get_all_keys['TagKeys']:
                # Get all the values for each of the keys
                get_all_values = client.get_tag_values(
                        Key=key
                    )

                for value in values:
                    if value in get_all_values['TagValues']:
                        get_all_values['TagValues'].remove(value)

                if ("cloudformation" not in key and 
                    "Git_Commit" not in key and 
                    "ImageTag" not in key and 
                    "kubernetes.io" not in key and
                    "Source_AMI_ID" not in key):

                    temp_dict = {
                            "Key": key,
                            "Values": get_all_values['TagValues']
                        }
                # print(temp_dict)

                    tag_response = client.get_resources(
                                    TagFilters=[temp_dict], 
                                    TagsPerPage=100,
                                )

                    for v in tag_response['ResourceTagMappingList']:
                        data = {v['ResourceARN']: v['Tags']}
                        with open(f"{new_dir}/{s}.json", "a+") as outfile:
                            json.dump(data, outfile, indent=4)


# def get_value(tags):
#     l = []
#     if tags is not None:
#         for tag in tags:
#             for key, value in tag.items():
#                 return value


# def catch_all_data(service, tags, client, new_dir):
#     """ Get the remaining keys and values for each tag """

#     used_tags = get_value(tags)

#     if used_tags:
#         get_all_keys = client.get_tag_keys()

#         for aws_key in get_all_keys['TagKeys']:
#             get_all_values = client.get_tag_values(
#                 Key=aws_key
#             )
#             if used_tags in get_all_values['TagValues']:
#                 new_list = get_all_values['TagValues'].remove(used_tags)
#                 print(aws_key, new_list)
            # return

            
            # get_all_keys = client.get_tag_keys()
            # # get_all_values = client.get_tag_values()
            # # all_keys = get_all_keys['TagKeys']
            
            # for aws_key in get_all_keys['TagKeys']:
            #     # print(item)
            #     get_all_values = client.get_tag_values(
            #         Key=aws_key
            #     )
            #     # key_value = {}'
            #     # print(key, get_all_values['TagValues'])
            #     if value in get_all_values['TagValues']:
            #         get_all_values['TagValues'].remove(value)
            #         print(aws_key, get_all_values['TagValues'])


@click.command()
@click.argument("config_file", type=click.Path(exists=True))
def cli(config_file=None):

    client = boto3.client('resourcegroupstaggingapi')
    service_list = []
    tag_list = []

    try:
        if(os.environ['AWS_PROFILE']):
            config = load_yaml(config_file)
            services = get_service_info(config)

            current_working_directory = os.getcwd()
            new_dir = "outputs"
            logging.info(f"Creating a directory called {new_dir} in {current_working_directory}")

            try:
                if path.exists(new_dir):
                    pass
                else:
                    os.mkdir(new_dir)
            except OSError:
                logging.error(f"Creation of the directory {new_dir} failed")

            for service, tags in services.items():
                get_tag_data(service, tags, client, new_dir)
                tag_list.append(tags)
                service_list.append(service)

            # if tags:
            #     for tag in tags:
            #         values = [value for key, value in tag.items()]
            #     print(values)
            catch_all(services, tag_list, client, new_dir)

    except KeyError as error:
        logging.error(f"The variable {error} isn't set")
        logging.error("Please switchrole into the appropriate AWS account")
    except Exception as exception:
        raise exception


if __name__ == "__main__":
    cli()
