from antlr4 import *
from TraduceJavaLexer import TraduceJavaLexer
from TraduceJavaParser import TraduceJavaParser
from TraduceJavaListener import TraduceJavaListener
from Traductor import Traductor
def main():
    in_code = ("pyToJava.txt")
    fileopen= open(in_code)
    lexer = TraduceJavaLexer(InputStream(fileopen.read()))
    stream = CommonTokenStream(lexer)
    parser = TraduceJavaParser(stream)
    tree = parser.programa()
    walker = ParseTreeWalker()
    walker.walk(Traductor(),tree)
    

    
    

      
    
if __name__=='__main__':
    main()