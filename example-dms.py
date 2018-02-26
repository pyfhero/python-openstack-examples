import os
import time

from openstack import connection



# Please put the endpoints which are not the native OpenStack services.
_endpoints = {
    'OS_DMS_ENDPOINT_OVERRIDE': 'https://dms.eu-de.otc.t-systems.com:443/v1.0/%(project_id)s/',
    'OS_LOAD_BALANCER_ENDPOINT_OVERRIDE': 'https://elb.eu-de.otc.t-systems.com:443/v1.0/%(project_id)s',
    'OS_RDS_ENDPOINT_OVERRIDE': 'https://rds.eu-de.otc.t-systems.com:443/v1.0/%(project_id)s',
    'OS_SMN_ENDPOINT_OVERRIDE': 'https://smn.eu-de.otc.t-systems.com:443/v1.0/%(project_id)s'
}

_auth = {
    'auth_url': "https://iam.eu-de.otc.t-systems.com:443/v3",
    'project_id': 'YOUR-PROJECT-ID',
    'user_domain_id': 'YOUR-DOMAIN-ID',
    'username': 'YOUR-USER-NAME',
    'password': 'YOUR-PASSWORD'
}


def create_queue(conn, queue_name):
    queue_obj = None
    queues = conn.dms.queues()
    for each in queues:
        if 0 != cmp(each.name, queue_name):
            pass
        else:
            queue_obj = each
            break

    # create a new one
    if queue_obj is None:
        queue_param = {
            'name': queue_name,
            'description': 'This is a dms demo queue.'
        }
        queue_obj = conn.dms.create_queue(**queue_param)
    else:
        pass

    # for debug
    #print(queue_obj)
    return queue_obj


def create_groups(conn, queue):
    print("create groups on queue %s", queue)
    groups_new = ["dms-group-01"]

    # check if the new groups are already exist.
    groups = conn.dms.groups(queue)
    groups_exist = [grp.name for grp in groups]
    groups_add = list(set(groups_new) - set(groups_exist))
    if 0 < len(groups_add):
        grps_params = {"groups": [{"name": i} for i in groups_add ]}
        print(conn.dms.create_groups(queue, **grps_params))
    else:
        pass


def delete_groups(conn, queue):
    print("delete all groups on queue %s", queue)
    for g in conn.dms.groups(queue):
        print(g)
        conn.dms.delete_group(queue, g)


def produce_message(conn, queue):
    print("send message on a queue %s", queue)
    msg_dict = {
        "messages": [
            {
                "body": "TEST11",
                "attributes":
                    {
                        "attribute1": "value1",
                        "attribute2": "value2"
                    }
            }
        ]
    }

    msgs = conn.dms.send_messages(queue, **msg_dict)
    #print("send messages %s" % msgs)


def consume_message(conn, queue):
    grps = conn.dms.groups(queue)

    for grp in grps:
        print("=========consumed message by group %s start..." % grp.name)
        csm_msgs = conn.dms.consume_message(queue, grp.id)
        for cm in csm_msgs:
            print("*****ack consumed message %s" % cm)
            print(conn.dms.ack_consumed_message(cm))
        print("=========consumed message by group %s end." % grp.name)


def consume_message_with_tags(conn, qui, gid):
    """Consume message by tag list in queue and group"""
    #qid = '673f8fca-9aa1-4974-8fc5-b0eb1c5f9724'
    #gid = 'g-a826e437-2e67-46c7-b220-63836b5bb463'
    params = {
        'max_msgs': 10,
        'time_wait': 30,
        'tags': ['tag1', 'tag2'],
        'tag_type': 'or'
    }

    for c in conn.dms.consume_message(qui, gid, **params):
        print(c)


def get_quotas(conn):
    for q in conn.dms.quotas():
        print(q)


def main():
    # set the endpoints
    for edp_key in _endpoints:
        #print(edp_key, _endpoints[edp_key])
        os.environ.setdefault(edp_key, _endpoints[edp_key])

    # connect to OTC
    conn = connection.Connection(**_auth)

    queue_name = 'dms-demo-queue'
    queue_obj = create_queue(conn, queue_name)
    create_groups(conn, queue_obj)

    produce_message(conn, queue_obj)
    consume_message(conn, queue_obj)

    get_quotas(conn)


if __name__ == '__main__':
    main()



