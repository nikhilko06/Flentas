# Flentas
#Coding Challenge

Problem Statements: Sherlock Holmes is working on a case. One day going through evidence, he finds some scribbled text at
corner of victim's diary. Now Sherlock believes that the scribbled text has something to do with the clue
leading to Murderer, so he decides to find every occurrence of all the permutations of the scribbled text in
the entire book. Since this is a huge task, he needs your help, he needs you to figure out if any permutation of
the scribbled text exists in the given text string, so he can save time with the case. Permutation means any
sequence of the string.

Input Format: First line contains number of test cases T. Each test case contains two lines, first line contains pattern and
next line contains a text string. All characters in both the strings are in lowercase only [a-z].

Constraints: 1≤T≤100
             1 ≤ |Pattern| ≤ 1000
             1 ≤ |Text String| ≤ 100000
             
Permitation: It is an arrangement of all or part of a set of objects, with regard to the order of the arrangement(as changing in the order of arrangement will create a new pattern)
For example, suppose we have a set of three letters: M, N, and O.
Now, by how many ways we can arrange these letters.
         
Same for the problem statement to avoid finding all the patterns, we could count the occurence of the characerts in the string, in addition we could still check for the occurence of the pattern would be equal to any part of the text string.

Calculating the permutation: Now the occurence of the characters from index value 0 to length of test case -1, this will tell the occurance of the cases.
if the pattern string matches with the text string it will break the loop and print the YES,
or if it doesn't match it will print the NO.

