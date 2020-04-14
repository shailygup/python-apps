:construction: - Work in Progress

# Service Resources - helper script

This solution allows quick discovery of all the resources that are part of a SignalFx Service 

## Getting Started

These instructions will get you started for using this tool

### Setup

1. Install the pre-requisites/runtime requisites: `pip install -r requirements.txt`
2. Ensure your environment is running Python 3 or higher

### Running the tool

1. Switch role into the AWS account using either `roller`, `cr-switchrole` or `switchy`. This tool was built using `cr-switchrole`(https://github.com/cloudreach-coreops/cr-ops-scripts/blob/develop/cr-switchrole)
2. Ensure the correct region is set, this tool runs on the specified region only
3. Run it using `python service-resource.py </alerting_config/signalfx/organisations/your_config_file.yaml>

## Understanding the Ouput

1. A directory called `outputs` will be created upon a successful run of the tool, this is located in the current working directory
2. In the directory a json file will be created for each service. This file consists of the ARN and associated tags of the resources that would/are added to the SignalFx service. 

## Built With
* [Python](https://docs.python.org/3/)
* [Boto3](https://aws.amazon.com/sdk-for-python/)

## Contributing

Contributions are obviously welcome. Before starting any work, please do the following:

1. Search for relevant existing issues.
2. Open an issue (or check for an update on existing ones) detailing what you would like to do and why.
3. Discuss with the maintainers whether that is in scope for this project or not and how should it be done.
4. Start work and open a pull request when you get to a point that you require feedback.

Only functionality that is reasonably covered by tests will be merged.
