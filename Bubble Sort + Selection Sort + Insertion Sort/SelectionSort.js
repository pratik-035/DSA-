
let arr = [7 ,8, 3, 1, 2]; 

for(let i=0; i<arr.length-1; i++) { 

    let smallest = i; 
    for(j=i+1; j<arr.length; j++) { 
        if(arr[j] < arr[smallest]) {
            smallest = j;
        }
    }
    // swap 
    let temp = arr[i];
    arr[i] = arr[smallest];
    arr[smallest] = temp
}

console.log("Sorted Array : ", arr)