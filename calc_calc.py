import sympy as sy

class Problem:

    def __init__(self, expression):
        self._expression = expression
        self.parse_expression()
        
    def parse_expression(self):
        self._parsed_expression=sy.parse_expr(self._expression,evaluate=False)
        self._vars = [var in self._parsed_expression if not var.isnumeric()]
        self._saved = None
        
    def differentiate(self, respect_to = None,order=1,save=True):
        if respect_to is None:
            for var in self._parsed_expression.args:
                if not var.isnumeric():
                    respect_to == char
                    break
        if respect_to is None:
            return False
        equation = self._parsed_expression
        for times in order:
            answer = sy.diff(equation,respect_to)
            primes = "'" * times
            print(f"f{primes}(self._vars) = {answer}")
            equation = answer
        if saved:
            self._saved = answer

    def integrate_ind(self, respect_to=None,save=True):
        if respect_to is None:
            respect_to = self._vars[0]
        if respect_to is None:
            respect_to = sy.symbols("x")
        equation = self._parsed_expression
        answer = sy.integrate(equation,respect_to)
        print(f"s({self._vars)}) = {answer}")
        self._saved = equation
        
    def integrate_def(self,bounds, respect_to= None,save=True):
        lower_bound=bounds[0]
        upper_bound=bounds[1]
        if respect_to is None:
            respect_to = self._vars[0]
        if respect_to is None:
            respect_to = sy.symbols("x")
        equation = sy.integrate(equation,(respect_to,lower_bound,upper_bound))
        result = sy.doit(equation)
        self._saved = equation
        print(f"The definite itegral from {lower_bound} to {upper_bound} is: {equation}")
        print(f"This evaluates to: {result}")
        return result
