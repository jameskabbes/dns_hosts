import kabbes_dns_hosts
import kabbes_user_client
import py_starter as ps

class Client( kabbes_dns_hosts.DNSHosts ):

    BASE_CONFIG_DICT = {
        "_Dir": kabbes_dns_hosts._Dir,
        "_src_Dir": kabbes_dns_hosts._src_Dir,
        "_repo_Dir": kabbes_dns_hosts._repo_Dir
    }

    def __init__( self, dict={}, **kwargs ):

        dict = ps.merge_dicts( Client.BASE_CONFIG_DICT, dict )
        self.cfg = kabbes_user_client.Client( dict=dict, **kwargs ).cfg
        kabbes_dns_hosts.DNSHosts.__init__( self )
