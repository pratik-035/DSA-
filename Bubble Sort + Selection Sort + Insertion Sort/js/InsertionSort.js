
let arr = [7 ,8, 3, 1, 2];

for(let i=1; i<arr.length; i++) {

    let current = arr[i];
    let j = i-1;

    while(j>=0 && arr[j] > current) {
        arr[j + 1] = arr[j];
        j--;
    }

    // correct position pe current ko daalo
    arr[j+1] = current;
}

console.log("Sorted Array using Insertion Sort : ", arr)