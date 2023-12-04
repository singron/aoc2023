#! /usr/bin/env -S awk -f

{
	match($0, /[^0-9]*([0-9]).*/, m);
	a = m[1];
	match($0, /.*([0-9])[^0-9]*/, m);
	b = m[1];
	t += 10*a + b;
}

END { print(t) }
