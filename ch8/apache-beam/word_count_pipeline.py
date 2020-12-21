#!/usr/bin/env python3

import apache_beam as beam
import argparse

def word_map(line, words):
   for word in words:
      if word in line:
         yield (word,1)

if __name__ == '__main__':
   parser = argparse.ArgumentParser(description='Find the most used word')
   parser.add_argument('--output_prefix', default='tmp/output', help='Output prefix')
   parser.add_argument('--input', default='Frankenstein.txt', help='Input file')
   parser.add_argument('--words', default='Frankenstein,Margaret', help='Comma-separated list of words to count')

   options, pipeline_args = parser.parse_known_args()
   p = beam.Pipeline(argv=pipeline_args)

   input = options.input 
   output_prefix = options.output_prefix
   words = options.words.split(',')

   # find most used packages
   (p
      | 'ReadFile' >> beam.io.ReadFromText(input)
      ## beam.FlatMap is equivalent to ParDo in Python
      | 'GetWords' >> beam.FlatMap(lambda line: word_map(line, words))
      | 'TotalUse' >> beam.CombinePerKey(sum)
      | 'write' >> beam.io.WriteToText(output_prefix)
   )

   p.run().wait_until_finish()
