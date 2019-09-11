package main

import "fmt"

func case_1_A(m, n, k, l, Delta int) bool {
	return 4 <= 2*l &&
		2*l <= m+k &&
		(2*Delta <= n-m+2*l || 2*Delta <= n-k)
}

func win_1_A(m, n, k, l, Delta int) bool {
	return Delta <= m-l+1 &&
		m-2*l-k <= 2*Delta
}

func case_1_B(m, n, k, l, Delta int) bool {
	return m+k <= 2*l &&
		2*l <= 2*m-2 &&
		(2*Delta <= n+k || 2*Delta <= n+m-2*l)
}

func win_1_B(m, n, k, l, Delta int) bool {
	return Delta <= l &&
		2*Delta >= 2*l-m+k
}

func case_2_A(m, n, k, l, Delta int) bool {
	return 4 <= 2*l &&
		2*l <= m+k &&
		n-m+2*l <= 2*Delta &&
		n-k <= 2*Delta
}

func win_2_A(m, n, k, l, Delta int) bool {
	return Delta >= n-m+l &&
		2*Delta <= 2*n-m-k+2*l
}

func case_2_B(m, n, k, l, Delta int) bool {
	return m+k <= 2*l &&
		2*l <= 2*m-2 &&
		n+k <= 2*Delta
}

func win_2_B(m, n, k, l, Delta int) bool {
	return Delta >= n-l-1 &&
		2*Delta <= 2*n+m-2*l+k
}

func not_too_big(n, Delta int) bool {
	return n-2*Delta+3 >= 0
}

func find_delta(m, n, k int) (possible_deltas []int) {
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
			//fmt.Printf("Testing Delta=%d, l=%d\n", Delta, l)
			if (!case_1_A(m, n, k, l, Delta) || !win_1_A(m, n, k, l, Delta)) &&
				(!case_1_B(m, n, k, l, Delta) || !win_1_B(m, n, k, l, Delta)) &&
				(!case_2_A(m, n, k, l, Delta) || !win_2_A(m, n, k, l, Delta)) &&
				(!case_2_B(m, n, k, l, Delta) || !win_2_B(m, n, k, l, Delta)) {
				win = false
				//fmt.Printf("Cannot win\n")
			}
		}
		if win && not_too_big(n, Delta) {
			possible_deltas = append(possible_deltas, Delta)
		}
	}
	return
}

func main() {
	max_n, max_m := 10, 10
	k := 3
	for i := 4; i < max_m; i++ {
		for j := i; j < max_n; j++ {
			possible_deltas := find_delta(i, j, k)
			fmt.Printf("%d, %d: ", i, j)
			fmt.Println(possible_deltas)
		}
	}
	// k := 0
	// for k := 0; k < 12; k++ {
	// 	possible_deltas := find_delta(m, n, k)
	// 	fmt.Printf("%d, %d, %d: ", m, n, k)
	// 	fmt.Println(possible_deltas)
	// }
}
