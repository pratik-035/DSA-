
Note that these sorting techniques are not used in production level code
since the time complexity of these sorting is really bad .

But these sorting techniques you should know becuase in interviews these sorting algorithms can be asked. 

Time Complexity : O(n^2)


Also note that for time complexity 
I suggest you to learn matehmatics concepts like AP and GP (i.e Sequence and Series)



For notes and diagram : 

Excalidraw : https://excalidraw.com/#json=JjbeS0voo-oTbgsvlnEVY,jMJEmEMmX214XnYnIQYZYw

app.easier workspace: https://app.eraser.io/workspace/cYp9Po23NFTpceOwbnSp




<h1><b>Bubble Sort</b></h1> 
Definition : Bubble Sort compares each pair of adjacent elements and swaps them if they are in the wrong order. This process repeast until the array is sorted .

============== Example ==================== 
Imagine you have a line of people and you want ti arrange them in order of height. You go from left to right, comparing each person with the next one. If the person on the left is taller, you ask them to swap. You repeat this process again and again until nobody needs to swap - that's Bubble Sort 

============= Difference =====================

Process : Repeatedly swaps adjacent elements 
Best Time Complexity : O(n) (already sorted) 
-> Matlab jaise ki yeh array [1, 2, 3, 4, 5] , jaise yeh phele hi sort hain toh iska aayega O(n) kyunki ismein kuch nhi hain change karne ke liye, toh iska aayega O(n) 
Worst Time : O(n^2)
Space Complexity : O(1)

============== When to use ? =======================
Use bubble sort if you want something easy to understand or teach. 



<h1><b>Selection Sort</b></h1> 

Definition : Selection Sort finds the minimum element from the unsorted part and swaps it with the first unsorted element. It repeats this process until everything is sorted

============== Example ==================== 
Suppose you are selecting the best players for a team. From a group, you pick the best player and place then in the front. Then from the remaining, you again pick the best and so on - that's Selection Sort


============= Difference =====================
Process : Selects min and swaps with correct position .
Best Time Complexity : O(n^2) (dosen't imporve)
-> Because in this it always looks through the entire unsorted part, even if the array is already sorted, means it does the same amount of work, even if the list is already sorted, and that's why its best case is still slow. and it dosen't improve 

for example : let arr = [1,2,3,4,5]; Already sorted 
-> When you run this using selection sort method, searches the entire array for minumum (even though it's already sorted) 
-> Swaps each element unnecessarily  

Worst time complexity : O(n^2) 
Space Complexity : O(1)


============== When to use ? =======================

Use Selection Sort when you care more about reducing the number of swaps 


<h1><b>Insertion Sort</b></h1> 

Insertion Sort : Insertion Sort builds the final sprted array ont item at a time by picking the next element and inserting it into the correct position among the already-sorted elements 

============== Example ==================== 

Think about sorting a hand of playing cards. You pick one card at a time from the deck and place it into the correct position in your hand so that your hand remains sorted - that's Insertion Sort


============= Difference =====================

Proces : Inserts element into the correct place .
Best Time Complexity : O(n) (already sorted)
-> Matlab jaise ki yeh array [1, 2, 3, 4, 5] , jaise yeh phele hi sort hain toh iska aayega O(n) kyunki ismein kuch nhi hain change karne ke liye, toh iska aayega O(n) 

Worst Time : O(n^2) 
Space Complexity : O(1)

============== When to use ? =======================
-> Use Insertion Sort for small or nearly sorted data 
