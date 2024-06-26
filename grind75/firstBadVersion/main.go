package main

/**
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */

func firstBadVersion(n int) int {
	left := 1
	right := n
	badVersion := n

	for left < right {
		mid := (left + right) / 2
		if isBadVersion(mid) {
			badVersion = min(badVersion, mid)
			right = mid
		} else {
			left = mid + 1
		}
	}

	return badVersion
}
