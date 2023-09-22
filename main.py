def arg_info_decorator(*decorator_args, **decorator_kwargs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            args_info = {}
            for i, arg in enumerate(args):
                arg_name = func.__code__.co_varnames[i]
                arg_type = type(arg).__name__
                args_info[arg_name] = arg
                args_info[arg_type] = arg
            return func(args_info=args_info, *args, **kwargs)

        return wrapper

    return decorator


@arg_info_decorator(arg1="value1", arg2="value2")
def example_function(a, b, c, args_info=None):
    print("Arguments:", a, b, c)
    return {"args_info": args_info}


result = example_function(42, "hello", 3.14)
print("Arguments Info:", result['args_info'])
