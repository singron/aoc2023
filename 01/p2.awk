#! /usr/bin/env -S awk -f
BEGIN {
	d["zero"]=0
	d["one"]=1
	d["two"]=2
	d["three"]=3
	d["four"]=4
	d["five"]=5
	d["six"]=6
	d["seven"]=7
	d["eight"]=8
	d["nine"]=9
}

function tonum(s) {
	if (match(s, /[0-9]/)) {
		return s + 0;
	}
	return d[s];
}

{
	match($0, /(zero|one|two|three|four|five|six|seven|eight|nine|[0-9])/, m);
	a = tonum(m[1]);
	match($0, /.*(zero|one|two|three|four|five|six|seven|eight|nine|[0-9]).*/, m);
	b = tonum(m[1]);
	t += 10*a + b;
}

END { print(t) }
