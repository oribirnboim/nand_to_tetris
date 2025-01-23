"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing


class SymbolTable:
    """A symbol table that associates names with information needed for Jack
    compilation: type, kind and running index. The symbol table has two nested
    scopes (class/subroutine).
    """

    def __init__(self) -> None:
        """Creates a new empty symbol table."""
        # Your code goes here!
        self.class_table = []
        self.subroutine_table = []
        self.types = []

    def start_subroutine(self,class_name= None) -> None:
        """Starts a new subroutine scope (i.e., resets the subroutine's 
        symbol table).
        """
        # Your code goes here!
        if class_name:
            self.subroutine_table = [['this', class_name, "ARG", 0]]   
        else:
            self.subroutine_table = []

    def define(self, name: str, type: str, kind: str) -> None:
        """Defines a new identifier of a given name, type and kind and assigns 
        it a running index. "STATIC" and "FIELD" identifiers have a class scope, 
        while "ARG" and "VAR" identifiers have a subroutine scope.

        Args:
            name (str): the name of the new identifier.
            type (str): the type of the new identifier.
            kind (str): the kind of the new identifier, can be:
            "STATIC", "FIELD", "ARG", "VAR".
        """
        # Your code goes here!
        identifier_table_row = [name, type, kind, self.var_count(kind)]
        if kind in {"STATIC", "FIELD"}:
            self.class_table.append(identifier_table_row)
        elif kind in {"ARG", "VAR"}:
            self.subroutine_table.append(identifier_table_row)
        else:
            raise SyntaxError("kind can only be ARG, FIELD, STATIC, VAR.")

    def var_count(self, kind: str) -> int:
        """
        Args:
            kind (str): can be "STATIC", "FIELD", "ARG", "VAR".

        Returns:
            int: the number of variables of the given kind already defined in 
            the current scope.
        """
        # Your code goes here!
        occurences = 0
        is_in_subroutine = False
        for var in self.subroutine_table:
            if var[2] == kind:
                occurences += 1
                is_in_subroutine = True
        if is_in_subroutine: return occurences
        for var in self.class_table:
            if var[2] == kind:
                occurences += 1
        return occurences 


    def kind_of(self, name: str) -> str:
        """
        Args:
            name (str): name of an identifier.

        Returns:
            str: the kind of the named identifier in the current scope, or None
            if the identifier is unknown in the current scope.
        """
        # Your code goes here!
        for var in self.subroutine_table:
            if var[0] == name:
                return var[2] # var kind
        for var in self.class_table:
            if var[0] == name:
                return var[2] # var kind
        return None

    def type_of(self, name: str) -> str:
        """
        Args:
            name (str):  name of an identifier.

        Returns:
            str: the type of the named identifier in the current scope.
        """
        # Your code goes here!
        for var in self.subroutine_table:
            if var[0] == name:
                return var[1] # var type
        for var in self.class_table:
            if var[0] == name:
                return var[1] # var type
        return None

    def index_of(self, name: str) -> int:
        """
        Args:
            name (str):  name of an identifier.

        Returns:
            int: the index assigned to the named identifier.
        """
        # Your code goes here!
        for var in self.subroutine_table:
            if var[0] == name:
                return var[3] # var index
        for var in self.class_table:
            if var[0] == name:
                return var[3] # var index
        return None
