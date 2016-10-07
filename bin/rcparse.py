#!/usr/bin/env python


from redcap_parser import parse as pa


from optparse import OptionParser
import os.path




if __name__ == '__main__':


    parser = OptionParser()

    (options, args) = parser.parse_args()

    if len(args) == 1:
        filename = str(args[0])

        if os.path.isfile(filename):

            if filename.endswith('.csv'):

                    print '=' * (len(filename)+2)
                    print ' ', filename, ' '
                    print '=' * (len(filename)+2)
                    pa.parse(filename)

            else:

                print '[Error] : filename should end with .csv'


        else:

            print '[Error] : path to ', filename, ' does not exist!'



    else:

        print '[Error]: parser only takes one file.csv as input'
