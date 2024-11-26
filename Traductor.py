from TraduceJavaListener import TraduceJavaListener
from TraduceJavaParser import *

class Traductor(TraduceJavaListener):
    def __init__(self):
        # Inicializa el código Java con la estructura básica de la clase y el método main
        self.java_code = "public class multi {\n\n"
        self.method_code = ""  # Aquí almacenaremos el código de las funciones/métodos
        self.main_content = "    public static void main(String[] args) {\n"
        self.indentation = "    "  # Identación base para el código de funciones
        self.function_calls = []  # Almacena las llamadas de función y sus argumentos

    def enterPrograma(self, ctx:TraduceJavaParser.ProgramaContext):
        print("Starting translation...")

    def exitPrograma(self, ctx:TraduceJavaParser.ProgramaContext):
       

        # Añade el contenido de main y de los métodos a la clase
        self.java_code += self.method_code  + "\n" + self.main_content
        self.java_code += "\n}\n"  # Cierra la clase
        print(self.java_code)  # Imprime el código Java generado
        # Abre (o crea) un archivo llamado "mi_archivo.txt" en modo de escritura
        with open("multi.java", "w") as archivo:
            # Escribe una cadena de texto en el archivo
            archivo.write(self.java_code)

    def enterFunction(self, ctx:TraduceJavaParser.FunctionContext):
        # Traduce la definición de función y la guarda en method_code en lugar de java_code
        func_name = ctx.ID().getText()
        params = ', '.join([f"int {param.getText()}" for param in ctx.parameters().ID()])
        self.method_code += f"    public static int {func_name}({params}) {{\n"

    def exitFunction(self, ctx:TraduceJavaParser.FunctionContext):
        # Cierra el cuerpo de la función y la añade a method_code
        self.method_code += "    }\n\n"

    def exitAssignment(self, ctx:TraduceJavaParser.AssignmentContext):
        # Traduce una asignación y la añade a method_code
        var_name = ctx.ID().getText()
        expression = ctx.expression().getText()
        self.method_code += f"{self.indentation}int {var_name} = {expression};\n"

    def exitReturn_statement(self, ctx:TraduceJavaParser.Return_statementContext):
        # Traduce una declaración de retorno y la añade a method_code
        return_expression = ctx.expression().getText()
        self.method_code += f"{self.indentation}return {return_expression};\n"

    def exitPrint_statement(self, ctx:TraduceJavaParser.Print_statementContext):
        # Cuando encontramos un `print`, almacenamos la llamada a la función en el main
        print_expression = ctx.expression().getText()
        self.main_content += f"        System.out.println({print_expression});\n    }}"

    def enterFunction_call(self, ctx:TraduceJavaParser.Function_callContext):
        # Almacena el nombre de la función y sus argumentos para ser usados en el main
        func_name = ctx.ID().getText()
        args = [arg.getText() for arg in ctx.arguments().expression()]
        # Asegura que los argumentos estén entre paréntesis y formateados correctamente
        self.function_calls.append((func_name, args))

    def exitFunction_call(self, ctx:TraduceJavaParser.Function_callContext):
        # No es necesario realizar ninguna acción adicional aquí, ya que los datos se almacenan en enterFunction_call
        pass
