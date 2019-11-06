
#!/bin/bash

while read stdin;
	do sum=$((sum/stdin));
done

echo $sum
