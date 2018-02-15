import argparse

parser = argparse.ArgumentParser(description='sniff the local network with ARP.')

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers ')
                    
parser.add_argument('--max', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='max the integers ')
                    
                    
parser.add_argument('--min', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='min the integers ')
                    
                    
parser.add_argument('--reverse', dest='types', action='store_const',
                    const=sum, default=max,
                    help='reverse the integers ')    
                    
parser.add_argument('--save', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='save the integers to file( file)' )
                    

parser.add_argument('--print', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='print the integers' ) 
                    
parser.add_argument('--add', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sdd one integers to the integers')                                         
                                                                            

parser.add_argument('bar', type=file)
                    

args = parser.parse_args()
print args.accumulate(args.integers)
