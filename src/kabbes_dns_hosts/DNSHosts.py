from parent_class import ParentClass

class DNSHosts:
    def __init__( self ):
        ParentClass.__init__( self )


    def run( self ):

        self.mapping = self.cfg['mapping.Path'].read()
        print (self.mapping)
        self.cfg.print_atts()

        self.hosts = self.cfg['hosts.Path'].read()

        self.print_hosts()

        if self.cfg['mode'] == 'add':
            self.add()
        if self.cfg['mode'] == 'remove':
            self.remove()

        self.print_hosts()

    def print_hosts( self ):

        print ('HOSTS: ')
        print (self.hosts)
        print ()

    def add( self ):

        print ('ADDING MAPPING')

        if self.mapping not in self.hosts:
            self.hosts += self.mapping

        self.cfg['hosts.Path'].write( string = self.hosts )

    def remove( self ):

        print ('REMOVING MAPPING')

        self.hosts = self.hosts.replace( self.mapping, '' )
        self.cfg['hosts.Path'].write( string = self.hosts )
