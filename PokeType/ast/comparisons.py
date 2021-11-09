from rply.token import BaseBox

class CompareOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        out = self.eval_op()
        if out:
            return "true"
        else:
            return "false"

    def eval_op(self) -> bool:
        return False

class Greater(CompareOp):
    def eval_op(self):
        return self.left.eval() > self.right.eval()

class Lesser(CompareOp):
    def eval_op(self):
        return self.left.eval() < self.right.eval()

class Equal(CompareOp):
    def eval_op(self):
        return self.left.eval() == self.right.eval()

class NotEqual(CompareOp):
    def eval_op(self):
        return self.left.eval() != self.right.eval()

class LessThanEqual(CompareOp):
    def eval_op(self):
        return self.left.eval() <= self.right.eval()

class GreaterThanEqual(CompareOp):
    def eval_op(self):
        return self.left.eval() >= self.right.eval()