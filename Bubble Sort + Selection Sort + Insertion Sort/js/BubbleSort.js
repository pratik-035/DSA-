
let arr = [7, 8, 3, 1, 2]; 

for(let i=0; i<arr.length-1; i++) { 

    for(let j=0; j<arr.length-1-i; j++) { 
        

        // swap 
        if(arr[j] > arr[j+1]) { 
            let temp = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = temp;
        }
    }
}

console.log("Sorted Array : ", arr)