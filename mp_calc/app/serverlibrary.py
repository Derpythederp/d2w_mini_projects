def _merge(array, start, end_left, end_right, key):
    # Make copies of left and right to copy from, +1 since exclusive
    left_arr = array[start:end_left+1]
    right_arr = array[end_left+1:end_right+1]

    i = 0
    j = 0
    k = start  # k is the current idx in original array
    
    left_len = len(left_arr)
    right_len =  len(right_arr)

    if key is None:
        key = lambda i: i

    # Sort array based on left or right
    while (i < left_len) and (j < right_len):
        if key(left_arr[i]) <= key(right_arr[j]):  # <= to pass assert 2
            array[k] = left_arr[i]
            i += 1
        else:
            array[k] = right_arr[j]
            j += 1
        k += 1
    
    # Copy excess no. in left or right array
    while (i < left_len):
        array[k] = left_arr[i]
        i += 1
        k += 1

    while (j < right_len):
        array[k] = right_arr[j]
        j += 1
        k += 1

def _mergesort(array, start, end, byfunc=None):
    if end != start:
        mid = ((end-start) // 2) + start
        _mergesort(array, start, mid, byfunc)
        _mergesort(array, mid+1, end, byfunc)
        _merge(array, start, mid, end, byfunc)
    
def mergesort(array, byfunc=None):
    """
    Merge sorts the array in place.
    Parameters
    ----------
    array : List
        array containing value to be sorted
    byfunc: Function, default=None
        function/callable which indicates the key to sort by
    Returns
    -------
    None
    """
    if len(array) > 1:
        _mergesort(array, 0, len(array)-1, byfunc)  


class Stack:
    def __init__(self, array=[]):
        self.__stack = array  # bottom is 0, top is len(self.__stack)
        
    def push(self, item):
        return self.__stack.append(item)
        
    def pop(self):
        return self.__stack.pop(len(self) - 1)
        
    def peek(self):
        if not self.isEmpty:
            return self.__stack[0]
    
    def __len__(self):
        return len(self.__stack)
    
    def __iter__(self):
        for i in range(len(self) - 1, -1, -1):
            yield self.__stack[i]
    
    @property
    def isEmpty(self):
        return len(self) == 0


class EvaluateExpression:
    valid_char = '0123456789+-*/() '
    valid_char_set = set(valid_char)
    valid_operator = '+-*/()'
    
    def __init__(self, string=""):
        self.expression = string
            
    @property
    def expression(self):
        return self.expr

    @expression.setter
    def expression(self, new_expr):
        if set(new_expr).issubset(EvaluateExpression.valid_char_set) and len(new_expr) != 0:
            self.expr = new_expr
        else:
            self.expr = ""

    def insert_space(self):
        result = self.expression
        for operator in EvaluateExpression.valid_operator:
            result = result.replace(operator, " " + operator + " ")
        return result
    
    
    def __perform_operation(self, operand1, operand2, operator):
        if operator == "*":
            return operand1 * operand2
        
        if operator == "/":
            return operand2 // operand1
        
        if operator == "+":
            return operand1 + operand2
        
        if operator == "-":
            return (operand2 - operand1)


    def process_operator(self, operand_stack, operator_stack):
        if not(operand_stack.isEmpty) and not(operator_stack.isEmpty):
            operator = operator_stack.pop()
            operand1 = operand_stack.pop()
            operand2 = operand_stack.pop()
            result = self.__perform_operation(operand1, operand2, operator)
            operand_stack.push(result)

    def evaluate(self):
        operand_stack = Stack([])
        operator_stack = Stack([])
        expression = self.insert_space()
        tokens = expression.split()

        for token in tokens:      
            if token.isdigit():
                operand_stack.push(int(token))
            
            if token == "(":
                operator_stack.push(token)

            # ) symbol, repeatedly process the operators from the top of operator_stack until seeing the ( symbol on the top of the stack.
            if token == ")":
                operator = operator_stack.pop()
                while operator != "(":
                    operand1 = operand_stack.pop()
                    operand2 = operand_stack.pop()
                    result = self.__perform_operation(operand1, operand2, operator)
                    operand_stack.push(result)
                    operator = operator_stack.pop()
            
            if token in "+-*/":
                # 5 cases (assuming there is other operators in the stack): 
                # 1) next_operator --> +- and token --> */
                # 2) next_operator --> */ and token --> +-
                # 3) next_operator --> +- and token --> +-
                # 4) next_operator --> */ and token --> */
                # 5) next_operator --> ( 
                # Cases 3 and 4 means both operations have equal precedence under BODMAS
                # Cases 1 and 2 means that */ has to be done first then can push token onto operand
                # In other words, cases 2, 3, 4 has to be done first... since top thing on operator stack has highest precedence

                while not (operator_stack.isEmpty):
                    next_operator = operator_stack.pop()  
                    operator_stack.push(next_operator)  # return operator after checking
                    if (next_operator in "+-" and token in "*/") or next_operator == "(":  # case 1, top operator lower precedence than new operator token and case 5
                        break
                    # otherwise, case 2, 3 and 4
                    self.process_operator(operand_stack, operator_stack)
                    
                operator_stack.push(token)

        # Phase 2: Repeatedly process the operators from the top of operator_stack until operator_stack is empty.
        # Phase 2 kicks in only when we have non-bracked operations, so we can just evaluate all the way
        while not operator_stack.isEmpty:
            self.process_operator(operand_stack, operator_stack)
        
        return operand_stack.pop()


def get_smallest_three(challenge):
    records = challenge.records
    times = [r for r in records]
    mergesort(times, lambda x: x.elapsed_time)
    return times[:3]





