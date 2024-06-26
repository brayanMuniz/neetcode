package main

import "container/list"

type Point struct {
	a, b interface{}
}

func numIslands(grid [][]byte) int {
	if len(grid) == 0 {
		return 0
	}

	rows := len(grid)
	cols := len(grid[0])

	visit := make(map[Point]bool)
	islands := 0

	bfs := func(r, c int, point Point) {
		queue := list.New()
		visit[point] = true
		queue.PushBack(point)

	}

	for r := 0; r < rows-1; r++ {
		for c := 0; c < cols-1; c++ {
			point := Point{r, c}
			if grid[r][c] == '1' && visit[point] == false {
				bfs(r, c, point)
				islands += 1
			}
		}
	}

	return islands
}
