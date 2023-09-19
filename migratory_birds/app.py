'''// https://www.hackerrank.com/challenges/migratory-birds/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

// Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

// Example

// arr = [1,1,2,2,3]

// There are two each of types 1 and 2, and one sighting of type 3. Pick the lower of the two types seen twice: type 1.

// Function Description

// Complete the migratoryBirds function in the editor below.

// migratoryBirds has the following parameter(s):

// int arr[n]: the types of birds sighted

// Returns
// int: the lowest type id of the most frequently sighted birds

// Input Format
// The first line contains an integer, , the size of .
// The second line describes  as  space-separated integers, each a type number of the bird sighted.

// Constraints
// 5 <= n <= 2 * 10^5
// It is guaranteed that each type is 1, 2, 3, 4, or 5.

// Sample Input 0
// 6
// 1 4 4 4 5 3

// Sample Output 0
// 4

Approach: migratoryBirds function, initialize list called bird_count, will have six elements, loop over each bird in array, increase bird count, use max to return highest value in the bird_count list, loop over bird_count list, if bird_count[i] == max_sightings, return i, this will return the lowest type id of the most frequently sighted birds
'''

def migratoryBirds(arr):
   
    bird_count = [0] * 6 
    for bird in arr:
        bird_count[bird] += 1

 
  
    max_sightings = max(bird_count)
    for i in range(len(bird_count)):
        if bird_count[i] == max_sightings:
            return i  

'''arr = [1, 4, 4, 4, 5, 3] works with this input, check if it will work if it will print the lower of types seen more than once'''
arr = [1, 4, 4, 4, 5, 5, 5, 3]
print(migratoryBirds(arr)) 