package main

import (
	"container/heap"
)

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

// Defines Fields
type KthLargest struct {
	k    int
	heap IntHeap
}

// Constructor
func Constructor(k int, nums []int) KthLargest {
	// creating a pointer to a new IntHeap object.
	h := &IntHeap{}
	heap.Init(h)
	kl := KthLargest{k: k, heap: *h}

	for _, num := range nums {
		kl.Add(num)
	}

	// Pop until the length is of k
	for kl.heap.Len() > k {
		kl.heap.Pop()
	}

	return kl
}

// Methods
func (this *KthLargest) Add(val int) int {
	heap.Push(&this.heap, val)

	if this.heap.Len() > this.k {
		heap.Pop(&this.heap)
	}
	return this.heap[0]
}
