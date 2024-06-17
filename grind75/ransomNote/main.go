package main

// make a map that consist of the frequencies of magazine
// loop over ransomNote, if it is in magazine, remove it from magazine
//
//	if its not, return false
//
// return true

func canConstruct(ransomNote string, magazine string) bool {
	m := make(map[rune]int)
	for _, c := range magazine {
		m[c] += 1
	}

	for _, c := range ransomNote {
		if m[c] == 0 {
			return false
		}
		m[c] -= 1
	}
	return true

}
