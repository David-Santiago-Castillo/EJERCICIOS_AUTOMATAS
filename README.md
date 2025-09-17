

This repository contains the Python implementation of several exercises related to the theory of formal languages and automata.The project covers the construction and simulation of Deterministic Finite Automata (DFA), Finite Automata (FA), and Pushdown Automata (PDA) to recognize different languages. 

This work fulfills the activity's requirements, which include the manual resolution of the problems and the implementation of each solution in Python, using a collaborative workflow on GitHub.

---

### **Exercises Description**

[cite_start]Python solutions were implemented for the 7 proposed problems.Each solution is a function that simulates the behavior of the corresponding automaton and determines whether an input string belongs to the specified language. 

Each problem is detailed below:

***Problem 1:** A **DFA** with a maximum of 4 states was programmed to accept the language represented by the regular expression `((01+10)(11)*0)*(01+10)(11)*` over the alphabet Σ={0,1}. 
* **Problem 2:** A **DFA** was defined for the language formed by strings where the number of 'a's is even and no 'bc' substring exists. 
* **Problem 3:** A **Finite Automaton** was built that accepts a language with the following three conditions:
    * If the string has no '1's, it must have an even number of '0's. 
    * If it has an even number of '1's (>0), it must end with an odd number of '0's.
    * If it has an odd number of '1's, it must end with an even number of '0's. 
* **Problem 4:** A **DFA** was implemented for the language L_3 = L_1 ∪ L_2, which corresponds to strings of alternating '0's and '1's, where L_1 = {(01)^n | n >= 0} and L_2 = {(10)^n | n >= 0}.

* **Problem 5:** A **DFA** equivalent to the regular expression `(((0+10)(10)*(11+0))+11)(0+1)*` was built.
* **Problem 6:** A **Pushdown Automaton (PDA)** was programmed to recognize the language L = {a^i b^j c^k a^i | i, j > 0; k = j}. 
* **Problem 7:** A **Pushdown Automaton (PDA)** was implemented for the language of strings where the number of 'a's is greater than or equal to the number of 'b's (n_a(w) >= n_b(w)). 


### **Team Members**

