#!/usr/bin/env python

# Copyright (C) <2015> EMBL-European Bioinformatics Institute

# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# Neither the institution name nor the name jupyter_example_pipeline can
# be used to endorse or promote products derived from this
# software without prior written permission. For written
# permission, please contact <marco@ebi.ac.uk>.

# Products derived from this software may not be called
# jupyter_example_pipeline nor may jupyter_example_pipeline appear in their names
# without prior written permission of the developers.
# You should have received a copy of the GNU General Public
# License along with this program. If not, see
# <http://www.gnu.org/licenses/>.

__author__ = "Marco Galardini"
__version__ = "0.0.1"

def get_options():
    import argparse

    # create the top-level parser
    description = "Extract protein sequences info from a gbk file"
    parser = argparse.ArgumentParser(description = description,
                                     prog = 'get_genes')
    parser.add_argument('gbk', action='store',
                        help='Input GenBank file')
    
    parser.add_argument('--version', action='version',
                         version='%(prog)s '+__version__)

    return parser.parse_args()

if __name__ == "__main__":
    from Bio import SeqIO
    options = get_options()

    for s in SeqIO.parse(options.gbk, 'genbank'):
        for f in filter(lambda x: x.type == 'CDS' and 'pseudo' not in x.qualifiers,
                s.features):
            name = f.qualifiers['locus_tag'][0]
            print('\t'.join( (s.id, name, str(f.strand),
                              str(int(f.location.end) - int(f.location.start))) ))    
