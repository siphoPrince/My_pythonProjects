import cmd


class CalCu(cmd.Cmd):
    prompt = "$"

    def do_add(self, arg):
        try:
            num1, num2 = map(float, arg.split())
            result = num1 + num2
            print(f"Results: {result}")
        except ValueError:
            print("Invalid output, Please enter two args")

    def do_divide(self, args):
        try:
            num1, num2 = map(float, args.split())
            result = num1 / num2
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Invalid input, Please enter two args.")

    def do_subtract(self, args):
        try:
            num1, num2 = map(float, args.split())
            result = num1 - num2
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input, please enter two args")

    def do_multiply(self, args):
        try:
            num1, num2 = map(float,args.split())
            result = num1 * num2
            print(f"Result: {result}")
        except ValueError:
            print("Input Invalid, please enter two args.")

    def do_exit(self, args):
        print("exit program")
        return True


calc = CalCu()
calc.cmdloop()
