package main

type MyQueue struct {
	s1 []int
	s2 []int
}

func Constructor() MyQueue {
	return MyQueue{
		s1: []int{},
		s2: []int{},
	}
}

func (this *MyQueue) Push(x int) {
	this.s1 = append(this.s1, x)

}

func (this *MyQueue) Pop() int {
	// while s1 not empty
	// remove last element from s1
	// push that to s2
	for len(this.s1) > 0 {
		poppedValue := this.s1[len(this.s1)-1]
		this.s2 = append(this.s2, poppedValue)
		this.s1 = this.s1[:len(this.s1)-1]
	}

	// remove last element from s2
	popReturn := this.s2[len(this.s2)-1]
	this.s2 = this.s2[:len(this.s2)-1]

	// add all the elemnts back to s1
	for len(this.s2) > 0 {
		poppedValue := this.s2[len(this.s2)-1]
		this.s1 = append(this.s1, poppedValue)
		this.s2 = this.s2[:len(this.s2)-1]
	}

	// return the popped element
	return popReturn

}

func (this *MyQueue) Peek() int {
	for len(this.s1) > 0 {
		poppedValue := this.s1[len(this.s1)-1]
		this.s2 = append(this.s2, poppedValue)
		this.s1 = this.s1[:len(this.s1)-1]
	}

	// remove last element from s2
	popReturn := this.s2[len(this.s2)-1]

	// add all the elemnts back to s1
	for len(this.s2) > 0 {
		poppedValue := this.s2[len(this.s2)-1]
		this.s1 = append(this.s1, poppedValue)
		this.s2 = this.s2[:len(this.s2)-1]
	}

	return popReturn

}

func (this *MyQueue) Empty() bool {
	return len(this.s1) == 0 && len(this.s2) == 0
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */
