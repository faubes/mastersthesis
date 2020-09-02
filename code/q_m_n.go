package main

import ( 
"fmt"
"os"
"strconv"
)

func case_1_A(m, n, l, Delta int) bool {
	return 4 <= 2*l &&
		2*l <= m+1 &&
		(2*Delta <= n-m+2*l || 2*Delta <= n-1)
}

func win_1_A(m, n, l, Delta int) bool {
	return 2*Delta <= 2*m-2*l+2 &&
		m-2*l-1 <= 2*Delta
}

func case_1_B(m, n, l, Delta int) bool {
	return m+1 <= 2*l &&
		2*l <= 2*m-2 &&
		(2*Delta <= 2*l || 2*l-m+1 <= 2*Delta)
}

func win_1_B(m, n, l, Delta int) bool {
	return 2*Delta <= 2*l &&
		2*l-m+1 <= 2*Delta
}

func case_2_A(m, n, l, Delta int) bool {
	return 4 <= 2*l &&
		2*l <= m+1 &&
		n-m+2*l <= 2*Delta &&
		n-1 <= 2*Delta
}

func win_2_A(m, n, l, Delta int) bool {
	return 2*Delta >= 2*n-2*m+2*l &&
		2*Delta <= 2*n+2*l-m-1
}

func case_2_B(m, n, l, Delta int) bool {
	return m+1 <= 2*l &&
		2*l <= 2*m-2 &&
		n+1 <= 2*Delta
}

func win_2_B(m, n, l, Delta int) bool {
	return n-Delta <= l+1 &&
		2*Delta <= 2*n+m-2*l+1
}

func not_too_big(n, Delta int) bool {
	return n-2*Delta+3 >= 0
}

func find_delta(m, n int) (possible_deltas []int) {
	possible_deltas = make([]int, 0)

	for Delta := 0; Delta <= n; Delta++ {
		win := true
		var l_upper int
		if Delta == 0 {
			l_upper = m - 2
		} else {
			l_upper = m - 1
		}

		for l := 2; l <= l_upper; l++ {
			if (!case_1_A(m, n, l, Delta) || !win_1_A(m, n, l, Delta)) &&
				(!case_1_B(m, n, l, Delta) || !win_1_B(m, n, l, Delta)) &&
				(!case_2_A(m, n, l, Delta) || !win_2_A(m, n, l, Delta)) &&
				(!case_2_B(m, n, l, Delta) || !win_2_B(m, n, l, Delta)) {
				win = false
			}
		}
		if win && not_too_big(n, Delta) {
			possible_deltas = append(possible_deltas, Delta)
		}
	}
	return
}

func find_offset(m, n int, possible_deltas []int) (possible_offsets []int) {
	possible_offsets = make([]int, 0)
	for delta := range possible_deltas {
		for offset := (n - 2*delta - 5)/4; offset <= (n - 2*delta)/4; offset++ {
			if offset > 0 {
				possible_offsets = append(possible_offsets, offset)
			}
		}
	}
	return possible_offsets
}

func main() {
//	max_n, max_m := 12, 12
//	for i := 4; i < max_m; i++ {
//		for j := i; j < max_n; j++ {
//			possible_deltas := find_delta(i, j)
	if len(os.Args) < 2 {
		fmt.Println("Need two arguments, for m and n")
		return
	}
	m, _ := strconv.Atoi(os.Args[1])
	n, _ := strconv.Atoi(os.Args[2])
	possible_deltas := find_delta(m, n)
	for _, delta := range possible_deltas {
		fmt.Printf("With Delta: %v ", delta)
		possible_offsets := make([]int, 0)
		for offset := (n - 2*delta - 5)/4; offset <= (n - 2*delta)/4; offset++ {
			if offset > 0 {		
				possible_offsets = append(possible_offsets, offset)
			}
		}
	      fmt.Printf("Possible offset: %v\n", possible_offsets)
	}
}
