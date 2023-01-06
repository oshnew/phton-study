import re

#참고
# 1) https://docs.aws.amazon.com/ko_kr/elasticloadbalancing/latest/application/load-balancer-access-logs.html
# 2) https://stackoverflow.com/questions/68875527/regex-for-python-based-logparser-for-printing-aws-elb-logs

fields = [ "type",
"time",
"elb",
"client_ip",
"client_port",
"target_ip",
"target_port",
"request_processing_time",
"target_processing_time",
"response_processing_time",
"elb_status_code",
"target_status_code",
"received_bytes",
"sent_bytes",
"request_type",
"request_url",
"request_protocol",
"user_agent_browser",
"ssl_cipher",
"ssl_protocol",
"target_group_arn",
"trace_id",
"domain_name",
"chosen_cert_arn",
"matched_rule_priority",
"request_creation_time",
"actions_executed",
"redirect_url",
"lambda_error_reason",
"target_port_list",
"target_status_code_list",
"classification",
"classification_reason" ]



field = str(input("what is the field needed? "))
regex = r'([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*):([0-9]*) ([^ ]*)[:-]([0-9]*) ([-.0-9]*) ([-.0-9]*) ([-.0-9]*) (|[-0-9]*) (-|[-0-9]*) ([-0-9]*) ([-0-9]*) \"([^ ]*) ([^ ]*) (- |[^ ]*)\" \"([^\"]*)\" ([A-Z0-9-]+) ([A-Za-z0-9.-]*) ([^ ]*) \"([^\"]*)\" \"([^\"]*)\" \"([^\"]*)\" ([-.0-9]*) ([^ ]*) \"([^\"]*)\" \"([^\"]*)\" \"([^ ]*)\" \"([^\s]+?)\" \"([^\s]+)\" \"([^ ]*)\" \"([^ ]*)\"'

def ParseLogFile(file):
    resultDict = {}

    with open(file, 'r') as log:
        line = log.readline()
        while line:
            line_split = re.split(regex, line)
            line_split = line_split[1:len(line_split) - 1]
            index = fields.index(field)
            val = line_split[index]
            resultDict.setdefault(val, 0)
            resultDict[val] += 1
            line = log.readline()
        return resultDict
if __name__ == '__main__':
    result=ParseLogFile("C:\\HOME\\2.log")
    print(result)