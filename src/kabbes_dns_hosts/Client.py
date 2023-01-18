import kabbes_dns_hosts
import kabbes_client
import py_starter as ps

class Client( kabbes_dns_hosts.DNSHosts ):

    _BASE_DICT = {
        "_src_Dir": kabbes_dns_hosts._src_Dir,
        "_repo_Dir": kabbes_dns_hosts._repo_Dir
    }

    def __init__( self, dict={} ):

        d = {}
        d.update( Client._BASE_DICT )
        d.update( dict )

        self.Package = kabbes_client.Package( kabbes_dns_hosts._Dir, dict=d )
        self.cfg = self.Package.cfg

        kabbes_dns_hosts.DNSHosts.__init__( self )
