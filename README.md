# python_process_timeout_test
Testing Python 3's process timeout

Here is the expected output:
```
y start
y joins
x start
x done
p exitcode 0
y ends

z start
z joins
x start
p exitcode None
z ends
done
```

This shows that if a daemon=True subprocess is terminated with a timeout, its exitcode is None