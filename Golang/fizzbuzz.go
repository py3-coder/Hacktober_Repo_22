// A simple implementation of FizzBuzz in Go
// Author: @jmmille
package main

import "fmt"

func main() {
	for i := 0; i < 101; i++ {
		if i%3 == 0 && i%5 == 0 {
			fmt.Println("fizzbuzz")
			continue
		} else if i%3 == 0 {
			fmt.Println("fizz")
			continue
		} else if i%5 == 0 {
			fmt.Println("buzz")
			continue
		}
		fmt.Println(i)
	}
}
