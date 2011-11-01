"""
Operations that the provisioner can do
"""
from celery.task import task, Task


class EPUService(Task):

    abstract = True

    def run(self, op=None, **kwargs):

        self.logger = self.get_logger()
        if not op:
            raise Exception("You EPUService expects an op")

        op_method = getattr(self, op)
        return op_method(**kwargs)

class Provisioner(EPUService):

    name = "provisioner"
    logger = None

    def __init__(self, *args, **kwargs):
        EPUService.__init__(self, *args, **kwargs)

        self.vms = []
        self.conf = self.app.conf.get("PROVISIONER_CONFIG")

    def start(self, **kwargs):
        self.logger.info("start!")
        self.data = kwargs.get('data')
        self.logger.info("conf: %s" % self.conf)

        return self.data

    def stop(self, **kwargs):
        """Stop provisioner service
        """
        return "stop"

    def provision(self, **kwargs):
        """Service operation: Provision a taskable resource
        """

        self.logger.info("original vms: %s" % self.vms)
        self.vms.append("avm")
        self.logger.info("provisioned vms: %s" % self.vms)

    def terminate_nodes(self, **kwargs):
        """Service operation: Terminate one or more nodes
        """
        pass

    def terminate_launches(self, **kwargs):
        """Service operation: Terminate one or more launches
        """
        pass

    def query(self, **kwargs):
        """Service operation: query IaaS  and send updates to subscribers.
        """
        return self.vms

    def terminate_all(self, **kwargs):
        """Service operation: terminate all running instances
        """
        pass

    def terminate_all_rpc(self, **kwargs):
        """Service operation: terminate all running instances if that has not been initiated yet.
        Return True if all running instances have been terminated.
        """
        pass

    def dump_state(self, **kwargs):
        """Service operation: (re)send state information to subscribers
        """
        pass

def get_cassandra_store(host, username, password, keyspace, port=None, prefix=""):
    store = CassandraProvisionerStore(host, port or 9160, username, password,
                                      keyspace, prefix)
    store.connect()
    return store

def get_provisioner_store(conf):
    cassandra_host = conf.getValue('cassandra_hostname')
    if cassandra_host:
        log.info("Using cassandra store. host: %s", cassandra_host)
        try:
            store = get_cassandra_store(cassandra_host,
                                        conf['cassandra_username'],
                                        conf['cassandra_password'],
                                        conf.getValue('cassandra_keyspace'),
                                        conf.getValue('cassandra_port'))
        except KeyError,e:
            raise KeyError("Provisioner config missing: " + str(e))
    else:
        log.info("Using in-memory Provisioner store")
        store = ProvisionerStore()
    return store

