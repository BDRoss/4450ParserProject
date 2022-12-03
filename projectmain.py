from antlr4 import *
from projectLexer import projectLexer
from projectListener import projectListener
from projectParser import projectParser
import sys


class ProjectPrintListener(projectListener):
	def enterStart(self, ctx):
		print("Project: %s" % ctx.start)
		
def main():

# From Antlr's GitHub documentation
	inFile = FileStream(sys.argv[1])


	lexer = projectLexer(inFile)
	stream = CommonTokenStream(lexer)
	parser = projectParser(stream)
	tree = parser.start()
	printer = ProjectPrintListener()
	walker = ParseTreeWalker()
	walker.walk(printer, tree)
	#Reconsider in the future
	print(tree.toStringTree(recog=parser))

	
	
if __name__ == '__main__':
	main()