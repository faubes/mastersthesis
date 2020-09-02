package main

import (
"fmt"
"os"
)


func main() {

	if len(os.Args) < 3 {
		fmt.Printf("Insufficient args: syntax <program> m n")
	}
	m = os.Args[1]
	n = os.Args[2]

	fmt.Println("Case I. A.")
	fmt.Printf("z1 clockwise: 4 <= 2l <= %d\n", m+1)
	fmt.Printf("z2 counter-clockwise: 2k <= n − m + 2` or 2∆ ≤ n − 1
	zombies win:
	2∆ ≤ 2m − 2` + 2 and
	m − 2` − 1 ≤ 2∆


	Case II.A.
	z 1 clockwise: 4 ≤ 2` ≤ m + 1
	z 2 clockwise:
	n − m + 2` ≤ 2∆ and n − 1 ≤ 2∆
	zombies win:
	2∆ ≥ 2n − 2m + 2` and
	2∆ ≤ 2n + 2` − m − 1

	Case I.B.
	z 1 counter-clockwise:
	m + 1 ≤ 2` ≤ 2m − 2
	z 2 counter-clockwise:
	2∆ ≤ n + 1 or 2∆ ≤ n + m − 2`
	zombies win:
	∆ ≤ 2` and
	2` − m + 1 ≤ 2∆


	Case II.B.
	z 1 counter-clockwise:
	m + 1 ≤ 2` ≤ 2m − 2
	z 2 clockwise:
	n + 1 ≤ 2∆
	zombies win:
	n − ∆ ≤ ` + 1 and
	2∆ ≤ 2n + m − 2` + 1

}
