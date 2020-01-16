# import yaml


# def load_yaml(path):
#     with open(path, "r") as stream:
#         return yaml.safe_load(stream)


# def detector(name, rules, scope, exclude=None):
#     config = load_yaml("test.yaml")
#     # for config in rules:
#     trigger_threshold = rules.get('threshold')
#     clear_threshold = rules.get('clear_threshold')
#     trigger_duration = rules.get('duration')
#     clear_duration = rules.get('clear_duration')
#     detector_name = rules.get('name')

#     # print(
#     #     "{Trigger: ", trigger_threshold,  ", "
#     #     "Clear Trigger: ", clear_threshold,  ", "
#     #     "Trigger Duration: ", trigger_duration,  ", "
#     #     "Clear Duration: ", clear_duration,  ", "
#     #     "Name: ",  detector_name , "}"
#     # )
#     # cpu = data('CPUUtilization', filter=scope and (filter('namespace', 'AWS/EC2') and filter('stat', 'mean') and filter('InstanceId', '*') and filter('aws_instance_type', '*')) and not exclude).publish(label='cpu', enable=False)
#     # detect(when(cpu >= trigger_threshold, lasting='trigger_duration'), when(cpu < clear_threshold, lasting='clear_duration' or 'trigger_duration')).publish(name + 'detector_name')

#     print(f"cpu = data('CPUUtilization', "
#             f"filter={scope} and (filter('namespace', 'AWS/EC2') and filter('stat', 'mean')"
#             f" and filter('InstanceId', '*') and filter('aws_instance_type', '*')) and not {exclude})."
#             f"publish(label='cpu', enable=False)")
#     print(f"detect(when(cpu >= {trigger_threshold}, lasting='{trigger_duration}'),"
#             f" when(cpu < {clear_threshold}, lasting='{'clear_duration'} "
#             f"or '{trigger_duration}')).publish(name + '{detector_name}')\n")


# # This definition can be created via the combination of different outputs.
# #default = spec file or the organization file
# # rules = spec file or the organization file
# # scope = organization file (config_file)
# # exclude = spec file or the organization file
# definitions = [
#     (
#         "default",
#         {'name': '95% CPU usage for last 5m', 'threshold': 95, 'duration': '5m', 'clear_threshold': 90, 'clear_duration': '5m', 'severity': 'Critical'},
#         "filter('aws_tag_project', 'MonQa')",
#         "filter('InstanceId', 'i-1234567')",
#     ),
#     (
#         "override1",
#         {'name': '100% CPU usage over last 5m', 'threshold': 100, 'duration': '5m', 'severity': 'Critical'},
#         "filter('aws_tag_project', 'MonQa') and filter('InstanceId', 'i-1234567')",
#     ),
# ]

# [detector(*x) for x in definitions]


def detector(name, rules, scope, exclude=None):
    trigger_threshold = rules["threshold", None]
    clear_threshold = rules["clear_threshold", None]
    trigger_duration = rules["duration", None]
    clear_duration = rules["clear_duration", None]
    detector_name = rules["name", None]

    print(
        f"cpu = data('CPUUtilization', "
        f"filter={scope} and (filter('namespace', 'AWS/EC2') and filter('stat', 'mean')"
        f" and filter('InstanceId', '*') and filter('aws_instance_type', '*')) and not {exclude})."
        f"publish(label='cpu', enable=False)"
    )
    print(
        f"detect(when(cpu >= {trigger_threshold}, lasting='{trigger_duration}'),"
        f" when(cpu < {clear_threshold}, lasting='{'clear_duration'} "
        f"or '{trigger_duration}')).publish(name + '{detector_name}')\n"
    )


#    cpu = data('CPUUtilization', filter=scope and (filter('namespace', 'AWS/EC2') and filter('stat', 'mean') and filter('InstanceId', '*') and filter('aws_instance_type', '*')) and not exclude).publish(label='cpu', enable=False)
#     detect(when(cpu >= trigger_threshold, lasting=trigger_duration), when(cpu < clear_threshold, lasting=clear_duration or trigger_duration)).publish(name + 'detector_name')


def map_rule(i):
    return {
        "name": i[0],
        "threshold": i[1],
        "trigger_duration": i[2],
        "clear_threshold": i[3],
        "clear_duration": i[4],
        "severity": i[5],
    }


definitions = [
    (
        "default",
        map_rule(("95% CPU usage for last 5m", 95, "5m", 90, "5m", "Critical")),
        "filter('aws_tag_project', 'MonQa')",
        "filter('InstanceId', 'i-1234567')",
    ),
    (
        "override1",
        map_rule(("100% CPU usage over last 5m", 100, "5m", 100, "5m", "Critical")),
        "filter('aws_tag_project', 'MonQa') and filter('InstanceId', 'i-1234567')",
    ),
]

[detector(*x) for x in definitions]
